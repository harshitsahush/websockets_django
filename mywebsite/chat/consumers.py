import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    #reponsible for incoming messages from the client 
    #and broadcasting them to anybody that has a connection to this consumer in real time

    def connect(self):
        self.room_group_name = 'test'           #consider it room_id, from the url

        async_to_sync(self.channel_layer.group_add)(
            #will add user's channel to a group
            self.room_group_name,
            self.channel_name
        )


        #connect to client
        self.accept()

        #this will be sent to frontend to let the client know that connection successful
        """ self.send(text_data=json.dumps({
            'type' : 'connection_established',
            'message' : 'You are now connected!'
        })) """


    def receive(self, text_data):
        #receive message from the client
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        """ print("Message:", message)

        #send data to all the connected clients
        self.send(text_data = json.dumps({
            'type':'chat',
            'message' : message
        })) """

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type' : 'chat_message',            #this function will be responsible for broadcasting the message
                'message' : message
            }
        )

    def chat_message(self, event):
        #retrieve the message that was sent
        message = event['message']

        self.send(text_data = json.dumps({
            'type' : 'chat',
            'message' : message
        }))

    def disconnect(self, close_code):
        #what happens when the client disconnects
        pass