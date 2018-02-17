class MapTile:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	
	def intro_text(self):
		raise NotImplementedError("Create a subclass instead!")

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
class TopRight(MapTile):
	def intro_text(self):
		return """You are to the Right of the ship
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
		return """This is a door exit
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
		It's on other the strongest Ship blasters out there"""
class R2Blank(MapTile):
	def intro_text(self):
		return"""
			There are much more fasinating parts of the room to explore"""

##Room 3 tiles
class EmptySpace(MapTile):
	def intro_text(self):
		return """There are much more fasinating parts of Fo-Land to explore
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
                They're a strange man here. His name appears to be MR.WILKINS
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
                        But be careful, Invaders stop here too, and their isn't anyone on in the land that won't rat you ok for the high bounty of Galactic Combater's head
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
		[TopLeft(),	TopMiddle(),	 TopRight(),    DoorExit(),    FusionCannon(),SpaceTile(),      SpaceTile(),    SpaceTile(),    SpaceTile(),SpaceTile()],
		[Nail(),	ShipTile(),	 Hammer(),      Cortex(),      R2Blank(),     SpaceTile(),      SpaceTile(),    SpaceTile(),    SpaceTile(),SpaceTile()],
		[DoorEntrance(),HatchEntrance(), BottomLeft(),  HatchExit(),   R2Blank(),     SpaceTile(),      SpaceTile(),    wormHole(),    	SpaceTile(),	SpaceTile()],
		[SpaceTile(),	SpaceTile(),	 SpaceTile(),   SpaceTile(),   SpaceTile(),   SpaceTile(),      SpaceTile(),    wormHole(),    	SpaceTile(),	SpaceTile()],
		[SpaceTile(),	SpaceTile(),	 SpaceTile(),   SpaceTile(),   SpaceTile(),   SpaceTile(),      SpaceTile(),    wormHole(),    	SpaceTile(),	SpaceTile()],
		[wilkinsTile(), EmptySpace,      EmptySpace,    SpaceTile(),   SpaceTile(),   SpaceTile(),      wormHole(),    	SpaceTile(),    SpaceTile(),	SpaceTile()],
		[EmptySpace,    EmptySpace,	 	 groundNPC(),   SpaceTile(),   SpaceTile(),   SpaceTile(),      SpaceTile(),    SpaceTile(),    SpaceTile(),	SpaceTile()],
		[riddlerTile,   EmptySpace,	 	 EmptySpace,    SpaceTile(),   SpaceTile(),   endStartTile(),	epodTile(),		moveSpace(),	moveSpace(),	moveSpace()],
		[groundNPC(),   planetEntrance(),merchantTile(),SpaceTile(),   SpaceTile(),   endStartTile(),	epodTile(),		moveSpace(),	BossTile(), 	moveSpace()],
		[SpaceTile(),   SpaceTile(),     SpaceTile(),   SpaceTile(),   SpaceTile(),   endStartTile(),	epodTile(),		moveSpace(),	moveSpace(),	moveSpace()]
		
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
