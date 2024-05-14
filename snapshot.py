import csv
import redis
from pytoniq_core import Address

import config

client = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    username=config.REDIS_USERNAME,
    password=config.REDIS_PASSWORD,
)

keys = []

for key in client.scan_iter("coinbot_*+connection"):
    print(key)
    keys.append(key)

table = []
for key in keys:
    value = client.get(key)
    user_id = int(key.decode().split("_")[1].split("+")[0])
    value = value.decode() if value else None
    value = eval(value)
    if value is None:
        continue
    adress = Address(value["connect_event"]["payload"]["items"][0]["address"]).to_str(
        is_bounceable=False
    )
    points = client.get(f"coinbot_{user_id}+points")
    points = int(points.decode()) if points else 0
    table.append({"user_id": user_id, "adress": adress, "points": points})

with open("snapshot.csv", "w", newline="") as csvfile:
    fieldnames = ["user_id", "adress", "points"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in table:
        writer.writerow(row)
