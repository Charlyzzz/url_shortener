import random
import asyncio

import channels

from url_shortener.models.channel_tracker import ChannelTracker


async def report_view():
    tracker = ChannelTracker()

    channel_layer = channels.layers.get_channel_layer()
    views = 0
    while True:
        views += random.randint(1, 30)
        payload = {
            'type': 'message',
            'message': {
                'viewCount': views
            }
        }
        await channel_layer.group_send('lobby', payload)
        await asyncio.sleep(random.randint(1, 5))


loop = asyncio.get_event_loop()
task = loop.create_task(report_view())
