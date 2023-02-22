import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


# This is the consumer class that will handle the websocket connection
class ChatConsumer(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_group_name = None

    def connect(self):
        """
        This method is called when the websocket is handshaking as part of initial connection
        :return:
        """

        # User grouping point
        self.room_group_name = 'group_name'

        # Now, All the user throw the same group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            # self.Channel_name => Automatically generated channel name for each user
            self.channel_name
        )
        # Accept the connection
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        """
        This method is called when we get a text data from the websocket
        :param self:
        :param text_data: Text data that we get from the websocket
                that received from the client's javascript
        :param bytes_data:
        :return:
        """

        # Convert the text data to json
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        # group_send() will send the message to all the users in the group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {
                'type': 'chat_message',
                'message': message,
            })

    # This will be called when we call the group_send method
    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message,
        }))
