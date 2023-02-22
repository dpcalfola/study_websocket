import json
from channels.generic.websocket import WebsocketConsumer


# This is the consumer class that will handle the websocket connection
class ChatConsumer(WebsocketConsumer):

    def connect(self):
        """
        This method is called when the websocket is handshaking as part of initial connection.
        :return:
        """

        # This will accept the connection
        self.accept()
        # This will send a message back to the client
        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'You ar now connected!!',
        }))

    def receive(self, text_data=None, bytes_data=None):
        """
        This method is called when we get a text frame
        :param text_data: It would be received from the lobby.html String Data looks Like Json
        :param bytes_data:
        :return:
        """
        # Convert the text data to json
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Print the received message to the console
        print(message)
