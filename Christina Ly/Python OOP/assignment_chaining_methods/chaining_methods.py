class Bike(object):
	def __init__(self, price, max_speed, miles):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles

	def displayinfo(self):
		print self.price
		print self.max_speed
		print self.miles
		return self

	def ride(self):
		print "Riding"
		self.miles +=10
		print self.miles
		return self

	def reverse(self):
		print "Reversing"
		self.miles -=5
		print self.miles
		return self

bmw = Bike('800','200', 3000)
honda = Bike('200','180', 1600)
triumph = Bike('1000', '250', 2000)


bmw.ride().ride().displayinfo().reverse().reverse().displayinfo()
# bmw.reverse()
# bmw.displayinfo()
# honda.ride()
# honda.displayinfo()
# triumph.displayinfo()




