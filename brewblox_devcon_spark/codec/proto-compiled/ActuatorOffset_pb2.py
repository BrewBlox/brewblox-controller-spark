# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ActuatorOffset.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2
import nanopb_pb2 as nanopb__pb2
import AnalogConstraints_pb2 as AnalogConstraints__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ActuatorOffset.proto',
  package='blox',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x14\x41\x63tuatorOffset.proto\x12\x04\x62lox\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\x1a\x17\x41nalogConstraints.proto\"\xec\x03\n\x0e\x41\x63tuatorOffset\x12\x1d\n\x08targetId\x18\x01 \x01(\rB\x0b\x8a\xb5\x18\x02\x18\x01\x92?\x02\x38\x10\x12 \n\x0breferenceId\x18\x03 \x01(\rB\x0b\x8a\xb5\x18\x02\x18\x01\x92?\x02\x38\x10\x12\x44\n\x17referenceSettingOrValue\x18\x04 \x01(\x0e\x32#.blox.ActuatorOffset.SettingOrValue\x12)\n\x07setting\x18\x06 \x01(\x11\x42\x18\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02(\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12\'\n\x05value\x18\x07 \x01(\x11\x42\x18\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12.\n\rconstrainedBy\x18\x08 \x01(\x0b\x32\x17.blox.AnalogConstraints\x12/\n\x0e\x64rivenTargetId\x18\t \x01(\rB\x17\x8a\xb5\x18\x02\x18\x01\x8a\xb5\x18\x02@\x01\x92?\x02\x38\x10\x8a\xb5\x18\x02(\x01\x12\x0f\n\x07\x65nabled\x18\n \x01(\x08\x12*\n\x0e\x64\x65siredSetting\x18\x0b \x01(\x11\x42\x12\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12(\n\x0estrippedFields\x18\x63 \x03(\rB\x10\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x10\x92?\x02\x10\x02\"(\n\x0eSettingOrValue\x12\x0b\n\x07SETTING\x10\x00\x12\t\n\x05VALUE\x10\x01:\r\x8a\xb5\x18\x03\x18\xb4\x02\x8a\xb5\x18\x02H\x05\x62\x06proto3'
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,AnalogConstraints__pb2.DESCRIPTOR,])



_ACTUATOROFFSET_SETTINGORVALUE = _descriptor.EnumDescriptor(
  name='SettingOrValue',
  full_name='blox.ActuatorOffset.SettingOrValue',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SETTING', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALUE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=523,
  serialized_end=563,
)
_sym_db.RegisterEnumDescriptor(_ACTUATOROFFSET_SETTINGORVALUE)


_ACTUATOROFFSET = _descriptor.Descriptor(
  name='ActuatorOffset',
  full_name='blox.ActuatorOffset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='targetId', full_name='blox.ActuatorOffset.targetId', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\030\001\222?\0028\020', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='referenceId', full_name='blox.ActuatorOffset.referenceId', index=1,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\030\001\222?\0028\020', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='referenceSettingOrValue', full_name='blox.ActuatorOffset.referenceSettingOrValue', index=2,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='setting', full_name='blox.ActuatorOffset.setting', index=3,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002(\001\212\265\030\003\020\200 \222?\0028 ', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='blox.ActuatorOffset.value', index=4,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='constrainedBy', full_name='blox.ActuatorOffset.constrainedBy', index=5,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='drivenTargetId', full_name='blox.ActuatorOffset.drivenTargetId', index=6,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\030\001\212\265\030\002@\001\222?\0028\020\212\265\030\002(\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='blox.ActuatorOffset.enabled', index=7,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='desiredSetting', full_name='blox.ActuatorOffset.desiredSetting', index=8,
      number=11, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\003\020\200 \222?\0028 ', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strippedFields', full_name='blox.ActuatorOffset.strippedFields', index=9,
      number=99, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\222?\0028\020\222?\002\020\002', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ACTUATOROFFSET_SETTINGORVALUE,
  ],
  serialized_options=b'\212\265\030\003\030\264\002\212\265\030\002H\005',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=578,
)

_ACTUATOROFFSET.fields_by_name['referenceSettingOrValue'].enum_type = _ACTUATOROFFSET_SETTINGORVALUE
_ACTUATOROFFSET.fields_by_name['constrainedBy'].message_type = AnalogConstraints__pb2._ANALOGCONSTRAINTS
_ACTUATOROFFSET_SETTINGORVALUE.containing_type = _ACTUATOROFFSET
DESCRIPTOR.message_types_by_name['ActuatorOffset'] = _ACTUATOROFFSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ActuatorOffset = _reflection.GeneratedProtocolMessageType('ActuatorOffset', (_message.Message,), {
  'DESCRIPTOR' : _ACTUATOROFFSET,
  '__module__' : 'ActuatorOffset_pb2'
  # @@protoc_insertion_point(class_scope:blox.ActuatorOffset)
  })
_sym_db.RegisterMessage(ActuatorOffset)


_ACTUATOROFFSET.fields_by_name['targetId']._options = None
_ACTUATOROFFSET.fields_by_name['referenceId']._options = None
_ACTUATOROFFSET.fields_by_name['setting']._options = None
_ACTUATOROFFSET.fields_by_name['value']._options = None
_ACTUATOROFFSET.fields_by_name['drivenTargetId']._options = None
_ACTUATOROFFSET.fields_by_name['desiredSetting']._options = None
_ACTUATOROFFSET.fields_by_name['strippedFields']._options = None
_ACTUATOROFFSET._options = None
# @@protoc_insertion_point(module_scope)
