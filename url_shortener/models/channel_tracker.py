import channels.layers
from asgiref.sync import async_to_sync


class ChannelTracker:
    def __init__(self):
        self.channel_layer = channels.layers.get_channel_layer()

    def update_metrics(self, link):
        self.push(link.slug, link.view_count)

    def push(self, name, view_count):
        payload = {
            'type': 'message',
            'message': {
                'viewCount': view_count
            }
        }
        async_to_sync(self.channel_layer.group_send)(name, payload)
