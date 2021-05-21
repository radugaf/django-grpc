# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: blog_proto/post.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='blog_proto/post.proto',
  package='blog_proto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15\x62log_proto/post.proto\x12\nblog_proto\x1a\x1bgoogle/protobuf/empty.proto\"2\n\x04Post\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\"\x11\n\x0fPostListRequest\"!\n\x13PostRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x32\xa3\x02\n\x0ePostController\x12\x39\n\x04List\x12\x1b.blog_proto.PostListRequest\x1a\x10.blog_proto.Post\"\x00\x30\x01\x12.\n\x06\x43reate\x12\x10.blog_proto.Post\x1a\x10.blog_proto.Post\"\x00\x12?\n\x08Retrieve\x12\x1f.blog_proto.PostRetrieveRequest\x1a\x10.blog_proto.Post\"\x00\x12.\n\x06Update\x12\x10.blog_proto.Post\x1a\x10.blog_proto.Post\"\x00\x12\x35\n\x07\x44\x65stroy\x12\x10.blog_proto.Post\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_POST = _descriptor.Descriptor(
  name='Post',
  full_name='blog_proto.Post',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='blog_proto.Post.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='blog_proto.Post.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='blog_proto.Post.content', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=116,
)


_POSTLISTREQUEST = _descriptor.Descriptor(
  name='PostListRequest',
  full_name='blog_proto.PostListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=135,
)


_POSTRETRIEVEREQUEST = _descriptor.Descriptor(
  name='PostRetrieveRequest',
  full_name='blog_proto.PostRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='blog_proto.PostRetrieveRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=170,
)

DESCRIPTOR.message_types_by_name['Post'] = _POST
DESCRIPTOR.message_types_by_name['PostListRequest'] = _POSTLISTREQUEST
DESCRIPTOR.message_types_by_name['PostRetrieveRequest'] = _POSTRETRIEVEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Post = _reflection.GeneratedProtocolMessageType('Post', (_message.Message,), {
  'DESCRIPTOR' : _POST,
  '__module__' : 'blog_proto.post_pb2'
  # @@protoc_insertion_point(class_scope:blog_proto.Post)
  })
_sym_db.RegisterMessage(Post)

PostListRequest = _reflection.GeneratedProtocolMessageType('PostListRequest', (_message.Message,), {
  'DESCRIPTOR' : _POSTLISTREQUEST,
  '__module__' : 'blog_proto.post_pb2'
  # @@protoc_insertion_point(class_scope:blog_proto.PostListRequest)
  })
_sym_db.RegisterMessage(PostListRequest)

PostRetrieveRequest = _reflection.GeneratedProtocolMessageType('PostRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _POSTRETRIEVEREQUEST,
  '__module__' : 'blog_proto.post_pb2'
  # @@protoc_insertion_point(class_scope:blog_proto.PostRetrieveRequest)
  })
_sym_db.RegisterMessage(PostRetrieveRequest)



_POSTCONTROLLER = _descriptor.ServiceDescriptor(
  name='PostController',
  full_name='blog_proto.PostController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=173,
  serialized_end=464,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='blog_proto.PostController.List',
    index=0,
    containing_service=None,
    input_type=_POSTLISTREQUEST,
    output_type=_POST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='blog_proto.PostController.Create',
    index=1,
    containing_service=None,
    input_type=_POST,
    output_type=_POST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='blog_proto.PostController.Retrieve',
    index=2,
    containing_service=None,
    input_type=_POSTRETRIEVEREQUEST,
    output_type=_POST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='blog_proto.PostController.Update',
    index=3,
    containing_service=None,
    input_type=_POST,
    output_type=_POST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='blog_proto.PostController.Destroy',
    index=4,
    containing_service=None,
    input_type=_POST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_POSTCONTROLLER)

DESCRIPTOR.services_by_name['PostController'] = _POSTCONTROLLER

# @@protoc_insertion_point(module_scope)
