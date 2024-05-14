from db import client
from dataclasses import dataclass

@dataclass
class Stats:
    connections: int
    subscribes: int
    points: int
    invited: int


async def get():
    # получаем число подключений
    keys = []
    async for key in client.scan_iter(match="coinbot_*+connection"):
        keys.append(key)
    connections = len(keys)

    # получаем число подписок
    keys = []
    async for key in client.scan_iter(match="coinbot_*+subscribe"):
        keys.append(key)
    subscribes = len(keys)

    # получаем сумму баллов
    keys = []
    async for key in client.scan_iter(match="coinbot_*+points"):
        keys.append(key)
    points = 0
    for key in keys:
        value = await client.get(key)
        points += int(value.decode())

    # получаем сумму invited
    keys = []
    async for key in client.scan_iter(match="coinbot_*+invited"):
        keys.append(key)
    invited = 0
    for key in keys:
        value = await client.get(key)
        invited += int(value.decode())

    return Stats(connections, subscribes, points, invited)