# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PokemonServer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13PokemonServer.proto\"&\n\x0bPokeRequest\x12\x17\n\x0fnumberOfPokemon\x18\x01 \x01(\x05\"v\n\x0cPokeResponse\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\r\n\x05Type1\x18\x02 \x01(\t\x12\r\n\x05Type2\x18\x03 \x01(\t\x12\n\n\x02HP\x18\x04 \x01(\x05\x12\x0e\n\x06\x41ttack\x18\x05 \x01(\x05\x12\x0f\n\x07\x44\x65\x66\x65nse\x18\x06 \x01(\x05\x12\r\n\x05Speed\x18\x07 \x01(\x05\x32=\n\x08PokeData\x12\x31\n\x0eRequestPokemon\x12\x0c.PokeRequest\x1a\r.PokeResponse\"\x00\x30\x01\x62\x06proto3')



_POKEREQUEST = DESCRIPTOR.message_types_by_name['PokeRequest']
_POKERESPONSE = DESCRIPTOR.message_types_by_name['PokeResponse']
PokeRequest = _reflection.GeneratedProtocolMessageType('PokeRequest', (_message.Message,), {
  'DESCRIPTOR' : _POKEREQUEST,
  '__module__' : 'PokemonServer_pb2'
  # @@protoc_insertion_point(class_scope:PokeRequest)
  })
_sym_db.RegisterMessage(PokeRequest)

PokeResponse = _reflection.GeneratedProtocolMessageType('PokeResponse', (_message.Message,), {
  'DESCRIPTOR' : _POKERESPONSE,
  '__module__' : 'PokemonServer_pb2'
  # @@protoc_insertion_point(class_scope:PokeResponse)
  })
_sym_db.RegisterMessage(PokeResponse)

_POKEDATA = DESCRIPTOR.services_by_name['PokeData']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _POKEREQUEST._serialized_start=23
  _POKEREQUEST._serialized_end=61
  _POKERESPONSE._serialized_start=63
  _POKERESPONSE._serialized_end=181
  _POKEDATA._serialized_start=183
  _POKEDATA._serialized_end=244
# @@protoc_insertion_point(module_scope)
