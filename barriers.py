class Barrier:
	name = None
	passable = False
	state = None	# Used to store the state of doors or hidden passages.
	locked = None	# Used to store the state of locked doors, if applicable.
	
	verbose = False	# Used to determine whether or not include the barrier's description in the room description.

	def __init__(self, direction):
		if(direction == 'n'):
			self.direction = 'north'
		elif(direction == 's'):
			self.direction = 'south'
		elif(direction == 'e'):
			self.direction = 'east'
		elif(direction == 'w'):
			self.direction = 'west'
		elif(direction == 'a'):
			self.direction = 'a'
		elif(direction == 'go'):
			self.direction = 'go'
		else:
			raise NotImplementedError("Barrier direction is not recognized.")
	
	def description(self):
		raise NotImplementedError("Create a subclass instead!")
		
	def handle_input(self, verb, noun1, noun2, inventory):
		return [False, None, inventory]
		
class Wall(Barrier):
	def description(self):
		return "There doesn't seem to be a path to the %s." % self.direction
		
class Door(Barrier):
	name = 'Door'
	state = 'closed'	# Used to store the state of doors or hidden passages.
	
	verbose = True	# Used to determine whether or not include the barrier's description in the room description.
	
	def description(self):
		if(self.state == 'closed'):
			return "A door blocks your path to the %s. There's an other room! I feel like something important is in there" % self.direction
		else:
			return "A door lies open before you to the %s." % self.direction
		
	def handle_input(self, verb, noun1, noun2, inventory):
		if(noun1 == 'door' or noun1 == 'door'):
			if(verb == 'check'):
				return [True, self.description(), inventory]
			if(verb == 'open'):
				if(self.state == 'closed'):
					self.state = 'open'
					self.passable = True
					return [True, "You push the door, and it opens swiftly", inventory]
				else:
					return [True, "The door is already open.", inventory]
			if(verb == 'close'):
				if(self.state == 'open'):
					self.state = 'closed'
					self.passable = False
					return [True, "You close the door", inventory]
				else:
					return [True, "The door is already closed.", inventory]
			
		return [False, "", inventory]
		
		
class HatchDoor(Barrier):
	name = 'Locked Door'
	state = 'closed'	# Used to store the state of doors or hidden passages.
	locked = True		# Used to store the state of locked doors, if applicable.
	
	verbose = True	# Used to determine whether or not include the barrier's description in the room description.
	
	def description(self):
		if(self.state == 'closed'):
			if(self.locked):
				return "A hatch blocks a passageway to the %s. It appears to be controlled by a wireless key. Your ship may help you." % self.direction
			else:
				return "You can now open the hatch"
		else:
			return "The hatch lies open before you to the %s." % self.direction
		
	def handle_input(self, verb, noun1, noun2, inventory):
		if(noun1 == 'door' or noun1 == 'locked door'):
			if(verb == 'check'):
				return [True, self.description(), inventory]
			if(verb == 'open'):
				if(self.state == 'closed'):
					if(self.locked):
						return [True, "You try to look for a handle, but the door doesn't have one. If this door is to budge, it'll need some wireless key", inventory]
					else:
						self.state = 'open'
						self.passable = True
						return [True, "The hatch opens. You can now fly out to space", inventory]
				else:
					return [True, "The hatch is already open. Space awaits you", inventory]
			if(verb == 'close'):
				if(self.state == 'open'):
					self.state = 'closed'
					self.passable = False
					return [True, "You lock the hatch", inventory]
				else:
					return [True, "The hatch is closed", inventory]
			if(verb == 'unlock'):
				if(self.locked):
					if(noun2 == 'iron key'):
						for index in range(len(inventory)):
							if(inventory[index].name.lower() == 'hatch key'):
								inventory.pop(index)	# Removes the item at this index from the inventory.
								self.locked = False
								return [True, "You press the button in the middle, and the hatch groans out.", inventory]
						return [True, "You don't seem to have the right key for the hatch.", inventory]
					elif(noun2 == 'key'):
						return [True, "Be more specific. This door only takes a specific key.", inventory]
					else:
						return [True, "What item do you plan to unlock the hatch with?", inventory]
				else:
					return [True, "The hatch is already open.", inventory]
			
		return [False, "", inventory]
		
class Asteroid(Barrier):
	def description(self):
		return "There seems to be asteroids blocking your path to the %s." % self.direction
class pWall(Barrier):
	def description(self):
		if (self.direction == "a"):
			return "You see a planet to the West"
		elif(self.direction == "go"):
			return "You can enter the planet. Head north"
		return "You see a planet to the %s." % self.direction +  "You cannot enter this planet from here %s." % self.direction