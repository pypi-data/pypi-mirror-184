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
from cakework import cakework_pb2
from cakework import cakework_pb2_grpc
import json
import importlib
# import os
import time
import threading
import requests

class Cakework(cakework_pb2_grpc.CakeworkServicer):
    def __init__(self, user_activity, local=False):
        self.user_activity = user_activity
        self.local = local
        if self.local:
            self.frontend_url = "http://host.docker.internal:8080"
        else:
            self.frontend_url = "https://cakework-frontend.fly.dev"

    def RunActivity(self, request, context):
        print("local mode is: " + str(self.local))
        print("frontend url: " + self.frontend_url)
        print("got request")
        print(request)
        print("after printing request")
        # update to in progress
        response = requests.patch(f"{self.frontend_url}/update-status", json={"userId": request.userId, "app": request.app, "requestId": request.requestId, "status": "IN_PROGRESS"})
        print("updated status to IN_PROGRESS") # this may be a lie
        # TODO check the response
        parameters = json.loads(request.parameters)
        task = threading.Thread(target=self.background, args=[request.userId, request.app, request.requestId, parameters])
        task.daemon = True # Q: does returning kill the task?
        task.start()
        # what should we return? now, the client is no longer hitting the grpc server
        return cakework_pb2.Reply(result=json.dumps("worker started task")) # TODO this should return the request id

    # note: we need to get the request id in here as well
    def background(self, user_id, app, request_id, parameters):

        # print("starting background task with parameters: " + str(parameters))
        try:
            res = self.user_activity(**parameters)
            print("finished task")
            # TODO call the frontend api to update the status and result
            

            response = requests.patch(f"{self.frontend_url}/update-result", json={"userId": user_id, "app": app, "requestId": request_id, "result": json.dumps(res)})
            print("updated result")
            print(response)
            # TODO check the response
            response = requests.patch(f"{self.frontend_url}/update-status", json={"userId": user_id, "app": app, "requestId": request_id, "status": "SUCCEEDED"})
            print("updated status")
            print(response)

        except Exception as e:
            print("got an exception: ")
            print(e)
            response = requests.patch(f"{self.frontend_url}/update-result", json={"userId": user_id, "app": app, "requestId": request_id, "status": "FAILED"})

        # Q: who are we returning to here? instead of returning, we can just write this to the database. or emit a message and have the poller be in charge of writing to db
        return cakework_pb2.Reply(result=json.dumps(res))

def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1)) # what should the default be?
    cakework_pb2_grpc.add_CakeworkServicer_to_server(Cakework(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()

class ActivityServer:
    def __init__(self, user_activity, local=False):
        self.user_activity = user_activity
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=1)) # what should the default be?
        self.local = local

    def start(self):        
        port = '50051'
        cakework_pb2_grpc.add_CakeworkServicer_to_server(Cakework(self.user_activity, self.local), self.server)
        self.server.add_insecure_port('[::]:' + port)
        self.server.start()
        print("Server started, listening on " + port)
        self.server.wait_for_termination()
