import pandas as pd

import grpc
import logging
import random
from concurrent import futures

import PokemonServer_pb2
import PokemonServer_pb2_grpc

# Remove the strange variations such as partner, mega or region specific varients of pokemons
def cleanData():
    df = pd.read_csv("PokemonDb.csv")
    df = df[df['Variation'].isnull()]
    df = df.drop(columns='Variation')
    df = df.drop(columns='Total')
    df = df.drop(columns='Sp.Atk')
    df = df.drop(columns='Sp.Def')

    return df

class PokemonServer(PokemonServer_pb2_grpc.PokeDataServicer):
    

    def __init__(self):
        self.pokemon = cleanData()
        self.PokeCount = 0
        self.PokeMax = self.pokemon.shape[0]

    def RequestPokemon(self, request, context):
        print("Recieved Request", flush= True)
        pokemon = self.pokemon.iloc[self.PokeCount]



        PokeResponse = PokemonServer_pb2.PokeResponse(
            Name = str(pokemon[0]),
            Type1 = str(pokemon[1]),
            Type2 = str(pokemon[2]),
            HP = int(pokemon[3]),
            Attack = int(pokemon[4]),
            Defense = int(pokemon[5]),
            Speed = int(pokemon[6])
        )
        
        self.PokeCount = self.PokeCount + 1
        return PokeResponse


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    PokemonServer_pb2_grpc.add_PokeDataServicer_to_server(PokemonServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()