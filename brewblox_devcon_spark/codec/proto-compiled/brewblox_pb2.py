# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: brewblox.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='brewblox.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0e\x62rewblox.proto\x1a google/protobuf/descriptor.proto\"\xfb\x07\n\x0f\x42rewbloxOptions\x12\'\n\x04unit\x18\x01 \x01(\x0e\x32\x19.BrewbloxOptions.UnitType\x12\r\n\x05scale\x18\x02 \x01(\r\x12+\n\x07objtype\x18\x03 \x01(\x0e\x32\x1a.BrewbloxOptions.BlockType\x12\r\n\x05hexed\x18\x04 \x01(\x08\x12\x10\n\x08readonly\x18\x05 \x01(\x08\x12\x0e\n\x06logged\x18\x06 \x01(\x08\x12\x0e\n\x06hexstr\x18\x07 \x01(\x08\x12\x0e\n\x06\x64riven\x18\x08 \x01(\x08\"\xfc\x04\n\tBlockType\x12\x0b\n\x07Invalid\x10\x00\x12\x19\n\x15ProcessValueInterface\x10\x01\x12\x17\n\x13TempSensorInterface\x10\x02\x12\x1f\n\x1bSetpointSensorPairInterface\x10\x04\x12\x1b\n\x17\x41\x63tuatorAnalogInterface\x10\x05\x12\x1c\n\x18\x41\x63tuatorDigitalInterface\x10\x06\x12\x15\n\x11\x42\x61lancerInterface\x10\x07\x12\x12\n\x0eMutexInterface\x10\x08\x12\x1a\n\x16OneWireDeviceInterface\x10\t\x12\x16\n\x12OneWireIOInterface\x10\n\x12\x08\n\x03\x41ny\x10\xff\x01\x12\x0c\n\x07SysInfo\x10\x80\x02\x12\x0f\n\nOneWireBus\x10\x82\x02\x12\n\n\x05Ticks\x10\x81\x02\x12\x13\n\x0eTempSensorMock\x10\xad\x02\x12\x16\n\x11TempSensorOneWire\x10\xae\x02\x12\x17\n\x12SetpointSensorPair\x10\xaf\x02\x12\x08\n\x03Pid\x10\xb0\x02\x12\x17\n\x12\x41\x63tuatorAnalogMock\x10\xb1\x02\x12\x10\n\x0b\x41\x63tuatorPin\x10\xb2\x02\x12\x10\n\x0b\x41\x63tuatorPwm\x10\xb3\x02\x12\x13\n\x0e\x41\x63tuatorOffset\x10\xb4\x02\x12\r\n\x08\x42\x61lancer\x10\xb5\x02\x12\n\n\x05Mutex\x10\xb6\x02\x12\x14\n\x0fSetpointProfile\x10\xb7\x02\x12\x11\n\x0cWiFiSettings\x10\xb8\x02\x12\x12\n\rTouchSettings\x10\xb9\x02\x12\x14\n\x0f\x44isplaySettings\x10\xba\x02\x12\x0b\n\x06\x44S2413\x10\xbb\x02\x12\x14\n\x0f\x41\x63tuatorOneWire\x10\xbc\x02\x12\x0b\n\x06\x44S2408\x10\xbd\x02\"\xb2\x01\n\x08UnitType\x12\n\n\x06NotSet\x10\x00\x12\x08\n\x04Temp\x10\x01\x12\r\n\tDeltaTemp\x10\x02\x12\x14\n\x10\x44\x65ltaTempPerTime\x10\x03\x12\x08\n\x04Time\x10\x04\x12\x0f\n\x0bInverseTemp\x10\x05\x12\x11\n\rDeltaTempTime\x10\x06\x12\x0c\n\x08LongTime\x10\x07\x12\x15\n\x11\x44\x65ltaTempLongTime\x10\x08\x12\x18\n\x14\x44\x65ltaTempPerLongTime\x10\t:C\n\x08\x62rewblox\x12\x1d.google.protobuf.FieldOptions\x18\xd1\x86\x03 \x01(\x0b\x32\x10.BrewbloxOptions:I\n\x0c\x62rewblox_msg\x12\x1f.google.protobuf.MessageOptions\x18\xd1\x86\x03 \x01(\x0b\x32\x10.BrewbloxOptionsb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


BREWBLOX_FIELD_NUMBER = 50001
brewblox = _descriptor.FieldDescriptor(
  name='brewblox', full_name='brewblox', index=0,
  number=50001, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
BREWBLOX_MSG_FIELD_NUMBER = 50001
brewblox_msg = _descriptor.FieldDescriptor(
  name='brewblox_msg', full_name='brewblox_msg', index=1,
  number=50001, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)

_BREWBLOXOPTIONS_BLOCKTYPE = _descriptor.EnumDescriptor(
  name='BlockType',
  full_name='BrewbloxOptions.BlockType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Invalid', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ProcessValueInterface', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TempSensorInterface', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SetpointSensorPairInterface', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActuatorAnalogInterface', index=4, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActuatorDigitalInterface', index=5, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BalancerInterface', index=6, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MutexInterface', index=7, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OneWireDeviceInterface', index=8, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OneWireIOInterface', index=9, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Any', index=10, number=255,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SysInfo', index=11, number=256,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OneWireBus', index=12, number=258,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Ticks', index=13, number=257,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TempSensorMock', index=14, number=301,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TempSensorOneWire', index=15, number=302,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SetpointSensorPair', index=16, number=303,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Pid', index=17, number=304,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActuatorAnalogMock', index=18, number=305,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActuatorPin', index=19, number=306,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActuatorPwm', index=20, number=307,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActuatorOffset', index=21, number=308,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Balancer', index=22, number=309,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Mutex', index=23, number=310,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SetpointProfile', index=24, number=311,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WiFiSettings', index=25, number=312,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TouchSettings', index=26, number=313,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DisplaySettings', index=27, number=314,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DS2413', index=28, number=315,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActuatorOneWire', index=29, number=316,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DS2408', index=30, number=317,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=255,
  serialized_end=891,
)
_sym_db.RegisterEnumDescriptor(_BREWBLOXOPTIONS_BLOCKTYPE)

_BREWBLOXOPTIONS_UNITTYPE = _descriptor.EnumDescriptor(
  name='UnitType',
  full_name='BrewbloxOptions.UnitType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NotSet', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Temp', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DeltaTemp', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DeltaTempPerTime', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Time', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='InverseTemp', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DeltaTempTime', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LongTime', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DeltaTempLongTime', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DeltaTempPerLongTime', index=9, number=9,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=894,
  serialized_end=1072,
)
_sym_db.RegisterEnumDescriptor(_BREWBLOXOPTIONS_UNITTYPE)


_BREWBLOXOPTIONS = _descriptor.Descriptor(
  name='BrewbloxOptions',
  full_name='BrewbloxOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unit', full_name='BrewbloxOptions.unit', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale', full_name='BrewbloxOptions.scale', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objtype', full_name='BrewbloxOptions.objtype', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hexed', full_name='BrewbloxOptions.hexed', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readonly', full_name='BrewbloxOptions.readonly', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logged', full_name='BrewbloxOptions.logged', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hexstr', full_name='BrewbloxOptions.hexstr', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='driven', full_name='BrewbloxOptions.driven', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BREWBLOXOPTIONS_BLOCKTYPE,
    _BREWBLOXOPTIONS_UNITTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=1072,
)

_BREWBLOXOPTIONS.fields_by_name['unit'].enum_type = _BREWBLOXOPTIONS_UNITTYPE
_BREWBLOXOPTIONS.fields_by_name['objtype'].enum_type = _BREWBLOXOPTIONS_BLOCKTYPE
_BREWBLOXOPTIONS_BLOCKTYPE.containing_type = _BREWBLOXOPTIONS
_BREWBLOXOPTIONS_UNITTYPE.containing_type = _BREWBLOXOPTIONS
DESCRIPTOR.message_types_by_name['BrewbloxOptions'] = _BREWBLOXOPTIONS
DESCRIPTOR.extensions_by_name['brewblox'] = brewblox
DESCRIPTOR.extensions_by_name['brewblox_msg'] = brewblox_msg
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BrewbloxOptions = _reflection.GeneratedProtocolMessageType('BrewbloxOptions', (_message.Message,), dict(
  DESCRIPTOR = _BREWBLOXOPTIONS,
  __module__ = 'brewblox_pb2'
  # @@protoc_insertion_point(class_scope:BrewbloxOptions)
  ))
_sym_db.RegisterMessage(BrewbloxOptions)

brewblox.message_type = _BREWBLOXOPTIONS
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(brewblox)
brewblox_msg.message_type = _BREWBLOXOPTIONS
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(brewblox_msg)

# @@protoc_insertion_point(module_scope)
