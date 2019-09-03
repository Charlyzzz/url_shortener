import random
import channels.layers

import asyncio


async def reportView():
    channel_layer = channels.layers.get_channel_layer()
    while True:
        await channel_layer.group_send('chat_lobby', {'type': 'message', 'message': random.randint(1, 30)})
        await asyncio.sleep(random.randint(1, 5))


loop = asyncio.get_event_loop()
task = loop.create_task(reportView())
