import json
import telegram_bot as tbot
filename = 'db.txt'


def New_data(symbol="NONE", interval="NONE", resistance="NONE", support="NONE", stop="NONE"):
    coin_data = {f"{symbol}"f"{interval}": [{
        "resistance": f"{resistance}",
        "support": f"{support}",
        "stop": f"{stop}"}
    ]

    }

    getted_data = Get_data()
    getted_data.update(coin_data)
    Write_data(getted_data)


def Write_data(newData):
    with open(filename, "w") as f:
        f.write(json.dumps(newData, indent=4))


def Get_data():
    with open(filename, "r") as js:
        opened = json.loads(js.read())
        return opened
