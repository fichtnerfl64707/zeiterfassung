class eintrag(): 
	
	def __init__(self, datum, kommen, gehen): 
		self.datum = datum
		self.kommen = kommen
		self.gehen = gehen
#		self.arbeitszeit = berechnen()

	def berechnen(self): 
		pause = 45
		
		kommen_h = self.kommen.split(':')[0]
		kommen_min = self.kommen.split(':')[1]

		gehen_h = self.gehen.split(':')[0]
		gehen_min = self.gehen.split(':')[1]

		arbeitszeit = (int(gehen_h)*60+int(gehen_min)) - pause - (int(kommen_h)*60+int(kommen_min))
		
		return arbeitszeit
