class Enemy:
	def __init__(self):
		raise NotImplementedError("Do not create raw Enemy objects.")

	def __str__(self):
		return self.name

	def is_alive(self):
		return self.hp > 0


class Invader(Enemy):
	def __init__(self):
		self.name = "Invader"
		self.hp = 75
		self.damage = 15
		self.accuracy = 35
