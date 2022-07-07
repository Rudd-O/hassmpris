# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: mpris.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.protobuf.empty_pb2
from hassmpris.proto import mpris_pb2


class MPRISBase(abc.ABC):

    @abc.abstractmethod
    async def Ping(self, stream: 'grpclib.server.Stream[google.protobuf.empty_pb2.Empty, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def Updates(self, stream: 'grpclib.server.Stream[mpris_pb2.MPRISUpdateRequest, mpris_pb2.MPRISUpdateReply]') -> None:
        pass

    @abc.abstractmethod
    async def ChangePlayerStatus(self, stream: 'grpclib.server.Stream[mpris_pb2.ChangePlayerStatusRequest, mpris_pb2.ChangePlayerStatusReply]') -> None:
        pass

    @abc.abstractmethod
    async def PlayerNext(self, stream: 'grpclib.server.Stream[mpris_pb2.PlayerNextRequest, mpris_pb2.PlayerNextReply]') -> None:
        pass

    @abc.abstractmethod
    async def PlayerPrevious(self, stream: 'grpclib.server.Stream[mpris_pb2.PlayerPreviousRequest, mpris_pb2.PlayerPreviousReply]') -> None:
        pass

    @abc.abstractmethod
    async def Seek(self, stream: 'grpclib.server.Stream[mpris_pb2.SeekRequest, mpris_pb2.SeekReply]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/MPRIS.MPRIS/Ping': grpclib.const.Handler(
                self.Ping,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.protobuf.empty_pb2.Empty,
                google.protobuf.empty_pb2.Empty,
            ),
            '/MPRIS.MPRIS/Updates': grpclib.const.Handler(
                self.Updates,
                grpclib.const.Cardinality.UNARY_STREAM,
                mpris_pb2.MPRISUpdateRequest,
                mpris_pb2.MPRISUpdateReply,
            ),
            '/MPRIS.MPRIS/ChangePlayerStatus': grpclib.const.Handler(
                self.ChangePlayerStatus,
                grpclib.const.Cardinality.UNARY_UNARY,
                mpris_pb2.ChangePlayerStatusRequest,
                mpris_pb2.ChangePlayerStatusReply,
            ),
            '/MPRIS.MPRIS/PlayerNext': grpclib.const.Handler(
                self.PlayerNext,
                grpclib.const.Cardinality.UNARY_UNARY,
                mpris_pb2.PlayerNextRequest,
                mpris_pb2.PlayerNextReply,
            ),
            '/MPRIS.MPRIS/PlayerPrevious': grpclib.const.Handler(
                self.PlayerPrevious,
                grpclib.const.Cardinality.UNARY_UNARY,
                mpris_pb2.PlayerPreviousRequest,
                mpris_pb2.PlayerPreviousReply,
            ),
            '/MPRIS.MPRIS/Seek': grpclib.const.Handler(
                self.Seek,
                grpclib.const.Cardinality.UNARY_UNARY,
                mpris_pb2.SeekRequest,
                mpris_pb2.SeekReply,
            ),
        }


class MPRISStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Ping = grpclib.client.UnaryUnaryMethod(
            channel,
            '/MPRIS.MPRIS/Ping',
            google.protobuf.empty_pb2.Empty,
            google.protobuf.empty_pb2.Empty,
        )
        self.Updates = grpclib.client.UnaryStreamMethod(
            channel,
            '/MPRIS.MPRIS/Updates',
            mpris_pb2.MPRISUpdateRequest,
            mpris_pb2.MPRISUpdateReply,
        )
        self.ChangePlayerStatus = grpclib.client.UnaryUnaryMethod(
            channel,
            '/MPRIS.MPRIS/ChangePlayerStatus',
            mpris_pb2.ChangePlayerStatusRequest,
            mpris_pb2.ChangePlayerStatusReply,
        )
        self.PlayerNext = grpclib.client.UnaryUnaryMethod(
            channel,
            '/MPRIS.MPRIS/PlayerNext',
            mpris_pb2.PlayerNextRequest,
            mpris_pb2.PlayerNextReply,
        )
        self.PlayerPrevious = grpclib.client.UnaryUnaryMethod(
            channel,
            '/MPRIS.MPRIS/PlayerPrevious',
            mpris_pb2.PlayerPreviousRequest,
            mpris_pb2.PlayerPreviousReply,
        )
        self.Seek = grpclib.client.UnaryUnaryMethod(
            channel,
            '/MPRIS.MPRIS/Seek',
            mpris_pb2.SeekRequest,
            mpris_pb2.SeekReply,
        )
