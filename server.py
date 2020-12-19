# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc

from proto import emailservice_pb2, emailservice_pb2_grpc


class Greeter(emailservice_pb2_grpc.EmailServiceServicer):

    def SayHello(self, request, context):
        return emailservice_pb2.HelloReply(message='Hello, %s!' % request.name)

    def SayHelloAgain(self, request, context):
        return emailservice_pb2.HelloReply(message='Hello again, %s!' % request.name)

    def GetEmail(self, request, context):
        # DAO.GetEmail(request.field, request.filter)
        # SELECT email, name from Users where User.field = filter

        return emailservice_pb2.Email(mail_address="emil.valbak.hermansen@gmail.com", name="Emil Hermansen")

    def GetFooBars(self, request, context):
        foo = emailservice_pb2.Foo()
        foo.bars.add(i=12, j=13)
        foo.bars.add(i=12, j=13)
        foo.bars.add(i=12, j=13)
        foo.bars.add(i=12, j=13)
        foo.bars.add(i=12, j=13)
        foo.bars.add(i=12, j=13)

        return emailservice_pb2.Foo(bars=foo.bars)

    def GetEmails(self, request, context):
        # DAO.GetEmail(request.field, request.filter)
        # SELECT email, name from Users where User.field = filter

        list_of_emails = emailservice_pb2.ListOfEmails()
        list_of_emails.emails.add(mail_address="emil@gmail.com", name="emil")  # Adds a Bar then modify
        list_of_emails.emails.add(mail_address="sebbe@gmail.com", name="sebbe")  # Adds a Bar then modify

        return emailservice_pb2.ListOfEmails(emails=list_of_emails.emails)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    emailservice_pb2_grpc.add_EmailServiceServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
