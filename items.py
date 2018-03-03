from random import randint 	# Used to generate random integers.

class Item:
	name = "Do not create raw Item objects!"
	
	description = "You should define a description for items in their subclass."
	dropped_description = "You should define the description for this item after it is dropped in its subclass."
	
	is_dropped = False	# This is going to store the status of whether this item has been picked up and dropped before.
	value = 0
		
	def __init__(self, description = ""):
		if(description):
			self.intro_description = description
		else:
			self.intro_description = self.dropped_description
			
	def __str__(self):
		return self.name	

	def room_text(self):
		if(not self.is_dropped):					# We may want to have a different description for a weapon the first time it is encountered vs. after it has been dropped.
			return self.intro_description
		else:
			return self.dropped_description

	def check_text(self):
		return self.description
		
	def drop(self):
		self.is_dropped = True
		
	def pick_up(self):
		self.is_dropped = False
		
	def handle_input(self, verb, noun1, noun2, inventory):
		return [False, None, inventory]
		
		
class Weapon(Item):	
	equip_description = "You should define flavor text for equipping this item in its subclass."
	attack_descriptions = ["You should define one or more attack descriptions as a list in your subclass.", "This is an example secondary attack description"]

	damage = 0		# Define this appropriately in your subclass.
		
	def equip_text(self):
		return self.equip_description
			
	def attack(self):
		return [self.attack_descriptions[randint(0, len(self.attack_descriptions)-1)], self.damage]		# Return damage and a random attack description from your list.

class PBlaster(Weapon):
	def __init__(self):
		self.name = "Blaster"
		self.description = "A Hand held gun used by the cadets and pilots of the space program."
		self.damage = 25
		self.equip_description = "Your P-Blaster is locked and Loaded!"
		self.attack_description = ["You fire the almight P-Blaster","A laser shoots out from your P-Blaster"]

class shipGun(Weapon):
		def __init__(self):
			self.name = "Ship Gun"
			self.description = "A Giant Cannon that your ship holds"
			self.damage = 125
			self.equip_description = "Ship Cannon READY!"
			self.attack_description = ["You fire the almight Ship-Cannon","A laser shoots out from your Ship Cannon"]
		
		
class Gold(Item):
	value = 0		# Define this appropriately in your subclass.
		
	def obtain_text(self):
		return "%i gold was added to your inventory." % value
		
class Gold_Coins(Gold):
	name = "gold coins"
	value = 5
	description = "A small handful of gold coins."
	dropped_description = "A shiny handful of gold coins is lying on the ground."
	
	

class Consumable(Item):
	consume_description = "You should define flavor text for consuming this item in its subclass."

	shield_value = 0		# Define this appropriately in your subclass.
	healing_value = 0		# Define this appropriately in your subclass.
	def consume(self):
		return [self.consume_description, self.healing_value]
		
class Shield_Pack(Consumable):
	name = "Shield Pack"
	shield_value = 50
	value = 10
	description = "A shield pack that increases your shields by 50 to either you or your ship!"
	dropped_description = "Your shield pack is laying on the ground, ready to be used."

class SparklingGem (Item):
	value = 20
	description = "A beautiful, red gem. I believe a certain Invader-Snitch would like this"
	name = "Sparkling Gem"



#items for the ship hanger room
class hatchKey(Item):
	name = "Hatch Key"
	description = "This key allows you to open the hatch. Their is a button in the center of it."

class Hammer(Item):
	name = "Hammer"
	description = "A strong iron-alloy tool, this hammer will pound any thing into its place."
	dropped_description = "A hammer lies on the floor"
class Nail(Item):
	name = "Nail"
	description = "A Iron-alloy nail. It appears to look similar to a hole in your ship."
	dropped_description = "A nail lies on the floor"
class Cortex(Item):
	name = "Cortex"
	description = "A large metal fusion-core, this cortex is the engine of the galaxy. It seems weird for it not to be in a ship"
	dropped_description = "A metal cortex lies on the floor. It looks like it might help a ship run"
class FusionCannon(Item):
	name = "Fusion Cannon"
	description = "A gigantic laser box, the fusion cannon holds ship laser ammo. Without it, your ship can't shoot"
	dropped_description = "A Fusion Cannon lies on the floor. It helps your ship fire lasers, so it's probably useful" 
