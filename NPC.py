import player

class NPC:
	def __init__(self):
		raise NotImplementedError("Do not create raw NPC objects.")

	def __str__(self):
		return self.name

class Wilkins(NPC):
	def __init__(self):
		self.name = "Mr. Wilkins"
	def response(input):
		if input == help:
			print("Give me a gem and you can get information that you need")
			print('Have you got the "thing"?')        										  #change thing to items later 
			if #thing in Player.inventory:	         										  <---  ^Same thing
				Wilkinsobject = True
				if Wilkinsobject == True:
					print("""Thanks. Here's the info, don't tell anybody... 
				The Invader's commander is located in the bottom right sector of space.""")
			else:
				print("It's not there, try again")
			
class Riddler(NPC):
	def __init__(self):
		self.name = "A Riddler"
	def response(input):
		if input == help:
				print("""Hello! A Riddler is my name, riddles are my game!
				Ask for one and receive the pain. Get it, because they are hard??""")
				print("""Oh? You want a Riddle? Hehehe, Here it is:""")
				print(#the riddle)
				ranswer = input("What's your answer??")
				if ranswer == #the answer
					print("You got it right... Here is some money...")
					Player.inventory.append("5 Gold")        								 #Change the gold to the gold value in items...
					
class Merchant(NPC):
	def __init__(self):
		self.name = "Merchant"
	def response(input):
		if input == help:
				print("The Mysterious Merchant is here- Oh heh, didn't see you there. What would you like to buy?")
				items = [Blaster_Ammo, Shield, Sparkling_Gem]
				buying = input("What would you like to buy?")
				if buying == Blaster_Ammo:
					BA = input("Would you like to buy Blaster Ammo?")
					if BA == yes:
						Player.inventory.append("20 Ammo")
						#Take out gold for the ammo
						print("That's 1 Gold, thanks for the business.")
					else:
						print("Oh well. Thanks for stopping by.")
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