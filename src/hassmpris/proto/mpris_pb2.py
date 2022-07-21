# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mpris.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bmpris.proto\x12\x05MPRIS\x1a\x1bgoogle/protobuf/empty.proto\"\x14\n\x12MPRISUpdateRequest\"\xeb\x02\n\x15MPRISPlayerProperties\x12\x17\n\nCanControl\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x15\n\x08\x43\x61nPause\x18\x02 \x01(\x08H\x01\x88\x01\x01\x12\x14\n\x07\x43\x61nPlay\x18\x03 \x01(\x08H\x02\x88\x01\x01\x12\x14\n\x07\x43\x61nSeek\x18\x04 \x01(\x08H\x03\x88\x01\x01\x12\x16\n\tCanGoNext\x18\x05 \x01(\x08H\x04\x88\x01\x01\x12\x1a\n\rCanGoPrevious\x18\x06 \x01(\x08H\x05\x88\x01\x01\x12\x11\n\x04Rate\x18\x07 \x01(\x01H\x06\x88\x01\x01\x12\x18\n\x0bMinimumRate\x18\x08 \x01(\x01H\x07\x88\x01\x01\x12\x18\n\x0bMaximumRate\x18\t \x01(\x01H\x08\x88\x01\x01\x42\r\n\x0b_CanControlB\x0b\n\t_CanPauseB\n\n\x08_CanPlayB\n\n\x08_CanSeekB\x0c\n\n_CanGoNextB\x10\n\x0e_CanGoPreviousB\x07\n\x05_RateB\x0e\n\x0c_MinimumRateB\x0e\n\x0c_MaximumRate\"\x16\n\x14MPRISUpdateHeartbeat\"%\n\x11MPRISPlayerSeeked\x12\x10\n\x08position\x18\x01 \x01(\x02\"\xbe\x01\n\x11MPRISPlayerUpdate\x12\x11\n\tplayer_id\x18\x01 \x01(\t\x12#\n\x06status\x18\x02 \x01(\x0e\x32\x13.MPRIS.PlayerStatus\x12\x15\n\rjson_metadata\x18\x03 \x01(\t\x12\x30\n\nproperties\x18\x04 \x01(\x0b\x32\x1c.MPRIS.MPRISPlayerProperties\x12(\n\x06seeked\x18\x05 \x01(\x0b\x32\x18.MPRIS.MPRISPlayerSeeked\"l\n\x10MPRISUpdateReply\x12.\n\theartbeat\x18\x01 \x01(\x0b\x32\x1b.MPRIS.MPRISUpdateHeartbeat\x12(\n\x06player\x18\x02 \x01(\x0b\x32\x18.MPRIS.MPRISPlayerUpdate\"\xb6\x01\n\x19\x43hangePlayerStatusRequest\x12\x11\n\tplayer_id\x18\x01 \x01(\t\x12?\n\x06status\x18\x02 \x01(\x0e\x32/.MPRIS.ChangePlayerStatusRequest.PlaybackStatus\"E\n\x0ePlaybackStatus\x12\r\n\tUNCHANGED\x10\x00\x12\x0b\n\x07PLAYING\x10\x01\x12\n\n\x06PAUSED\x10\x02\x12\x0b\n\x07STOPPED\x10\x03\"0\n\x0bSeekRequest\x12\x11\n\tplayer_id\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x02\"\x0b\n\tSeekReply\"K\n\x12SetPositionRequest\x12\x11\n\tplayer_id\x18\x01 \x01(\t\x12\x10\n\x08track_id\x18\x02 \x01(\t\x12\x10\n\x08position\x18\x03 \x01(\x02\"\x12\n\x10SetPositionReply\"\x19\n\x17\x43hangePlayerStatusReply\" \n\x0bNextRequest\x12\x11\n\tplayer_id\x18\x01 \x01(\t\"\x0b\n\tNextReply\"$\n\x0fPreviousRequest\x12\x11\n\tplayer_id\x18\x01 \x01(\t\"\x0f\n\rPreviousReply*Y\n\x0cPlayerStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04GONE\x10\x01\x12\x0c\n\x08\x41PPEARED\x10\x02\x12\x0b\n\x07PLAYING\x10\x03\x12\n\n\x06PAUSED\x10\x04\x12\x0b\n\x07STOPPED\x10\x05\x32\xbf\x03\n\x05MPRIS\x12\x38\n\x04Ping\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x12\x41\n\x07Updates\x12\x19.MPRIS.MPRISUpdateRequest\x1a\x17.MPRIS.MPRISUpdateReply\"\x00\x30\x01\x12X\n\x12\x43hangePlayerStatus\x12 .MPRIS.ChangePlayerStatusRequest\x1a\x1e.MPRIS.ChangePlayerStatusReply\"\x00\x12.\n\x04Next\x12\x12.MPRIS.NextRequest\x1a\x10.MPRIS.NextReply\"\x00\x12:\n\x08Previous\x12\x16.MPRIS.PreviousRequest\x1a\x14.MPRIS.PreviousReply\"\x00\x12.\n\x04Seek\x12\x12.MPRIS.SeekRequest\x1a\x10.MPRIS.SeekReply\"\x00\x12\x43\n\x0bSetPosition\x12\x19.MPRIS.SetPositionRequest\x1a\x17.MPRIS.SetPositionReply\"\x00\x62\x06proto3')

_PLAYERSTATUS = DESCRIPTOR.enum_types_by_name['PlayerStatus']
PlayerStatus = enum_type_wrapper.EnumTypeWrapper(_PLAYERSTATUS)
UNKNOWN = 0
GONE = 1
APPEARED = 2
PLAYING = 3
PAUSED = 4
STOPPED = 5


_MPRISUPDATEREQUEST = DESCRIPTOR.message_types_by_name['MPRISUpdateRequest']
_MPRISPLAYERPROPERTIES = DESCRIPTOR.message_types_by_name['MPRISPlayerProperties']
_MPRISUPDATEHEARTBEAT = DESCRIPTOR.message_types_by_name['MPRISUpdateHeartbeat']
_MPRISPLAYERSEEKED = DESCRIPTOR.message_types_by_name['MPRISPlayerSeeked']
_MPRISPLAYERUPDATE = DESCRIPTOR.message_types_by_name['MPRISPlayerUpdate']
_MPRISUPDATEREPLY = DESCRIPTOR.message_types_by_name['MPRISUpdateReply']
_CHANGEPLAYERSTATUSREQUEST = DESCRIPTOR.message_types_by_name['ChangePlayerStatusRequest']
_SEEKREQUEST = DESCRIPTOR.message_types_by_name['SeekRequest']
_SEEKREPLY = DESCRIPTOR.message_types_by_name['SeekReply']
_SETPOSITIONREQUEST = DESCRIPTOR.message_types_by_name['SetPositionRequest']
_SETPOSITIONREPLY = DESCRIPTOR.message_types_by_name['SetPositionReply']
_CHANGEPLAYERSTATUSREPLY = DESCRIPTOR.message_types_by_name['ChangePlayerStatusReply']
_NEXTREQUEST = DESCRIPTOR.message_types_by_name['NextRequest']
_NEXTREPLY = DESCRIPTOR.message_types_by_name['NextReply']
_PREVIOUSREQUEST = DESCRIPTOR.message_types_by_name['PreviousRequest']
_PREVIOUSREPLY = DESCRIPTOR.message_types_by_name['PreviousReply']
_CHANGEPLAYERSTATUSREQUEST_PLAYBACKSTATUS = _CHANGEPLAYERSTATUSREQUEST.enum_types_by_name['PlaybackStatus']
MPRISUpdateRequest = _reflection.GeneratedProtocolMessageType('MPRISUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _MPRISUPDATEREQUEST,
  '__module__' : 'mpris_pb2'
  # @@protoc_insertion_point(class_scope:MPRIS.MPRISUpdateRequest)
  })
_sym_db.RegisterMessage(MPRISUpdateRequest)

MPRISPlayerProperties = _reflection.GeneratedProtocolMessageType('MPRISPlayerProperties', (_message.Message,), {
  'DESCRIPTOR' : _MPRISPLAYERPROPERTIES,
  '__module__' : 'mpris_pb2'
  # @@protoc_insertion_point(class_scope:MPRIS.MPRISPlayerProperties)
  })
_sym_db.RegisterMessage(MPRISPlayerProperties)

MPRISUpdateHeartbeat = _reflection.GeneratedProtocolMessageType('MPRISUpdateHeartbeat', (_message.Message,), {
  'DESCRIPTOR' : _MPRISUPDATEHEARTBEAT,
  '__module__' : 'mpris_pb2'
  # @@protoc_insertion_point(class_scope:MPRIS.MPRISUpdateHeartbeat)
  })
_sym_db.RegisterMessage(MPRISUpdateHeartbeat)

MPRISPlayerSeeked = _reflection.GeneratedProtocolMessageType('MPRISPlayerSeeked', (_message.Message,), {
  'DESCRIPTOR' : _MPRISPLAYERSEEKED,
  '__module__' : 'mpris_pb2'
  # @@protoc_insertion_point(class_scope:MPRIS.MPRISPlayerSeeked)
  })
_sym_db.RegisterMessage(MPRISPlayerSeeked)

MPRISPlayerUpdate = _reflection.GeneratedProtocolMessageType('MPRISPlayerUpdate', (_message.Message,), {
  'DESCRIPTOR' : _MPRISPLAYERUPDATE,
  '__module__' : 'mpris_pb2'
  # @@protoc_insertion_point(class_scope:MPRIS.MPRISPlayerUpdate)
  })
_sym_db.RegisterMessage(MPRISPlayerUpdate)

MPRISUpdateReply = _reflection.GeneratedProtocolMessageType('MPRISUpdateReply', (_message.Message,), {
  'DESCRIPTOR' : _MPRISUPDATEREPLY,
  '__module__' : 'mpris_pb2'
  # @@protoc_insertion_point(class_scope:MPRIS.MPRISUpdateReply)
  })
_sym_db.RegisterMessage(MPRISUpdateReply)

ChangePlayerStatusRequest = _reflection.GeneratedProtocolMessageType('ChangePlayerStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHANGEPLAYERSTATUSREQUEST,
  '__module__' : 'mpris_pb2'
  # @@protoc_insertion_point(class_scope:MPRIS.ChangePlayerStatusRequest)
  })
_sym_db.RegisterMessage(ChangePlayerStatusRequest)

SeekRequest = _reflection.GeneratedProtocolMessageType('SeekRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEEKREQUEST,
  '__module__' : 'mpris_pb2'
  # @@protoc_insertion_point(class_scope:MPRIS.SeekRequest)
  })
_sym_db.RegisterMessage(SeekRequest)

SeekReply = _reflection.GeneratedProtocolMessageType('SeekReply', (_message.Message,), {
  'DESCRIPTOR' : _SEEKREPLY,
  '__module__' : 'mpris_pb2'
  # @@protoc_insertion_point(class_scope:MPRIS.SeekReply)
  })
_sym_db.RegisterMessage(SeekReply)

SetPositionRequest = _reflection.GeneratedProtocolMessageType('SetPositionRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETPOSITIONREQUEST,
  '__module__' : 'mpris_pb2'
  # @@protoc_insertion_point(class_scope:MPRIS.SetPositionRequest)
  })
_sym_db.RegisterMessage(SetPositionRequest)

SetPositionReply = _reflection.GeneratedProtocolMessageType('SetPositionReply', (_message.Message,), {
  'DESCRIPTOR' : _SETPOSITIONREPLY,
  '__module__' : 'mpris_pb2'
  # @@protoc_insertion_point(class_scope:MPRIS.SetPositionReply)
  })
_sym_db.RegisterMessage(SetPositionReply)

ChangePlayerStatusReply = _reflection.GeneratedProtocolMessageType('ChangePlayerStatusReply', (_message.Message,), {
  'DESCRIPTOR' : _CHANGEPLAYERSTATUSREPLY,
  '__module__' : 'mpris_pb2'
  # @@protoc_insertion_point(class_scope:MPRIS.ChangePlayerStatusReply)
  })
_sym_db.RegisterMessage(ChangePlayerStatusReply)

NextRequest = _reflection.GeneratedProtocolMessageType('NextRequest', (_message.Message,), {
  'DESCRIPTOR' : _NEXTREQUEST,
  '__module__' : 'mpris_pb2'
  # @@protoc_insertion_point(class_scope:MPRIS.NextRequest)
  })
_sym_db.RegisterMessage(NextRequest)

NextReply = _reflection.GeneratedProtocolMessageType('NextReply', (_message.Message,), {
  'DESCRIPTOR' : _NEXTREPLY,
  '__module__' : 'mpris_pb2'
  # @@protoc_insertion_point(class_scope:MPRIS.NextReply)
  })
_sym_db.RegisterMessage(NextReply)

PreviousRequest = _reflection.GeneratedProtocolMessageType('PreviousRequest', (_message.Message,), {
  'DESCRIPTOR' : _PREVIOUSREQUEST,
  '__module__' : 'mpris_pb2'
  # @@protoc_insertion_point(class_scope:MPRIS.PreviousRequest)
  })
_sym_db.RegisterMessage(PreviousRequest)

PreviousReply = _reflection.GeneratedProtocolMessageType('PreviousReply', (_message.Message,), {
  'DESCRIPTOR' : _PREVIOUSREPLY,
  '__module__' : 'mpris_pb2'
  # @@protoc_insertion_point(class_scope:MPRIS.PreviousReply)
  })
_sym_db.RegisterMessage(PreviousReply)

_MPRIS = DESCRIPTOR.services_by_name['MPRIS']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLAYERSTATUS._serialized_start=1279
  _PLAYERSTATUS._serialized_end=1368
  _MPRISUPDATEREQUEST._serialized_start=51
  _MPRISUPDATEREQUEST._serialized_end=71
  _MPRISPLAYERPROPERTIES._serialized_start=74
  _MPRISPLAYERPROPERTIES._serialized_end=437
  _MPRISUPDATEHEARTBEAT._serialized_start=439
  _MPRISUPDATEHEARTBEAT._serialized_end=461
  _MPRISPLAYERSEEKED._serialized_start=463
  _MPRISPLAYERSEEKED._serialized_end=500
  _MPRISPLAYERUPDATE._serialized_start=503
  _MPRISPLAYERUPDATE._serialized_end=693
  _MPRISUPDATEREPLY._serialized_start=695
  _MPRISUPDATEREPLY._serialized_end=803
  _CHANGEPLAYERSTATUSREQUEST._serialized_start=806
  _CHANGEPLAYERSTATUSREQUEST._serialized_end=988
  _CHANGEPLAYERSTATUSREQUEST_PLAYBACKSTATUS._serialized_start=919
  _CHANGEPLAYERSTATUSREQUEST_PLAYBACKSTATUS._serialized_end=988
  _SEEKREQUEST._serialized_start=990
  _SEEKREQUEST._serialized_end=1038
  _SEEKREPLY._serialized_start=1040
  _SEEKREPLY._serialized_end=1051
  _SETPOSITIONREQUEST._serialized_start=1053
  _SETPOSITIONREQUEST._serialized_end=1128
  _SETPOSITIONREPLY._serialized_start=1130
  _SETPOSITIONREPLY._serialized_end=1148
  _CHANGEPLAYERSTATUSREPLY._serialized_start=1150
  _CHANGEPLAYERSTATUSREPLY._serialized_end=1175
  _NEXTREQUEST._serialized_start=1177
  _NEXTREQUEST._serialized_end=1209
  _NEXTREPLY._serialized_start=1211
  _NEXTREPLY._serialized_end=1222
  _PREVIOUSREQUEST._serialized_start=1224
  _PREVIOUSREQUEST._serialized_end=1260
  _PREVIOUSREPLY._serialized_start=1262
  _PREVIOUSREPLY._serialized_end=1277
  _MPRIS._serialized_start=1371
  _MPRIS._serialized_end=1818
# @@protoc_insertion_point(module_scope)
