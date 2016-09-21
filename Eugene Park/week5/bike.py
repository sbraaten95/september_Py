class Bike(object):
	def __init__(self, price, max_speed, miles=0):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles
	def displayInfo(self):
		print 'Price: ', self.price
		print 'Max Speed: ', self.max_speed
		print 'Miles: ', self.miles
		return self
	def ride(self):
		print "Riding"
		self.miles += 10
		return self
	def reverse(self):
		print "Reversing"
		self.miles -= 5
		if self.miles < 0:
			self.miles = 0
		return self

bike1 = Bike(200, 30)
bike2 = Bike(1500, 15)
bike3 = Bike(1200, 40)
bike1.ride().ride().ride().reverse().displayInfo()
print
bike2.ride().ride().reverse().reverse().displayInfo()
print
bike3.reverse().reverse().reverse().displayInfo()