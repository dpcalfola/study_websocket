import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'You ar now connected!!',
        }))

    # def receive(self, text_data):
    #     pass
    #
    # def disconnect(self, close_code):
    #     pass
