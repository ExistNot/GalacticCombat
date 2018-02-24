import items
import barriers

from random import randint 	# Used to generate random integers.

class MapTile:
	description = "Do not create raw MapTiles! Create a subclass instead!"
	barriers = []
	enemies = []
	items = []
	
	def __init__(self, x=0, y=0, barriers = [], items = [], enemies = []):
		self.x = x
		self.y = y
		for barrier in barriers:
			self.add_barrier(barrier)
		for item in items:
			self.add_item(item)
		for enemy in enemies:
			self.add_enemy(enemy)
	
	def intro_text(self):
		text = self.description
		for barrier in self.barriers:
			if(barrier.verbose):
				text += " " + barrier.description()
		#for enemy in self.contents['enemies']:
		#	text += " " + enemy.description()
		for item in self.items:
			text += " " + item.room_text()
		return text
		
	def handle_input(self, verb, noun1, noun2, inventory):
		if(not noun2):
			if(verb == 'check'):
				for item in self.items:
					if(item.name.lower() == noun1):
						return [True, item.check_text(), inventory]
			elif(verb == 'take'):
				for index in range(len(self.items)):
					if(self.items[index].name.lower() == noun1):
						if(isinstance(self.items[index], items.Item)):
							pickup_text = "You picked up the %s." % self.items[index].name
							inventory.append(self.items[index])
							self.items.pop(index)
							return [True, pickup_text, inventory]
						else:
							return [True, "The %s is too heavy to pick up." % self.items[index].name, inventory]
			elif(verb == 'drop'):
				for index in range(len(inventory)):
					if(inventory[index].name.lower() == noun1):
						inventory[index].is_dropped = True
						drop_text = "You dropped the %s." % inventory[index].name
						self.add_item(inventory[index])
						inventory.pop(index)
						return [True, drop_text, inventory]

		for list in [self.barriers, self.items, self.enemies]:
			for item in list:
				[status, description, inventory] = item.handle_input(verb, noun1, noun2, inventory)
				if(status):
					return [status, description, inventory]
					
		for list in [self.barriers, self.items, self.enemies]:			# Added to give the player feedback if they have part of the name of an object correct.
			for item in list:
				if(item.name):
					if(noun1 in item.name):
						return [True, "Be more specific.", inventory]
			
		return [False, "", inventory]
		
	def add_barrier(self, barrier):
		if(len(self.barriers) == 0):
			self.barriers = [barrier]		# Initialize the list if it is empty.
		else:
			self.barriers.append(barrier)	# Add to the list if it is not empty.
			
	def add_item(self, item):
		if(len(self.items) == 0):
			self.items = [item]		# Initialize the list if it is empty.
		else:
			self.items.append(item)	# Add to the list if it is not empty.
			
	def add_enemy(self, enemy):
		if(len(self.enemies) == 0):
			self.enemies = [enemy]		# Initialize the list if it is empty.
		else:
			self.enemies.append(enemy)	# Add to the list if it is not empty.


##Room1 Tiles
class ShipTile(MapTile):
	def intro_text(self):
		return """Starter Room for Player
		"""
class Nail(MapTile):
	def intro_text(self):
		return """There appears to be a nail of the floor
		"""
class Hammer(MapTile):
	def intro_text(self):
		return """There appears to be a Hammer of the floor
		"""
class HatchEntrance(MapTile):
	def intro_text(self):
		return """This is the hatch entrance
		"""

class DoorEntrance(MapTile):
	def intro_text(self):
		return """This is a door entrance
		"""
class TopLeft(MapTile):
	def intro_text(self):
		return """You are to the Left of the ship
		"""
class MiddleLeft(MapTile):
	def intro_text(self):
		return """You are to the left of the ship
		"""
class TopMiddle(MapTile):
	def intro_text(self):
		return """You are to the In front of the ship
		"""
class BottomLeft(MapTile):
	def intro_text(self):
		return """There's a Hammer to the north
		"""
		
##Room2 Tiles
class DoorExit(MapTile):
	def intro_text(self):
		return """You are on the other side of the door
		"""
class HatchExit(MapTile):
	def intro_text(self):
		return """This is the hatch exit
		"""
class Cortex(MapTile):
	def intro_text(self):
		return """WOW There's a cortex here
		(You might need it for the ship)"""
class FusionCannon(MapTile):
	def intro_text(self):
		return """There's a Fusion Cannon
		It's on other strong Ship blasters out there"""
class R2Blank(MapTile):
	def intro_text(self):
		return"""
			There are much more fascinating parts of the room to explore"""

##Room 3 tiles
class EmptySpace(MapTile):
	def intro_text(self):
		return """There are much more fascinating parts of Fo-Land to explore
		"""
class SomeOne(MapTile):
	def intro_text(self):
		return """There is Someone Here(The person will be added
		"""
class groundNPC(Maptile):
        def intro_text(self):
                return """
                        There's an enemy Invader!!!!!!!!!!!
		"""
class wilkinsTile(Maptile):
        def intro_text(self):
                return """
                They're a strange man here. His name appears to be MR. WILKINS
		"""
class riddlerTile(Maptile):
        def intro_text(self):
                return """There's something puzzling about this man! He name appears to be A RIDDLER
		"""
class merchantTile(Maptile):
        def intro_text(self):
                return """There's a MERCHANT here!
		"""
class planetEntrance(Maptile):
        def intro_text(self):
                return """You have entered FO-LAND!!!!!
                        Here you will find all the the parts a galaxy pilot could want, and also gossip for the locals
                        But be careful, Invaders stop here too, and there isn't anyone on in the land that won't rat you out for the high bounty of Galactic Combater's head
                        Be careful.....
		"""
##Room 4 and Boss Tiles		
class BossTile(MapTile):
	def intro_text(self):
		return """
		This Tile Holds the boss
		"""
class epodTile(MapTile):
	def intro_text(self):
		return """
		This Tile Hold the boss
		"""
class endStartTile(MapTile):
        def intro_text(self):
                return """
                        This is the beginning of the end?
                        But for who? You? The Invaders?
                        3 enemy epod stare out at you. A single ship
                        You feel the sweat of your brow; tensions are rising...
                        Are you ready, to face your destiny
                        (I guess it doesn't matter, because here, you GOOOOO
                        """
class moveSpace(MapTile):
        def intro_text(self):
                return """
                        This is space you can move in.
                        You're so close... DEFEAT THAT BOSS SHIP
                        """


#Space Tiles	
class SpaceTile(MapTile):
	def intro_text(self):
		return """Nothing is here except space..."""

class wormHole(MapTile):
        def intro_text(self):
                return """You are in a worm hole
                                You are also dead,
                                Next time try not to stray in empty space
                                Game Over
                                """
class World:									# I choose to define the world as a class. This makes it more straightforward to import into the game.
	map = [
		[TopLeft(barriers = [barriers.Wall('n')]),														TopMiddle(barriers = [barriers.Wall('n')]),	 									DoorEntrance(barriers = [barriers.Wall('n'),barriers.Door('e')]),    					DoorExit(barriers = [barriers.Wall('n')]),    					FusionCannon(barriers = [barriers.Wall('n'),barriers.Wall('e')]),SpaceTile(),      SpaceTile(),    SpaceTile(),    	SpaceTile(),	SpaceTile()],
		[Nail(),																						ShipTile(),	 																	Hammer(barriers = [barriers.Wall('e')]),      											Cortex(barriers = [barriers.Wall('w')]),      					R2Blank(barriers = [barriers.Wall('e')]),     					SpaceTile(),      SpaceTile(),    SpaceTile(),    	SpaceTile(),	SpaceTile()],
		[BottomLeft(barriers = [barriers.Wall('w'),barries.Wall('s')]), 								MiddleLeft(barriers = [barries.Wall('s')]),   									HatchEntrance(barriers = [barriers.Wall('e'),barries.Wall('s'),barries.HatchDoor('e')]),HatchExit(barriers = [barriers.Wall('w'),barries.Wall('s')]),  R2Blank(barriers = [barriers.Wall('e'),barries.Wall('s')]),     SpaceTile(),      SpaceTile(),    wormHole(),    	SpaceTile(),	SpaceTile()],
		[SpaceTile(),																					SpaceTile(),	 																SpaceTile(),   																			SpaceTile(),   													SpaceTile(),   													SpaceTile(),      SpaceTile(),    wormHole(),    	SpaceTile(),	SpaceTile()],
		[SpaceTile(),																					SpaceTile(),	 																SpaceTile(),   																			SpaceTile(),   													SpaceTile(),   													SpaceTile(),      SpaceTile(),    wormHole(),    	SpaceTile(),	SpaceTile()]
		[wilkinsTile(barriers = [barriers.Wall('w'),barries.Wall('n')]), 								EmptySpace(barriers = [barries.Wall('n')]),      								EmptySpace(barriers = [barriers.Wall('e'),barries.Wall('n')]),   						SpaceTile(),   													SpaceTile(),   													SpaceTile(),      SpaceTile(),    	SpaceTile(),    SpaceTile(),	SpaceTile()],
		[EmptySpace(barriers = [barriers.Wall('w')]),    												EmptySpace(),	 	 															groundNPC(barriers = [barriers.Wall('e')]),   											SpaceTile(),   													SpaceTile(),   													SpaceTile(),      	SpaceTile(),    SpaceTile(),    SpaceTile(),	SpaceTile()],
		[riddlerTile(),   																				EmptySpace(),	 	 															EmptySpace(barriers = [barriers.Wall('e')]),    										SpaceTile(),   													SpaceTile(),   													endStartTile(),		epodTile(),		moveSpace(),	moveSpace(),	moveSpace()],
		[groundNPC(barriers = [barriers.Wall('e'),barries.Wall('s')]),   								planetEntrance(),																merchantTile(barriers = [barriers.Wall('e'),barries.Wall('s')]),						SpaceTile(),  													SpaceTile(),   													endStartTile(),		epodTile(),		moveSpace(),	BossTile(), 	moveSpace()],
		[SpaceTile(),   																				SpaceTile(),     																SpaceTile(),   																			SpaceTile(),   													SpaceTile(),   													endStartTile(),		epodTile(),		moveSpace(),	moveSpace(),	moveSpace()]
		
	]

	def __init__(self):
		for i in range(len(self.map)):			# We want to set the x, y coordinates for each tile so that it "knows" where it is in the map.
			for j in range(len(self.map[i])):	# I prefer to handle this automatically so there is no chance that the map index does not match
				if(self.map[i][j]):				# the tile's internal coordinates.
					self.map[i][j].x = j
					self.map[i][j].y = i
					
					self.add_implied_barriers(j,i)	# If there are implied barriers (e.g. edge of map, adjacent None room, etc.) add a Wall.
						
					
	def tile_at(self, x, y):
		if x < 0 or y < 0:
			return None
		try:
			return self.map[y][x]
		except IndexError:
			return None
			
	def check_north(self, x, y):
		for barrier in self.map[y][x].barriers:
			if(barrier.direction == 'north' and not barrier.passable):
				return [False, barrier.description()]				
				
		if y-1 < 0:
			room = None
		else:
			try:
				room = self.map[y-1][x]
			except IndexError:
				room = None
		
		if(room):
			return [True, "You head to the north."]
		else:
			return [False, "There doesn't seem to be a path to the north."]
			
	def check_south(self, x, y):
		for barrier in self.map[y][x].barriers:
			if(barrier.direction == 'south' and not barrier.passable):
				return [False, barrier.description()]	
				
		if y+1 < 0:
			room = None
		else:
			try:
				room = self.map[y+1][x]
			except IndexError:
				room = None
		
		if(room):
			return [True, "You head to the south."]
		else:
			return [False, "There doesn't seem to be a path to the south."]

	def check_west(self, x, y):
		for barrier in self.map[y][x].barriers:
			if(barrier.direction == 'west' and not barrier.passable):
				return [False, barrier.description()]	
	
		if x-1 < 0:
			room = None
		else:
			try:
				room = self.map[y][x-1]
			except IndexError:
				room = None
		
		if(room):
			return [True, "You head to the west."]
		else:
			return [False, "There doesn't seem to be a path to the west."]
			
	def check_east(self, x, y):
		for barrier in self.map[y][x].barriers:
			if(barrier.direction == 'east' and not barrier.passable):
				return [False, barrier.description()]	
				
		if x+1 < 0:
			room = None
		else:
			try:
				room = self.map[y][x+1]
			except IndexError:
				room = None
		
		if(room):
			return [True, "You head to the east."]
		else:
			return [False, "There doesn't seem to be a path to the east."]
			
	def add_implied_barriers(self, x, y):

		[status, text] = self.check_north(x,y)
		barrier_present = False
		if(not status):
			for barrier in self.map[y][x].barriers:
				if barrier.direction == 'north':
					barrier_present = True
			if(not barrier_present):
				self.map[y][x].add_barrier(barriers.Wall('n'))	
				
		[status, text] = self.check_south(x,y)
		barrier_present = False
		if(not status):
			for barrier in self.map[y][x].barriers:
				if barrier.direction == 'south':
					barrier_present = True
			if(not barrier_present):
				self.map[y][x].add_barrier(barriers.Wall('s'))	
			
		[status, text] = self.check_east(x,y)
		barrier_present = False
		if(not status):
			for barrier in self.map[y][x].barriers:
				if barrier.direction == 'east':
					barrier_present = True
			if(not barrier_present):
				self.map[y][x].add_barrier(barriers.Wall('e'))	
			
		[status, text] = self.check_west(x,y)
		barrier_present = False
		if(not status):
			for barrier in self.map[y][x].barriers:
				if barrier.direction == 'west':
					barrier_present = True
			if(not barrier_present):
				self.map[y][x].add_barrier(barriers.Wall('w'))	