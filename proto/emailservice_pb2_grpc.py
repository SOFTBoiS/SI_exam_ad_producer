# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import proto.emailservice_pb2 as emailservice__pb2


class EmailServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetEmail = channel.unary_unary(
                '/emailservice.EmailService/GetEmail',
                request_serializer=emailservice__pb2.Query.SerializeToString,
                response_deserializer=emailservice__pb2.Email.FromString,
                )
        self.GetEmails = channel.unary_unary(
                '/emailservice.EmailService/GetEmails',
                request_serializer=emailservice__pb2.Query.SerializeToString,
                response_deserializer=emailservice__pb2.ListOfEmails.FromString,
                )


class EmailServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetEmail(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEmails(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EmailServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetEmail': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEmail,
                    request_deserializer=emailservice__pb2.Query.FromString,
                    response_serializer=emailservice__pb2.Email.SerializeToString,
            ),
            'GetEmails': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEmails,
                    request_deserializer=emailservice__pb2.Query.FromString,
                    response_serializer=emailservice__pb2.ListOfEmails.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'emailservice.EmailService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EmailService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetEmail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/emailservice.EmailService/GetEmail',
            emailservice__pb2.Query.SerializeToString,
            emailservice__pb2.Email.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEmails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/emailservice.EmailService/GetEmails',
            emailservice__pb2.Query.SerializeToString,
            emailservice__pb2.ListOfEmails.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
