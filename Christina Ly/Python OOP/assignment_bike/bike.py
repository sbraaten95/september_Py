class Bike(object):
	def __init__(self, price, max_speed, miles):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles

	def displayinfo(self):
		print self.price
		print self.max_speed
		print self.miles

	def ride(self):
		print "Riding"
		self.miles +=10
		print self.miles

	def reverse(self):
		print "Reversing"
		self.miles -=5
		print self.miles

bmw = Bike('800','200', 3000)
honda = Bike('200','180', 1600)
triumph = Bike('1000', '250', 2000)


bmw.ride()
bmw.reverse()
bmw.displayinfo()
honda.ride()
honda.displayinfo()
triumph.displayinfo()




