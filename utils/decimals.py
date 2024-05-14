def to_float(balance: str) -> float:
    balance = f"{balance[:-9]}.{balance[-9:]}"
    if balance.startswith("."):
        balance = "0" + balance
    return float(balance)


def to_decimal_str(balance: float) -> str:
    balance = str(balance)
    if "." in balance:
        balance = balance.replace(".", "")
    else:
        balance += "000000000"
    return balance
