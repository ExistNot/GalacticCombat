import items

class Player:
	def __str__(self):
		self.name = name
		return """Ha, welcome to the Space Training Program. Oh, you forgot your name? 
It's """ + self.name + """."""
	def __init__(self):
		self.inventory = [items.PBlaster(), items.Sparkling_Gem(),items.Hammer(),items.Nail(),items.Cortex(),items.FusionCannon()]##CHAGNE THIS
		self.hp	= 100
		self.gold = 0
		self.ammo = 10
		self.shields = 50
		self.accuracy = 75			#<40 is garbage,   around 50 is okay,    >60 is great
		self.reloadtime = 2
		self.x = 3  					##CHange this
		self.y = 7
		self.damage = items.PBlaster.damage
		self.ship = PlayerShip()
		self.removeShipitems = False
		self.weapon = None
	def is_alive(self):
		if(self.hp <= 0):
			return False
		else:
			return True

	def reload(self):
		if self.ammo == 0:
			time.sleep(reloadtime)
			self.ammo = 10

	def print_inventory(self):
		print("Inventory:")
		best_weapon = None
		equipped_weapon = False
		for item in self.inventory:
			inventory_text = '* ' + str(item).title()
			if(item == self.weapon and not equipped_weapon):
				inventory_text += ' (equipped)'
				equipped_weapon = True
			print(inventory_text)
			best_weapon = self.most_powerful_weapon()
		print("* %i Gold" % self.gold)
		if(best_weapon):
			print("Your best weapon is your {}.".format(best_weapon))
		else:
			print("You are not carrying any weapons.")
	
	def most_powerful_weapon(self):
		max_damage = 0
		best_weapon = None
		for item in self.inventory:
			try:
				if item.damage > max_damage:
					best_weapon = item
					max_damage = item.damage
			except AttributeError:
				pass
		return best_weapon
	def move(self, dx, dy):
		self.x += dx
		self.y += dy
		#Remove the hammer nail, cortex and fusion cannon if the player "has" the ship"
		if(not self.removeShipitems):
			responce = self.getinShip()
			if(self.removeShipitems):
				for index in range(len(self.inventory)):
					if(self.inventory[index].name.lower() == "hammer" and self.inventory[index].name.lower() == "nail" and self.inventory[index].name.lower() == "cortex" and self.inventory[index].name.lower() == "fusion cannon"):
						self.inventory.pop(index)
				print(responce)
			else:
				if(responce):
					print (responce)
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
		if(random.randint(1,100)<=self.accuracy):
			self.ammo = self.ammo - 1
			print("You hit the Enemy!")
		else:
			print("You missed the enemy")
	def status(self):
		print("HP = "  + self.health +" Ammo = " + self.ammo )
		
	def handle_input(self, verb, noun1, noun2):
		if(verb == 'check'):
			for item in self.inventory:
				if item.name.lower() == noun1:
					return [True, item.check_text()]
		return [False, ""]
		
	def update_inventory(self):
		#Remove the hammer nail, cortex and fusion cannon if the player "has" the ship"
		#if(not self.removeShipitems):
		#	responce = self.getinShip()
		#	if(self.removeShipitems):
		#		for index in range(len(self.inventory)):
		#			if(self.inventory[index].name.lower() == "hammer" and self.inventory[index].name.lower() == "nail" and self.inventory[index].name.lower() == "cortex" and self.inventory[index].name.lower() == "fusion cannon"):
		#				self.inventory.pop(index)
		#		print(responce)
		#	else:
		#		if(responce):
		#			print (responce)
		gold_indices = []
		gold_total = 0
		for index in range(len(self.inventory)):
			if(isinstance(self.inventory[index], items.Gold)):
				gold_total += self.inventory[index].value
				gold_indices.append(index)
		if(gold_total > 0):
			for index in gold_indices:	
				self.inventory.pop(index)
			self.gold += gold_total
			print("Your wealth increased by %d Gold." % gold_total)
			

	def getinShip(self):# a basic boolean function that only allows ship access if the player the items he/she needs
		if(not self.ship.open and self.x == 1 and self.y == 1):
			counter = 0 #We will check for the 4 items needed to "enter" the ship
			for index in range(len(self.inventory)):
				if(self.inventory[index].name.lower() == 'hammer'):
					counter+=1
				if(self.inventory[index].name.lower() == 'nail'):
					counter+=1
				if(self.inventory[index].name.lower() == 'cortex'):
					counter+=1
				if(self.inventory[index].name.lower() == 'fusion cannon'):
					counter+=1
			if(counter == 4 ):#All items are present
					self.ship.open = True
					self.removeShipitems = True
					self.x = 3
					self.y = 3
					return "You hammer the nail in place. This cortex fits in smoothly. The fusion cannon is attached behind the ship's barrel. You now have a functioning ship.You exit the hatch door and are thrust into space"
			else:#help the player realize what they don't have
					return"You can't access the ship. You need a Fusion Cannon,Cortex,Hammer and Nail"
		else:
			return None

def myself():
	print(Player())


class PlayerShip:
	def __str__(self):
		return """Your trusty ship!"""
	def __init__(self):
		self.health	= 100
		self.shields = 50
		self.damage = 50
		self.x = 1   				
		self.y = 1
		self.open = False
	
	
	
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

