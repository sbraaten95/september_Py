class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage

	def display_all(self):
		print "Price:", self.price
		print "Speed:", self.speed, "mph"
		print "Fuel:", self.fuel 
		print "Mileage:", self.mileage, "mpg"
		if self.price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
		print self.tax

honda = Car(2000, 50, 'Full', 15)
acura = Car(26000, 75, 'Not Full', 16)
audi = Car(4000, 60, 'Full', 14)
lexus = Car(55000, 40, 'Full', 18)
mercedes = Car(60000, 35, 'Not Full', 18)
porsche = Car(8000, 80, 'Full', 12 )
# honda.display_all()
# lexus.display_all()