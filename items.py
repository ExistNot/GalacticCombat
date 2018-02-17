class Weapon:
	def __init__(self):
		raise NotImplementedError("Do not create raw Weapon objects.")

	def __str__(self):
		return self.name


class PBlaster(Weapon):
	def __init__(self):
		self.name = "Blaster"
		self.description = "A Hand held gun used by the cadets and pilots of the space program."
		self.damage = 25
