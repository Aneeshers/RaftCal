# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import chat_pb2 as chat__pb2


class ChatServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ChatStream = channel.unary_stream(
                '/grpc.ChatServer/ChatStream',
                request_serializer=chat__pb2.Account.SerializeToString,
                response_deserializer=chat__pb2.Str.FromString,
                )
        self.createAccount = channel.unary_unary(
                '/grpc.ChatServer/createAccount',
                request_serializer=chat__pb2.Account.SerializeToString,
                response_deserializer=chat__pb2.Account.FromString,
                )
        self.deleteAccount = channel.unary_unary(
                '/grpc.ChatServer/deleteAccount',
                request_serializer=chat__pb2.Account.SerializeToString,
                response_deserializer=chat__pb2.Str.FromString,
                )
        self.listAccounts = channel.unary_unary(
                '/grpc.ChatServer/listAccounts',
                request_serializer=chat__pb2.Empty.SerializeToString,
                response_deserializer=chat__pb2.Str.FromString,
                )
        self.login = channel.unary_unary(
                '/grpc.ChatServer/login',
                request_serializer=chat__pb2.Account.SerializeToString,
                response_deserializer=chat__pb2.Account.FromString,
                )
        self.sendNote = channel.unary_unary(
                '/grpc.ChatServer/sendNote',
                request_serializer=chat__pb2.Str.SerializeToString,
                response_deserializer=chat__pb2.Str.FromString,
                )
        self.dequeue = channel.unary_unary(
                '/grpc.ChatServer/dequeue',
                request_serializer=chat__pb2.Account.SerializeToString,
                response_deserializer=chat__pb2.Str.FromString,
                )


class ChatServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ChatStream(self, request, context):
        """This bi-directional stream makes it possible to send and receive Notes between 2 persons
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listAccounts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendNote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def dequeue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChatServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ChatStream': grpc.unary_stream_rpc_method_handler(
                    servicer.ChatStream,
                    request_deserializer=chat__pb2.Account.FromString,
                    response_serializer=chat__pb2.Str.SerializeToString,
            ),
            'createAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.createAccount,
                    request_deserializer=chat__pb2.Account.FromString,
                    response_serializer=chat__pb2.Account.SerializeToString,
            ),
            'deleteAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteAccount,
                    request_deserializer=chat__pb2.Account.FromString,
                    response_serializer=chat__pb2.Str.SerializeToString,
            ),
            'listAccounts': grpc.unary_unary_rpc_method_handler(
                    servicer.listAccounts,
                    request_deserializer=chat__pb2.Empty.FromString,
                    response_serializer=chat__pb2.Str.SerializeToString,
            ),
            'login': grpc.unary_unary_rpc_method_handler(
                    servicer.login,
                    request_deserializer=chat__pb2.Account.FromString,
                    response_serializer=chat__pb2.Account.SerializeToString,
            ),
            'sendNote': grpc.unary_unary_rpc_method_handler(
                    servicer.sendNote,
                    request_deserializer=chat__pb2.Str.FromString,
                    response_serializer=chat__pb2.Str.SerializeToString,
            ),
            'dequeue': grpc.unary_unary_rpc_method_handler(
                    servicer.dequeue,
                    request_deserializer=chat__pb2.Account.FromString,
                    response_serializer=chat__pb2.Str.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc.ChatServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ChatServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ChatStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpc.ChatServer/ChatStream',
            chat__pb2.Account.SerializeToString,
            chat__pb2.Str.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def createAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ChatServer/createAccount',
            chat__pb2.Account.SerializeToString,
            chat__pb2.Account.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ChatServer/deleteAccount',
            chat__pb2.Account.SerializeToString,
            chat__pb2.Str.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listAccounts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ChatServer/listAccounts',
            chat__pb2.Empty.SerializeToString,
            chat__pb2.Str.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ChatServer/login',
            chat__pb2.Account.SerializeToString,
            chat__pb2.Account.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sendNote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ChatServer/sendNote',
            chat__pb2.Str.SerializeToString,
            chat__pb2.Str.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def dequeue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ChatServer/dequeue',
            chat__pb2.Account.SerializeToString,
            chat__pb2.Str.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
