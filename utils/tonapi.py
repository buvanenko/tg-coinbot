import aiohttp

from pytoniq_core import Address

from utils.decimals import to_float
import config

async def jetton_balance(address: str, contract: str = config.JETTON) -> float:
    url = f"https://tonapi.io/v2/accounts/{address}/jettons"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
    
    contract = Address(contract).to_str(is_user_friendly=False)

    for balance_item in data['balances']:
        print(balance_item)
        if balance_item['jetton']['address'] == contract:
            balance = to_float(balance_item['balance'])
            return balance
    return 0.0