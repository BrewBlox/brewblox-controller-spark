# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SetPointSimple.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='SetPointSimple.proto',
  package='blox',
  syntax='proto3',
  serialized_pb=_b('\n\x14SetPointSimple.proto\x12\x04\x62lox\"\\\n\x0eSetPointSimple\x12/\n\x08settings\x18\x01 \x01(\x0b\x32\x1d.blox.SetPointSimple.Settings\x1a\x19\n\x08Settings\x12\r\n\x05value\x18\x01 \x01(\x11\"K\n\x18SetPointSimple_Persisted\x12/\n\x08settings\x18\x01 \x01(\x0b\x32\x1d.blox.SetPointSimple.Settingsb\x06proto3')
)




_SETPOINTSIMPLE_SETTINGS = _descriptor.Descriptor(
  name='Settings',
  full_name='blox.SetPointSimple.Settings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='blox.SetPointSimple.Settings.value', index=0,
      number=1, type=17, cpp_type=1, label=1,
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
  serialized_start=97,
  serialized_end=122,
)

_SETPOINTSIMPLE = _descriptor.Descriptor(
  name='SetPointSimple',
  full_name='blox.SetPointSimple',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='settings', full_name='blox.SetPointSimple.settings', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SETPOINTSIMPLE_SETTINGS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=122,
)


_SETPOINTSIMPLE_PERSISTED = _descriptor.Descriptor(
  name='SetPointSimple_Persisted',
  full_name='blox.SetPointSimple_Persisted',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='settings', full_name='blox.SetPointSimple_Persisted.settings', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=124,
  serialized_end=199,
)

_SETPOINTSIMPLE_SETTINGS.containing_type = _SETPOINTSIMPLE
_SETPOINTSIMPLE.fields_by_name['settings'].message_type = _SETPOINTSIMPLE_SETTINGS
_SETPOINTSIMPLE_PERSISTED.fields_by_name['settings'].message_type = _SETPOINTSIMPLE_SETTINGS
DESCRIPTOR.message_types_by_name['SetPointSimple'] = _SETPOINTSIMPLE
DESCRIPTOR.message_types_by_name['SetPointSimple_Persisted'] = _SETPOINTSIMPLE_PERSISTED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetPointSimple = _reflection.GeneratedProtocolMessageType('SetPointSimple', (_message.Message,), dict(

  Settings = _reflection.GeneratedProtocolMessageType('Settings', (_message.Message,), dict(
    DESCRIPTOR = _SETPOINTSIMPLE_SETTINGS,
    __module__ = 'SetPointSimple_pb2'
    # @@protoc_insertion_point(class_scope:blox.SetPointSimple.Settings)
    ))
  ,
  DESCRIPTOR = _SETPOINTSIMPLE,
  __module__ = 'SetPointSimple_pb2'
  # @@protoc_insertion_point(class_scope:blox.SetPointSimple)
  ))
_sym_db.RegisterMessage(SetPointSimple)
_sym_db.RegisterMessage(SetPointSimple.Settings)

SetPointSimple_Persisted = _reflection.GeneratedProtocolMessageType('SetPointSimple_Persisted', (_message.Message,), dict(
  DESCRIPTOR = _SETPOINTSIMPLE_PERSISTED,
  __module__ = 'SetPointSimple_pb2'
  # @@protoc_insertion_point(class_scope:blox.SetPointSimple_Persisted)
  ))
_sym_db.RegisterMessage(SetPointSimple_Persisted)


# @@protoc_insertion_point(module_scope)
