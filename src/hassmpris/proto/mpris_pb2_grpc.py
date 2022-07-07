# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from hassmpris.proto import mpris_pb2 as mpris__pb2


class MPRISStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ping = channel.unary_unary(
                '/MPRIS.MPRIS/Ping',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Updates = channel.unary_stream(
                '/MPRIS.MPRIS/Updates',
                request_serializer=mpris__pb2.MPRISUpdateRequest.SerializeToString,
                response_deserializer=mpris__pb2.MPRISUpdateReply.FromString,
                )
        self.ChangePlayerStatus = channel.unary_unary(
                '/MPRIS.MPRIS/ChangePlayerStatus',
                request_serializer=mpris__pb2.ChangePlayerStatusRequest.SerializeToString,
                response_deserializer=mpris__pb2.ChangePlayerStatusReply.FromString,
                )
        self.Next = channel.unary_unary(
                '/MPRIS.MPRIS/Next',
                request_serializer=mpris__pb2.NextRequest.SerializeToString,
                response_deserializer=mpris__pb2.NextReply.FromString,
                )
        self.Previous = channel.unary_unary(
                '/MPRIS.MPRIS/Previous',
                request_serializer=mpris__pb2.PreviousRequest.SerializeToString,
                response_deserializer=mpris__pb2.PreviousReply.FromString,
                )
        self.Seek = channel.unary_unary(
                '/MPRIS.MPRIS/Seek',
                request_serializer=mpris__pb2.SeekRequest.SerializeToString,
                response_deserializer=mpris__pb2.SeekReply.FromString,
                )


class MPRISServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Updates(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangePlayerStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Next(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Previous(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Seek(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MPRISServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Updates': grpc.unary_stream_rpc_method_handler(
                    servicer.Updates,
                    request_deserializer=mpris__pb2.MPRISUpdateRequest.FromString,
                    response_serializer=mpris__pb2.MPRISUpdateReply.SerializeToString,
            ),
            'ChangePlayerStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.ChangePlayerStatus,
                    request_deserializer=mpris__pb2.ChangePlayerStatusRequest.FromString,
                    response_serializer=mpris__pb2.ChangePlayerStatusReply.SerializeToString,
            ),
            'Next': grpc.unary_unary_rpc_method_handler(
                    servicer.Next,
                    request_deserializer=mpris__pb2.NextRequest.FromString,
                    response_serializer=mpris__pb2.NextReply.SerializeToString,
            ),
            'Previous': grpc.unary_unary_rpc_method_handler(
                    servicer.Previous,
                    request_deserializer=mpris__pb2.PreviousRequest.FromString,
                    response_serializer=mpris__pb2.PreviousReply.SerializeToString,
            ),
            'Seek': grpc.unary_unary_rpc_method_handler(
                    servicer.Seek,
                    request_deserializer=mpris__pb2.SeekRequest.FromString,
                    response_serializer=mpris__pb2.SeekReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MPRIS.MPRIS', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MPRIS(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MPRIS.MPRIS/Ping',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Updates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/MPRIS.MPRIS/Updates',
            mpris__pb2.MPRISUpdateRequest.SerializeToString,
            mpris__pb2.MPRISUpdateReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChangePlayerStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MPRIS.MPRIS/ChangePlayerStatus',
            mpris__pb2.ChangePlayerStatusRequest.SerializeToString,
            mpris__pb2.ChangePlayerStatusReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Next(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MPRIS.MPRIS/Next',
            mpris__pb2.NextRequest.SerializeToString,
            mpris__pb2.NextReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Previous(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MPRIS.MPRIS/Previous',
            mpris__pb2.PreviousRequest.SerializeToString,
            mpris__pb2.PreviousReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Seek(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MPRIS.MPRIS/Seek',
            mpris__pb2.SeekRequest.SerializeToString,
            mpris__pb2.SeekReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
