class Enemy:
	def __init__(self):
		raise NotImplementedError("Do not create raw Enemy objects.")

	def __str__(self):
		return self.name

	def is_alive(self):
		return self.hp > 0
		
	def handle_input(self, verb, noun1, noun2, inventory):
		return [False, None, inventory]
	
	def status(self):
		print("Enemy HP: "+self.hp)


class Invader(Enemy):## ground troop
	def __init__(self):
		self.name = "Invader"
		self.hp = 75
		self.damage = 15
		self.accuracy = 35
	def shoot(self):
		return random.randint(1,100)<=self.accuracy
	def hit(self):
		self.hp = self.hp-1
		
class Boss(Enemy):
        def __init__ (self):
                self.name = "Boss"
                self.hp = 10,000
                self.damage = 250##Subject to change
                self.accuracy = 100
        def shoot(self):
                return self.damage
class Invader(Enemy):## ground troop
	def __init__(self):
		self.name = "Epod"
		self.hp = 250
		self.damage = 15
		self.accuracy = 35
	def shoot(self):
		return random.randint(1,100)<=self.accuracy
	def hit(self):
		self.hp = self.hp-1

        

        
