FROM python:3-stretch
WORKDIR /app

COPY /container-client /app
COPY /grpc-files/PokemonServer_pb2_grpc.py /app
COPY /grpc-files/PokemonServer_pb2.py /app

RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt
CMD ["python3", "pokemon-client.py"]