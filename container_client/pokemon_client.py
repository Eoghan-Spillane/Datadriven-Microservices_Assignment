from __future__ import print_function
import logging

import grpc
import PokemonServer_pb2
import PokemonServer_pb2_grpc

def run():
        channel = grpc.insecure_channel('pokemon_server:50051')
        stub = PokemonServer_pb2_grpc.PokeDataStub(channel)
        
        while True:
            for pokemon in stub.RequestPokemon(PokemonServer_pb2.PokeRequest(numberOfPokemon = int(1))):
                try:
                    print(pokemon.Name + " - " +  str(pokemon.HP), flush = True)
                except Exception as ex:
                    print(ex)

if __name__ == '__main__':
    logging.basicConfig()
    run()