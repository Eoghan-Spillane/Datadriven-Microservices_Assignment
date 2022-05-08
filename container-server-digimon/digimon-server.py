from numpy import append
import pandas as pd

import grpc
import logging
import random
import time
from concurrent import futures

import PokemonServer_pb2
import PokemonServer_pb2_grpc

# Remove the strange variations such as partner, mega or region specific varients of pokemons
def cleanData():
    df = pd.read_csv("DigiDB_digimonlist.csv")
    df = df.drop(columns={'Number', 'Stage', 'Memory'})
    df = df.drop(columns={'Equip Slots', 'Lv50 Int', 'Lv50 SP'})

    # Match pokemon naming scheme
    df = df.rename(columns = {'Digimon':'Name', 'Type':'Type1', 'Attribute':'Type2', 'Lv 50 HP':'HP'})
    df = df.rename(columns = {'Lv50 Atk':'Attack', 'Lv50 Def':'Defense', 'Lv50 Spd':'Speed'})
    
    return df

class DigimonServer(PokemonServer_pb2_grpc.PokeDataServicer):
    
    def __init__(self):
        self.pokemonData = cleanData()
        self.PokeCount = self.pokemonData.shape[0]

    def RequestPokemon(self, request, context):
        print("Recieved -> RequestPokemon: " + str(request.numberOfPokemon), flush= True)
        
        # Randomise the pokemon Order
        shuffled_order = []
        for x in range(self.PokeCount): 
            shuffled_order.append(x)

        random.shuffle(shuffled_order)

        # When using yield the place in the loop is remembered.
        for poke in shuffled_order:
            # on average stream 2 per second
            time.sleep(random.uniform(0.35, 0.65))
            print("Server -> Response")
            
            pokemon = self.pokemonData.iloc[poke]

            PokeResponse = PokemonServer_pb2.PokeResponse(
                Name = str(pokemon[0]),
                Type1 = str(pokemon[1]),
                Type2 = str(pokemon[2]),
                HP = int(pokemon[3]),
                Attack = int(pokemon[4]),
                Defense = int(pokemon[5]),
                Speed = int(pokemon[6])
            )
            
            yield PokeResponse


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    PokemonServer_pb2_grpc.add_PokeDataServicer_to_server(DigimonServer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    # Needed to print out
    logging.basicConfig()
    serve()