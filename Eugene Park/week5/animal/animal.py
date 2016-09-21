class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100
	def walk(self):
		self.health -=1
		return self
	def run(self):
		self.health -=5
		return self
	def displayHealth(self):
		print 'Health:',self.health
		return self

# animal = Animal('snake')
# animal.walk().walk().walk().run().run().displayHealth()