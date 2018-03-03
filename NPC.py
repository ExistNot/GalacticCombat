import items

class NPC:
	name = "Do not create raw NPCs!"
	description = "There is no description here because you should not create raw NPC objects!"
	
	goods = []	# Stuff an NPC is carrying.
	quantities = []	# Quantities of that stuff.
	
	first_encounter = True			# Used to do something different on first encounter.
	
	def __str__(self):
		return self.name
		
	def check_text(self):
		if(self.first_encounter):
			text = self.first_time()
			return text
		else:
			return self.description

	def talk(self):		# Add to this method if you want to be able to talk to your NPC.
		return "The %s doesn't seem to have anything to say." % self.name		

	def first_time(self):		# Used to have your NPC do something different the first time you see them.
		self.first_encounter = False
		return self.description
		
	def handle_input(self, verb, noun1, noun2, inventory):
		return [False, None, inventory]
class Wilkins(NPC):
	name = "Mr. Wilkins"
	goods = []
	quantities = [1, -1, 2]		# Set quantity to -1 if you want it to be infinite.
	
	description = "A war hardened man that has information on the Invaders."
	def talk(self):		# Add to this method if you want to be able to talk to your NPC.
		print("Mr. Wilkins says 'Give me a Gem and you shall receive informations on the Invaders!")
		if Sparkling_Gem in Player.inventory:	 
				Wilkinsobject = True
				if (Wilkinsobject == True):
					for index in range(len(self.inventory)):
						if(isinstance(self.inventory[index], items.SparklingGem)):
							for index in reversed(SparklingGem_indices):		# Reversed to avoid popping the wrong element.	
								self.inventory.pop(index)
								print("""Thanks. Here's the info, don't tell anybody... 
								The Invader's commander is located in the bottom right sector of space.""")
				else:
					print("It's not there, try again")
	def first_time(self):		# Used to have your NPC do something different the first time you see them.
		self.first_encounter = False
		text = self.description
		text += " Mr. Wilkins says you shall receive information on the Invaders if you give me a Sparkling Gem."
		return text
		
	def give(self, item, inventory):
		for good in self.goods:
			if(good == item):
				inventory.append(good)
				if(self.quantities[self.goods.index(good)] > 0):
					self.quantities[self.goods.index(good)] -= 1
		return inventory	
		
	def handle_input(self, verb, noun1, noun2, inventory):
		if(noun1 == 'mr. wilkins' or noun1 == 'wilkins'):
			if(verb == 'check'):
				return [True, self.check_text(), inventory]
			elif(verb == 'talk'):
				text = self.talk()
				return [True, text, inventory]				
				
class Riddler(NPC):
	name = "Riddler"
	goods = [items.Gold_Coins()]
	quantities = [1, -1, 2]		# Set quantity to -1 if you want it to be infinite.
	description = "A Riddler that gives riddles for Gold."
	def talk(self):		# Add to this method if you want to be able to talk to your NPC. ###CHANGE LATER
		print("Want some Gold? Ask for a riddle and I shall fiddle your mind down the to middle!")
		print("the riddle")
		ranswer = "the answer"
		pans = input("What is your response?")
		return""
		
	def riddle(self):
		print("Want some Gold? Ask for a riddle and I shall fiddle your mind down the to middle!")
		print("the riddle")
		ranswer = "the answer"
		pans = input("What is your response?")
		return pans==ranswer 

	def give(self, item, inventory):
		for good in self.goods:
			if(good == item):
				inventory.append(good)
				if(self.quantities[self.goods.index(good)] > 0):
					self.quantities[self.goods.index(good)] -= 1
		return inventory

	def first_time(self):		# Used to have your NPC do something different the first time you see them.
		self.first_encounter = False
		text = self.description
		text += " Hello! A Riddler is my name, riddles are my game! Ask for one and receive the pain. Get it, because they are hard?? Oh? You want a Riddle? Hehehe, Here it is:"
		return text
	def handle_input(self, verb, noun1, noun2, inventory):
		if(noun1 == 'riddler' or noun1 == 'a riddler'):
			if(verb == 'check'):
				return [True, self.check_text(), inventory]
			elif(verb == 'talk'):
				text = self.talk()
				return [True, text, inventory]
					
class Merchant(NPC):
	def __init__(self):
		self.name = "Merchant"
	def response(input):
		if input == help:
				print("The Mysterious Merchant is here- Oh heh, didn't see you there. What would you like to buy?")
				items = [Shield_Pack, Sparkling_Gem]
				buying = input("What would you like to buy?")
				if buying == Shield:
					SH = input("Would you like to buy Shields?")
					if SH == yes:
						Player.shields = Player.shields + 50
						#Take out gold for the shields
						print("That's 2 Gold, thanks for the business.")
					else:
						print("Oh well. Thanks for stopping by.")
				if buying == Sparkling_Gem:
					SG = input("Would you like to buy the majestic Sparkling Gem?")
					if SG == yes:
						Player.inventory.append("Sparkling Gem")
						#Take out gold for the Gem
						print("That's 10 Gold, thanks for the business.")
					else:
						print("Oh well. Thanks for stopping by.")