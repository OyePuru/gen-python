# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rexample.proto\x12\x07\x65xample\"\x13\n\x11\x45xampleGetRequest\"%\n\x12\x45xampleGetResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\"\n\x12\x45xamplePostRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"&\n\x13\x45xamplePostResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xb3\x01\n\x0e\x45xampleService\x12N\n\x11\x45xampleGetHandler\x12\x1a.example.ExampleGetRequest\x1a\x1b.example.ExampleGetResponse\"\x00\x12Q\n\x12\x45xamplePostHandler\x12\x1b.example.ExamplePostRequest\x1a\x1c.example.ExamplePostResponse\"\x00\x42=Z;github.com/CrossBorder-Co/sales-marker-proto/gen/go/exampleb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'example_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z;github.com/CrossBorder-Co/sales-marker-proto/gen/go/example'
  _globals['_EXAMPLEGETREQUEST']._serialized_start=26
  _globals['_EXAMPLEGETREQUEST']._serialized_end=45
  _globals['_EXAMPLEGETRESPONSE']._serialized_start=47
  _globals['_EXAMPLEGETRESPONSE']._serialized_end=84
  _globals['_EXAMPLEPOSTREQUEST']._serialized_start=86
  _globals['_EXAMPLEPOSTREQUEST']._serialized_end=120
  _globals['_EXAMPLEPOSTRESPONSE']._serialized_start=122
  _globals['_EXAMPLEPOSTRESPONSE']._serialized_end=160
  _globals['_EXAMPLESERVICE']._serialized_start=163
  _globals['_EXAMPLESERVICE']._serialized_end=342
# @@protoc_insertion_point(module_scope)