from animal import Animal
class Dog(Animal):
	def __init__(self, name):
		super(Dog,self).__init__(name)
		self.health = 150
	def pet(self):
		self.health += 5
		return self

class Dragon(Animal):
	def __init__(self, name):
		super(Dragon,self).__init__(name)
		self.health = 170
	def fly(self):
		self.health -= 10
		return self
	def displayHealth(self):
		print 'this is a dragon!'
		super(Dragon,self).displayHealth()

dog1 = Dog('yes_this_is_a_dog')
drag1 = Dragon("Ima_dragon")
dog1.walk().walk().walk().run().run().pet().displayHealth()
drag1.walk().walk().walk().run().run().fly().fly().displayHealth()