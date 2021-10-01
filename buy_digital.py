from iqoptionapi.stable_api import IQ_Option
import json



 #MODE: "PRACTICE"/"REAL"

class buy_digital_action():
	def __init__(self):
		self.time = 5
		#global duract
		#duract = 1
		with open("config/dates_config.json", "r") as file:
			self.read = json.loads(file.read())
			self.email = self.read['email']
			self.passwd = self.read['senha']
			self.account = self.read['account']
			file.close()
		with open('config/martin.json', 'r') as self.mart:
			self.read_m = json.loads(self.mart.read())
			self.martingale = self.read_m['mart']
			self.mart.close()

	def call_buy_dig(self ,active, money, acti, duract):					
		try:		
			self.iq = IQ_Option(self.email, self.passwd)
			self.status, self.ranson = self.iq.connect()
			if not self.status:
				print("Erro na conexão...")
				print("Tentando novamente...")
			if self.status:
				print("--> Conectado...")
				print("--> Realisando compra...")
				self.iq.change_balance(self.account)
				try:
					if self.martingale[0] == "-":
						self.money = float(self.martingale[1:]) * 2.3
						money = self.money
					else:
						pass
					self.iq_buy, self.id_buy = self.iq.buy_digital_spot(str(active), (money), str(acti), duract)
					self.status = self.iq_buy
					if self.status:
						while True:
							self.chack, self.win = self.iq.check_win_digital_v2(self.id_buy)
							if self.chack:
								break
						self.win = ('%0.2f' %self.win)
						if self.win[0] == '-':
							with open('config/martin.json', 'w') as mart:
								mart.write('{"mart": "'+str(self.win)+'"}')
								mart.close()
							print("Perdeu -->", self.win)
						else:
							with open('config/martin.json', 'w') as mart:
								mart.write('{"mart": "'+str(self.win)+'"}')
								mart.close()
							print("Ganhou -->", self.win)					
				except Exception as error:
					print("Erro na compra...")
		except Exception as error:
			print("Error --> ", error)


#bd = buy_digital_action()

#bd.call_buy_dig("EURUSD", 2, "put", 1)