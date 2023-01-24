def updload_file(file):
    transactions = []

    for data in file:
        type = data[:1].decode(encoding="utf-8", errors="strict")
        date = f"{data[1:5].decode('utf-8')}-{data[6:7].decode('utf-8')}-{data[8:9].decode('utf-8')}"
        value = data[9:19].decode(encoding="utf-8", errors="strict")
        cpf = data[19:30].decode(encoding="utf-8", errors="strict")
        card = data[30:42].decode(encoding="utf-8", errors="strict")
        hour = f"{data[42:44].decode('utf-8')}:{data[44:46].decode('utf-8')}:{data[46:48].decode('utf-8')}"
        owner = data[48:62].decode(encoding="utf-8", errors="strict")
        name = data[62:].decode(encoding="utf-8", errors="strict")

        obj = {
            "type": type,
            "date": date,
            "value": int(value) / 100,
            "cpf": cpf,
            "card": card,
            "hour": hour,
            "store_owner": owner,
            "store_name": name,
        }
        transactions.append(obj)

    return transactions
