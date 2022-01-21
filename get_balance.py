from iqoptionapi.stable_api import IQ_Option
import json 

file_json = "config/dates_config.json"


with open(file_json, 'r+') as file_json:
	json_loads = json.loads(file_json.read())
	email = json_loads['email']
	passw = json_loads['senha']

iq=IQ_Option(email, passw)

c, r = iq.connect()
balance_init = iq.get_balance()

def get_():
    dict = { "balance":  balance_init }
    with open("config/balance.json", "w+") as file:
        json.dump(dict, file)
        file.close()

def reader_balance():
    with open("config/balance.json", "r") as read_json:
        loads = json.loads(read_json.read())
        return loads['balance']
        


if balance_init < reader_balance():
    print("Conta negativa: ", balance_init - reader_balance())
elif balance_init > reader_balance():
    print("Conta positiva: ", balance_init - reader_balance())


print("Balanço da conta atual >> ", balance_init)
print("Balanço gravado na BD atual", reader_balance())