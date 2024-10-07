import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    #reponsible for incoming messages from the client 
    #and broadcasting them to anybody that has a connection to this consumer in real time

    def connect(self):
        #connect to client
        self.accept()

        #this will be sent to frontend to let the client know that connection successful
        self.send(text_data=json.dumps({
            'type' : 'connection_established',
            'message' : 'You are now connected!'
        }))


    def receive(self, text_data):
        #receive message from the client
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        print("Message:", message)

        #send data to all the connected clients
        self.send(text_data = json.dumps({
            'type':'chat',
            'message' : message
        }))

    def disconnect(self, close_code):
        #what happens when the client disconnects
        pass