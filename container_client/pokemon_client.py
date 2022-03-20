from __future__ import print_function
import logging
from collections import Counter

import grpc
import time
import random
import redis
import PokemonServer_pb2
import PokemonServer_pb2_grpc

# Criteria to Analyse
# Average pokemon HP - 1.
# Most Common Type of pokemon over 3 minutes - 2.
# Weakest Pokemon Attack - 3.
# Tankiet Pokemon So Far (Best HP and Attack)- 4.

def run():
    # while True: Uncomment to have dataset start again
        with grpc.insecure_channel('pokemon_server:50051') as channel:
            stub = PokemonServer_pb2_grpc.PokeDataStub(channel)
            allPokemon = []             # Contains a list of pokemone for the website
            pokemon_types = []          # For Tracking most common type over time
            pokemon_names = []          # For Tracking most common type over time
            pokemon_hp = []             # For Tracking HP
            pokemon_attack = []         # For Tracking attack
            pokemon_toughness = []      # For tracking toughness (Hp + Attack)
            start_time = time.time()    # Store start time for check later

            for pokemon in stub.RequestPokemon(PokemonServer_pb2.PokeRequest(numberOfPokemon=int(1))):
                # time.sleep(random.uniform(0.35, 0.65))  # On Average 2 records per second
                print("Requesting Pokemon", flush=True)
                # Convert to proper variable
                pokemonData = [str(pokemon.Name), str(pokemon.Type1), str(pokemon.Type2), int(pokemon.HP), int(pokemon.Attack), int(pokemon.Defense), int(pokemon.Speed)]
                allPokemon.append(pokemonData)
                pokemon_names.append(pokemonData[0])
                
                
                # Get most common type of Pokemon
                for x in range(1, 3):
                    if pokemonData[x] != 'nan':
                        pokemon_types.append(pokemonData[x])

                        if (time.time() - start_time) >= 180:    # If it's been 3 mins (180 Seconds) , remove one for every added type.
                            pokemon_types.pop(0)
                mostCommonType = Counter(pokemon_types).most_common(1)[0][0]
                mostCommonTypeLen = len(pokemon_types)
            


                # Average Pokemon HP
                pokemon_hp.append(pokemonData[3])
                averageHP = sum(pokemon_hp) / len(pokemon_hp)

                # Weakest Pokemon Attack
                pokemon_attack.append(pokemonData[4])
                weakestAttack = min(pokemon_attack)
                strongestAttack = max(pokemon_attack)

                # Toughest Pokemon
                pokemon_toughness.append(pokemonData[3] + pokemonData[4])
                toughestPokemon = max(pokemon_toughness)
                if pokemonData[3] + pokemonData[4] == toughestPokemon:
                    toughestPokemonName = pokemonData[0]

                # Send Data to website
                try:
                    conn = redis.StrictRedis(host='redis', port=6379)

                    # conn.flushall()

                    conn.set("mostCommonType",  mostCommonType)
                    conn.set("mostCommonTypeLen",  mostCommonTypeLen)
                    conn.set("averageHP",  averageHP)
                    conn.set("weakestAttack",  weakestAttack)
                    conn.set("strongestAttack",  strongestAttack)
                    conn.set("toughestPokemon",  toughestPokemon)
                    conn.set("toughestPokemonName",  toughestPokemonName)
                    conn.set("allPokemon", str(allPokemon))
                    conn.set("allHp", str(pokemon_hp))
                    conn.set("allAttack", str(pokemon_attack))
                    conn.set("allNames", str(pokemon_names))

                    if (time.time() - start_time) >= 180:    # If it's been 3 mins (180 Seconds) , remove one for every added type.
                        conn.set("rollingStatus", "Rolling has started")
                    else:
                        conn.set("rollingStatus", "Not 3 minues yet")

                    print("Sending Analytics", flush=True)
                    
                except Exception as ex:
                    print("Error: ", ex, flush=True)
                    
if __name__ == '__main__':
    # Needed to print out
    logging.basicConfig()
    run()