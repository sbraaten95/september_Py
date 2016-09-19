from animal import Animal
class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.health = 150
	def pet(self):
		self.health += 5
		return self

class Dragon(Animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name)
		self.health = 170
	def displayHealth(self):
		print "this is a dragon"
		super(Dragon, self).displayHealth()
	def fly(self):
		self.health -= 10
		return self



dog = Dog('dog')
dog.walk().walk().walk().run().run().pet().displayHealth()
dragon = Dragon('dragon')
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()
