import items

name = input("What is your name kid? ")

class Player:
	def __str__(self):
		self.name = name
		return """Ha, welcome to the Space Training Program. Oh, you forgot your name? 
It's """ + self.name + """."""
	def __init__(self):
		#self.inventory = [items.Rock(),				#EDIT THE INVENTORY AFTER ALL STATS FOR PLAYER ARE ADDED
						#items.Dagger(),				#EDIT THE INVENTORY AFTER ALL STATS FOR PLAYER ARE ADDED
						#'Gold(5)',					#EDIT THE INVENTORY AFTER ALL STATS FOR PLAYER ARE ADDED
						#'Crusty Bread']				#EDIT THE INVENTORY AFTER ALL STATS FOR PLAYER ARE ADDED
		self.health	= 100
		self.ammo = 10
		self.shields = 50
		self.accuracy = 75			#<40 is garbage,   around 50 is okay,    >60 is great
		self.damage = 50
		self.reloadtime = 2
		self.x = 1   					#will change to start on the ship later
		self.y = 2
	def reload(self):
		if self.ammo == 0:
			time.sleep(reloadtime)
			self.ammo = 10

	def print_inventory(self):
		print("Inventory:")
		for item in self.inventory:
			print('* ' + str(item))
			
	def move(self, dx, dy):
		self.x += dx
		self.y += dy

	def move_north(self):
		self.move(dx=0, dy=-1)

	def move_south(self):
		self.move(dx=0, dy=1)

	def move_east(self):
		self.move(dx=1, dy=0)

	def move_west(self):
		self.move(dx=-1, dy=0)
	def shoot(self):
		self.ammo = self.ammo - 1
def myself():
	print(Player())
	
myself()

