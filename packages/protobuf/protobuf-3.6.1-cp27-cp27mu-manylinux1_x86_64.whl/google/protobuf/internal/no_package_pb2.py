# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/internal/no_package.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/protobuf/internal/no_package.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n)google/protobuf/internal/no_package.proto\";\n\x10NoPackageMessage\x12\'\n\x0fno_package_enum\x18\x01 \x01(\x0e\x32\x0e.NoPackageEnum*?\n\rNoPackageEnum\x12\x16\n\x12NO_PACKAGE_VALUE_0\x10\x00\x12\x16\n\x12NO_PACKAGE_VALUE_1\x10\x01')
)

_NOPACKAGEENUM = _descriptor.EnumDescriptor(
  name='NoPackageEnum',
  full_name='NoPackageEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_PACKAGE_VALUE_0', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_PACKAGE_VALUE_1', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=106,
  serialized_end=169,
)
_sym_db.RegisterEnumDescriptor(_NOPACKAGEENUM)

NoPackageEnum = enum_type_wrapper.EnumTypeWrapper(_NOPACKAGEENUM)
NO_PACKAGE_VALUE_0 = 0
NO_PACKAGE_VALUE_1 = 1



_NOPACKAGEMESSAGE = _descriptor.Descriptor(
  name='NoPackageMessage',
  full_name='NoPackageMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='no_package_enum', full_name='NoPackageMessage.no_package_enum', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=104,
)

_NOPACKAGEMESSAGE.fields_by_name['no_package_enum'].enum_type = _NOPACKAGEENUM
DESCRIPTOR.message_types_by_name['NoPackageMessage'] = _NOPACKAGEMESSAGE
DESCRIPTOR.enum_types_by_name['NoPackageEnum'] = _NOPACKAGEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NoPackageMessage = _reflection.GeneratedProtocolMessageType('NoPackageMessage', (_message.Message,), dict(
  DESCRIPTOR = _NOPACKAGEMESSAGE,
  __module__ = 'google.protobuf.internal.no_package_pb2'
  # @@protoc_insertion_point(class_scope:NoPackageMessage)
  ))
_sym_db.RegisterMessage(NoPackageMessage)


# @@protoc_insertion_point(module_scope)
