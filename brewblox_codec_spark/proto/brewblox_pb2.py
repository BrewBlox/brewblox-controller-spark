# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: brewblox.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='brewblox.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0e\x62rewblox.proto\x1a google/protobuf/descriptor.proto\"3\n\x14\x42rewbloxFieldOptions\x12\x0c\n\x04unit\x18\x01 \x01(\t\x12\r\n\x05scale\x18\x02 \x01(\r:G\n\x08\x62rewblox\x12\x1d.google.protobuf.FieldOptions\x18\xf3\x07 \x01(\x0b\x32\x15.BrewbloxFieldOptionsb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


BREWBLOX_FIELD_NUMBER = 1011
brewblox = _descriptor.FieldDescriptor(
  name='brewblox', full_name='brewblox', index=0,
  number=1011, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None, file=DESCRIPTOR)


_BREWBLOXFIELDOPTIONS = _descriptor.Descriptor(
  name='BrewbloxFieldOptions',
  full_name='BrewbloxFieldOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unit', full_name='BrewbloxFieldOptions.unit', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale', full_name='BrewbloxFieldOptions.scale', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=103,
)

DESCRIPTOR.message_types_by_name['BrewbloxFieldOptions'] = _BREWBLOXFIELDOPTIONS
DESCRIPTOR.extensions_by_name['brewblox'] = brewblox
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BrewbloxFieldOptions = _reflection.GeneratedProtocolMessageType('BrewbloxFieldOptions', (_message.Message,), dict(
  DESCRIPTOR = _BREWBLOXFIELDOPTIONS,
  __module__ = 'brewblox_pb2'
  # @@protoc_insertion_point(class_scope:BrewbloxFieldOptions)
  ))
_sym_db.RegisterMessage(BrewbloxFieldOptions)

brewblox.message_type = _BREWBLOXFIELDOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(brewblox)

# @@protoc_insertion_point(module_scope)