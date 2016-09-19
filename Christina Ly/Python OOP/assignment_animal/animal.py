class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100

	def walk(self):
		print "walking"
		self.health -=1
		print self.health
		return self

	def run(self):
		print "running"
		self.health -=5
		print self.health
		return self

	def displayHealth(self):
		print self.name
		print self.health
		return self

animal = Animal('animal')
animal.walk().walk().walk().run().run().displayHealth()

