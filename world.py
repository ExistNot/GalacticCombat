class MapTile:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	
	def intro_text(self):
		raise NotImplementedError("Create a subclass instead!")


class StartTile(MapTile):
	def intro_text(self):
		return """You find yourself in a cave with a flickering torch on the wall.
		You can make out four paths, each equally as dark and foreboding.
		"""


class Room2(MapTile):
	def intro_text(self):
		return """Secret Room with parts for ship! The door you came through is on your left."""


class Room1(MapTile):
	def intro_text(self):
		return """Room in which ship and items are found...
		starter room!
		"""
		
class SpaceTile(MapTile):
	def intro_text(self):
		return """Nothing is here except space..."""
		
class World:									# I choose to define the world as a class. This makes it more straightforward to import into the game.
	map = [
		[Room1(), 			Room2(), 		SpaceTile()],
		[None, 			Room2(), 	SpaceTile()],
		[None, 	StartTile(), 	BoringTile()],
		[SpaceTile(), 	BoringTile(), 	Room4()]
	]
	
	def __init__(self):
		for i in range(len(self.map)):			# We want to set the x, y coordinates for each tile so that it "knows" where it is in the map.
			for j in range(len(self.map[i])):	# I prefer to handle this automatically so there is no chance that the map index does not match
				if(self.map[i][j]):				# the tile's internal coordinates.
					self.map[i][j].x = j
					self.map[i][j].y = i
					
	def tile_at(self, x, y):
		if x < 0 or y < 0:
			return None
		try:
			return self.map[y][x]
		except IndexError:
			return None
			
	def check_north(self, x, y):
		if y-1 < 0:
			room = None
		try:
			room = self.map[y-1][x]
		except IndexError:
			room = None
		
		if(room):
			return [True, "You head to the north."]
		else:
			return [False, "There doesn't seem to be anything to the north."]
			
	def check_south(self, x, y):
		if y+1 < 0:
			room = None
		try:
			room = self.map[y+1][x]
		except IndexError:
			room = None
		
		if(room):
			return [True, "You head to the south."]
		else:
			return [False, "There doesn't seem to be anything to the south."]

	def check_west(self, x, y):
		if x-1 < 0:
			room = None
		try:
			room = self.map[y][x-1]
		except IndexError:
			room = None
		
		if(room):
			return [True, "You head to the west."]
		else:
			return [False, "There doesn't seem to be anything to the west."]
			
	def check_east(self, x, y):
		if x+1 < 0:
			room = None
		try:
			room = self.map[y][x+1]
		except IndexError:
			room = None
		
		if(room):
			return [True, "You head to the east."]
		else:
			return [False, "There doesn't seem to be anything to the east."]