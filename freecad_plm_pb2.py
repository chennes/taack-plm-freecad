# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: freecad_plm.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x66reecad_plm.proto\x12\x0bplm.freecad\"\xeb\x01\n\x07PlmFile\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x0c \x01(\t\x12\x10\n\x08\x66ileName\x18\x02 \x01(\t\x12\r\n\x05label\x18\x03 \x01(\t\x12\x16\n\x0elastModifiedBy\x18\x04 \x01(\t\x12\x18\n\x10lastModifiedDate\x18\x05 \x01(\t\x12\x0f\n\x07\x63omment\x18\x06 \x01(\t\x12\x0f\n\x07\x63ompany\x18\x07 \x01(\t\x12\x11\n\tcreatedBy\x18\x08 \x01(\t\x12\x13\n\x0b\x63reatedDate\x18\t \x01(\t\x12\x14\n\x0c\x65xternalLink\x18\n \x03(\t\x12\x13\n\x0b\x66ileContent\x18\x0b \x01(\x0c\"\xf1\x01\n\x07PlmLink\x12\x14\n\x0clinkedObject\x18\x01 \x01(\t\x12\x16\n\x0elinkClaimChild\x18\x02 \x01(\x08\x12\x15\n\rlinkTransform\x18\x03 \x01(\x08\x12\x43\n\x10linkCopyOnChange\x18\x04 \x01(\x0e\x32).plm.freecad.PlmLink.LinkCopyOnChangeEnum\x12\r\n\x05scale\x18\x05 \x01(\x01\x12\x0f\n\x07plmFile\x18\x06 \x01(\t\"<\n\x14LinkCopyOnChangeEnum\x12\x0c\n\x08\x44isabled\x10\x00\x12\x0b\n\x07\x45nabled\x10\x01\x12\t\n\x05Owned\x10\x02\"\xf7\x01\n\x06\x42ucket\x12\x33\n\x08plmFiles\x18\x01 \x03(\x0b\x32!.plm.freecad.Bucket.PlmFilesEntry\x12-\n\x05links\x18\x02 \x03(\x0b\x32\x1e.plm.freecad.Bucket.LinksEntry\x1a\x45\n\rPlmFilesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.plm.freecad.PlmFile:\x02\x38\x01\x1a\x42\n\nLinksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.plm.freecad.PlmLink:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'freecad_plm_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BUCKET_PLMFILESENTRY._options = None
  _BUCKET_PLMFILESENTRY._serialized_options = b'8\001'
  _BUCKET_LINKSENTRY._options = None
  _BUCKET_LINKSENTRY._serialized_options = b'8\001'
  _PLMFILE._serialized_start=35
  _PLMFILE._serialized_end=270
  _PLMLINK._serialized_start=273
  _PLMLINK._serialized_end=514
  _PLMLINK_LINKCOPYONCHANGEENUM._serialized_start=454
  _PLMLINK_LINKCOPYONCHANGEENUM._serialized_end=514
  _BUCKET._serialized_start=517
  _BUCKET._serialized_end=764
  _BUCKET_PLMFILESENTRY._serialized_start=627
  _BUCKET_PLMFILESENTRY._serialized_end=696
  _BUCKET_LINKSENTRY._serialized_start=698
  _BUCKET_LINKSENTRY._serialized_end=764
# @@protoc_insertion_point(module_scope)
