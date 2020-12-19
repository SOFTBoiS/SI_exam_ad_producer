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
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function
import logging

import grpc

from proto import emailservice_pb2, emailservice_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = emailservice_pb2_grpc.EmailServiceStub(channel)

    response = stub.SayHello(emailservice_pb2.HelloRequest(name='you'))
    print("Greeter client received: " + response.message)
    response = stub.SayHelloAgain(emailservice_pb2.HelloRequest(name='you'))
    print("Greeter client received: " + response.message)

    response = stub.GetFooBars(emailservice_pb2.HelloRequest(name="hello"))
    print("Greeter client received: " + str(response.bars[1]))

    for bar in response.bars:
        print(bar.i)
        print(bar.j)


def get_email(field="departure_airport", query_filter="CPH", message="test mails"):
    channel = grpc.insecure_channel('localhost:50051')
    stub = emailservice_pb2_grpc.EmailServiceStub(channel)
    response = stub.GetEmails(emailservice_pb2.Query(field=field, filter=query_filter))
    for email in response.emails:
        print(f'Sending email to "{email.mail_address}" with message: "Hi {email.name}! We have a special offer for  you.. {message}"')

    return len(response.emails)



if __name__ == '__main__':
    logging.basicConfig()
    run()
    get_email()