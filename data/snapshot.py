import csv
from db import client
from pytoniq_core import Address


async def save():
    # получаем число подключений
    keys = []
    async for key in client.scan_iter(match="coinbot_*+connection"):
        keys.append(key)

    table = []
    for key in keys:
        value = await client.get(key)
        user_id = int(key.decode().split("_")[1].split("+")[0])
        value = value.decode() if value else None
        value = eval(value)
        if value is None:
            continue
        adress = Address(
            value["connect_event"]["payload"]["items"][0]["address"]
        ).to_str(is_bounceable=False)
        points = await client.get(f"coinbot_{user_id}+points")
        points = int(points.decode()) if points else 0
        table.append({"user_id": user_id, "adress": adress, "points": points})

    # сохраняем в csv
    with open("snapshot.csv", "w", newline="") as csvfile:
        fieldnames = ["user_id", "adress", "points"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in table:
            writer.writerow(row)
