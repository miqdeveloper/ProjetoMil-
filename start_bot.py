
from threading import Thread
from iqcapture import IQ_capture
from time import strftime

class main():
	def __init__(self):
		self.x_ = 0
		self.y_ = 0 
	def main_st(self):
		try:
			while self.x_ < 3:
				while strftime("%S") == '30':
					print("Round --> ", self.x_)
					self.iq_ = IQ_capture()
					self.iq_.IQconnect()
					self.x_+=1				
				#REseta martingale			
			with open('config/martin.json', 'w') as mart:
				mart.write('{"mart": "0"}')
				mart.close()				
		except Exception as error:
			print("Start.main_st -->", error)


for i in range(60):
	st = main()
	th = Thread(target=st.main_st(), daemon=True)
	th.start()	
	
	print("FIm da execução > ", i)

