# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/internal/any_test.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/protobuf/internal/any_test.proto',
  package='google.protobuf.internal',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\'google/protobuf/internal/any_test.proto\x12\x18google.protobuf.internal\x1a\x19google/protobuf/any.proto\"\xc0\x01\n\x07TestAny\x12#\n\x05value\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x11\n\tint_value\x18\x02 \x01(\x05\x12\x42\n\tmap_value\x18\x03 \x03(\x0b\x32/.google.protobuf.internal.TestAny.MapValueEntry\x1a/\n\rMapValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01*\x08\x08\n\x10\x80\x80\x80\x80\x02\"\x85\x01\n\x11TestAnyExtension1\x12\t\n\x01i\x18\x0f \x01(\x05\x32\x65\n\nextension1\x12!.google.protobuf.internal.TestAny\x18\xab\xff\xf6. \x01(\x0b\x32+.google.protobuf.internal.TestAnyExtension1')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_TESTANY_MAPVALUEENTRY = _descriptor.Descriptor(
  name='MapValueEntry',
  full_name='google.protobuf.internal.TestAny.MapValueEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.protobuf.internal.TestAny.MapValueEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.protobuf.internal.TestAny.MapValueEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=232,
  serialized_end=279,
)

_TESTANY = _descriptor.Descriptor(
  name='TestAny',
  full_name='google.protobuf.internal.TestAny',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='google.protobuf.internal.TestAny.value', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int_value', full_name='google.protobuf.internal.TestAny.int_value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_value', full_name='google.protobuf.internal.TestAny.map_value', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TESTANY_MAPVALUEENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(10, 536870912), ],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=289,
)


_TESTANYEXTENSION1 = _descriptor.Descriptor(
  name='TestAnyExtension1',
  full_name='google.protobuf.internal.TestAnyExtension1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='i', full_name='google.protobuf.internal.TestAnyExtension1.i', index=0,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='extension1', full_name='google.protobuf.internal.TestAnyExtension1.extension1', index=0,
      number=98418603, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=292,
  serialized_end=425,
)

_TESTANY_MAPVALUEENTRY.containing_type = _TESTANY
_TESTANY.fields_by_name['value'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_TESTANY.fields_by_name['map_value'].message_type = _TESTANY_MAPVALUEENTRY
DESCRIPTOR.message_types_by_name['TestAny'] = _TESTANY
DESCRIPTOR.message_types_by_name['TestAnyExtension1'] = _TESTANYEXTENSION1
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestAny = _reflection.GeneratedProtocolMessageType('TestAny', (_message.Message,), dict(

  MapValueEntry = _reflection.GeneratedProtocolMessageType('MapValueEntry', (_message.Message,), dict(
    DESCRIPTOR = _TESTANY_MAPVALUEENTRY,
    __module__ = 'google.protobuf.internal.any_test_pb2'
    # @@protoc_insertion_point(class_scope:google.protobuf.internal.TestAny.MapValueEntry)
    ))
  ,
  DESCRIPTOR = _TESTANY,
  __module__ = 'google.protobuf.internal.any_test_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.internal.TestAny)
  ))
_sym_db.RegisterMessage(TestAny)
_sym_db.RegisterMessage(TestAny.MapValueEntry)

TestAnyExtension1 = _reflection.GeneratedProtocolMessageType('TestAnyExtension1', (_message.Message,), dict(
  DESCRIPTOR = _TESTANYEXTENSION1,
  __module__ = 'google.protobuf.internal.any_test_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.internal.TestAnyExtension1)
  ))
_sym_db.RegisterMessage(TestAnyExtension1)

_TESTANYEXTENSION1.extensions_by_name['extension1'].message_type = _TESTANYEXTENSION1
TestAny.RegisterExtension(_TESTANYEXTENSION1.extensions_by_name['extension1'])

_TESTANY_MAPVALUEENTRY._options = None
# @@protoc_insertion_point(module_scope)
