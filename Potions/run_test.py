# contains unit test functions for each module	

def potion1(eye_of_newt, rabbit_foot, salamander_tongue):	
	import matplotlib.pyplot as plt	
	import matplotlib.image as image	
	try: eye_of_newt	
	except NameError: print('eye_of_newt not properly defined. Make sure the spelling/capitalization are the exact same as in the recipe')	
	else: print('eye_of_newt properly defined')	

	try: salamander_tongue	
	except NameError: print('salamander_tongue not properly defined. Make sure the spelling/capitalization are the exact same as in the recipe')	
	else: print('salamander_tongue properly defined')	

	try: rabbit_foot	
	except NameError: print('rabbit_foot not properly defined. Make sure the spelling/capitalization are the exact same as in the recipe')	
	else: print('rabbit_foot properly defined')	

	if eye_of_newt == 4 and salamander_tongue == 2 and rabbit_foot ==1:	
		print("Fantastic job! You successfully created the Potion of Luck!")
		img = image.imread('../im/potion1.png')	
		imgplot = plt.imshow(img)	
		plt.axis('off')	
		plt.show()		
	elif eye_of_newt == 4 and salamander_tongue == 2:	
		print("It looks like the eye_of_newt and salamander_tongue are correct. You might need to correct the rabbit_foot")	
	elif eye_of_newt == 4 and rabbit_foot == 1:	
		print("So close! The eye_of_newt and rabbit_foot are correct. Looks like you need to correct the salamander_tongue")	
	elif salamander_tongue ==2 and rabbit_foot == 1:	
		print("Almost there! You have the correct amount of salamander_tongue and rabbit_foot. Looks like you need to correct the eye_of_newt")	
	elif eye_of_newt == 4:	
		print("You're getting there. I think you'll need to correct the amount of salamander_tongue and rabbit_foot")	
	elif salamander_tongue == 2:	
		print("Hm... you have the right amount of salamander_tongue. Looks like you'll need to fix eye_of_newt and rabbit_foot")	
	elif rabbit_foot == 1:	
		print("You're making progress! The rabbit_foot is right, but you'll need to fix salamander_tongue and eye_of_newt to complete the potion")	
	else:	
		print("Ack! A black cat ran across your path and you broke a mirror after drinking the potion. \nYou might have changed eye_of_newt. \nTry changing that back to what it was at the start of the activity and see if that helps!")	


def potion2(bat_wing, alligator_tooth, rose_thorn, cat_hair):	
	import matplotlib.pyplot as plt	
	import matplotlib.image as image	
	try: bat_wing	
	except NameError: print('bat_wing not properly defined. Make sure the spelling/capitalization are the exact same as in the recipe')	
	else: print('bat_wing properly defined')	

	try: alligator_tooth	
	except NameError: print('alligator_tooth not properly defined. Make sure the spelling/capitalization are the exact same as in the recipe')	
	else: print('alligator_tooth properly defined')	

	try: rose_thorn	
	except NameError: print('rose_thorn not properly defined. Make sure the spelling/capitalization are the exact same as in the recipe')	
	else: print('rose_thorn properly defined')	

	try: cat_hair	
	except NameError: print('cat_hair not properly defined. Make sure the spelling/capitalization are the exact same as in the recipe')	
	else: print('cat_hair properly defined')	

	if bat_wing == 2 and alligator_tooth == 12 and rose_thorn ==10 and cat_hair ==6:	
		print("Fantastic job! You successfully created the Potion of Invisibility!")	
		img = image.imread('../im/potion2.png')	
		imgplot = plt.imshow(img)	
		plt.axis('off')	
		plt.show()	
	elif bat_wing == 2 and alligator_tooth == 12 and rose_thorn != 10 and cat_hair !=6:	
		print("Hm... it seems like the rose_thorn and cat_hair are off.\nRight now your rose_thorn = ",rose_thorn,"\nAnd cat_hair = ",cat_hair)	
	elif bat_wing == 2 and alligator_tooth == 12 and rose_thorn == 10 and cat_hair !=6:	
		print("So close! I think we need to tweak the cat_hair.\nCurrently cat_hair = ",cat_hair)	
	elif bat_wing == 2 and alligator_tooth == 12 and rose_thorn != 10 and cat_hair ==6:	
		print("Almost there! We might need to tweak the amount of rose_thorn.\nCurrently rose_thorn = ",rose_thorn)	
	else:	
		print("Ack! Drinking the potion just turned you blue!\nCould you have changed bat_wing and/or alligator_tooth? Try changing those back and see if that helps!")	

def potion3(fire_slug, flame_pepper, phoenix_tear, dragon_scale):	
	import matplotlib.pyplot as plt	
	import matplotlib.image as image	
	try: fire_slug	
	except NameError: print('fire_slug not properly defined. Make sure the spelling/capitalization are the exact same as in the recipe')	
	else: print('fire_slug properly defined')	

	try: flame_pepper	
	except NameError: print('flame_pepper not properly defined. Make sure the spelling/capitalization are the exact same as in the recipe')	
	else: print('flame_pepper properly defined')	

	try: phoenix_tear	
	except NameError: print('phoenix_tear not properly defined. Make sure the spelling/capitalization are the exact same as in the recipe')	
	else: print('phoenix_tear properly defined')	

	try: dragon_scale	
	except NameError: print('dragon_scale not properly defined. Make sure the spelling/capitalization are the exact same as in the recipe')	
	else: print('dragon_scale properly defined')	

	if fire_slug == 2 and flame_pepper == 5 and phoenix_tear == 18 and dragon_scale == 15:	
		print("Fantastic job! You successfully created the Potion of Fire Breathing!")	
		img = image.imread('../im/potion3.png')	
		imgplot = plt.imshow(img)	
		plt.axis('off')	
		plt.show()	

	elif fire_slug == 2 and flame_pepper != 5 and phoenix_tear ==18 and dragon_scale !=15:	
		print("You've made good progress! It looks like the flame_pepper and dragon_scale are not correct.\n I think the issue might be with the flame pepper which currently equals ",flame_pepper)	
	elif fire_slug == 2 and flame_pepper == 5 and phoenix_tear !=18 and dragon_scale ==15:	
		print("So close! Try looking bck at the phoenix_tear.\n Currently the phoenix_tear equals ",phoenix_tear)	
	elif fire_slug == 2 and flame_pepper == 5 and phoenix_tear ==18 and dragon_scale !=15:	
		print("Almost there! The problem might be with the dragon_scale.\n Currently the dragon_scale equals ",phoenix_tear)	
	elif fire_slug == 2 and flame_pepper != 5 and phoenix_tear !=18 and dragon_scale !=15:	
		print("Hm... I think we need to correct some things to finish the potion. It looks like the flame_pepper, phoenix_tear, and dragon_scale need to be corrected.\ndragon_scale =",dragon_scale,"\nflame_pepper =",flame_pepper,"\nphoenix_tear =",phoenix_tear)	
	elif fire_slug == 2 and flame_pepper != 5 and phoenix_tear !=18 and dragon_scale !=15:	
		print("Hm... I think we need to correct some things to finish the potion. It looks like the flame_pepper, phoenix_tear, and dragon_scale need to be corrected.\ndragon_scale =",dragon_scale,"\nflame_pepper =",flame_pepper,"\nphoenix_tear =",phoenix_tear)	
	elif fire_slug == 2 and flame_pepper == 5 and phoenix_tear !=18 and dragon_scale !=15:	
		print("Halfway there! The fire_slug and flame_pepper are correct. Now you just have to fix up the phoenix_tear and dragon_scale.\nCurrent pheonix_tear = ", phoenix_tear,"\nCurrent dragon_scale = ",dragon_scale)	
	elif fire_slug == 2 and flame_pepper != 5 and phoenix_tear !=18 and dragon_scale ==15:	
		print("Potion is 50% complete! The fire_slug and dragon_scale are correct. Adust the phoenix_tear and flame_pepper to complete the potion.\nCurrent pheonix_tear = ", phoenix_tear,"\nCurrent flame_pepper = ",flame_pepper)	
	elif fire_slug == 2 and flame_pepper != 5 and phoenix_tear ==18 and dragon_scale ==15:	
		print("Potion seems to be slightly off! Try looking bck at the flame_pepper.\n Currently the flame_pepper equals ",flame_pepper)	
	else:	
		print("Ack! I started breathing ice after drinking the potion!\nYou might have changed the fire_slug. Try changing it back and see if that helps!")	


def debug(cauldron):	
	import matplotlib.pyplot as plt	
	import matplotlib.image as image	

	if cauldron == 23:	
		img = image.imread('../im/potion4.png')	
		imgplot = plt.imshow(img)	
		plt.axis('off')	
		plt.show()	

		print("You did it! Great job finding all of the bugs!")	
	else:	
		print("This spell still has bugs. Try to find some more!")

def potion4(rabbit_foot, cat_hair, dragon_scale, fire_slug, bat_wing):	
	import matplotlib.pyplot as plt	
	import matplotlib.image as image	
	try: rabbit_foot	
	except NameError: print('rabbit_foot not properly defined. Make sure the spelling/capitalization are the exact same as in the recipe')	
	else: print('rabbit_foot properly defined')	

	try: cat_hair	
	except NameError: print('cat_hair not properly defined. Make sure the spelling/capitalization are the exact same as in the recipe')	
	else: print('cat_hair properly defined')	

	try: dragon_scale	
	except NameError: print('dragon_scale not properly defined. Make sure the spelling/capitalization are the exact same as in the recipe')	
	else: print('dragon_scale properly defined')	

	try: fire_slug	
	except NameError: print('fire_slug not properly defined. Make sure the spelling/capitalization are the exact same as in the recipe')	
	else: print('fire_slug properly defined')	
    
	try: bat_wing	
	except NameError: print('bat_wing not properly defined. Make sure the spelling/capitalization are the exact same as in the recipe')	
	else: print('bat_wing properly defined')	

	if rabbit_foot == 6 and cat_hair == 2 and dragon_scale == 36 and fire_slug == 5 and bat_wing == 19:	
		print("Fantastic job! You successfully created the Potion of Transformation!")	
		img = image.imread('../im/potion4-1.png')	
		imgplot = plt.imshow(img)	
		plt.axis('off')	
		plt.show()	

	elif dragon_scale ==36 and fire_slug !=5 and bat_wing == 19:	
		print("You've made good progress! It looks like fire_slug is not correct. Try again! \n")	
	elif dragon_scale !=36 and fire_slug ==5 and bat_wing == 19:	
		print("So close! Try looking bck at the dragon_scale.\n Currently the dragon scale equals ",dragon_scale)	
	elif dragon_scale ==36 and fire_slug ==5 and bat_wing != 19:	
		print("Almost there! The problem might be with the bat_wing.\n Currently the bat_wing equals ",bat_wing)	
              
	elif dragon_scale !=36 and fire_slug !=5 and bat_wing == 19:	
		print("Hm... I think we need to correct some things to finish the potion. It looks like the dragon_scale and fire_slug need to be corrected.")	
	elif dragon_scale !=36 and fire_slug ==5 and bat_wing != 19:	
		print("Close! The dragon_scale and bat_wing are not correct.")	
	elif dragon_scale ==36 and fire_slug !=5 and bat_wing != 19:	
		print("Potion is almost complete! The dragon_scale is correct. Adjust the fire_slug and bat_wing to complete the potion.")	
              
	else:	
		print("Ack! One of my legs turned into a dragon leg and one into a rabbit foot after drinking the potion!\nYou might have changed the rabbit_foot or cat_hair. Try changing it back and see if that helps!")


# Potion 5 
def potion5(ostrich_egg, penguin_fluff, dodo_brain, kiwi_talon):	
	import matplotlib.pyplot as plt	
	import matplotlib.image as image	
	try: ostrich_egg	
	except NameError: print('ostrich_egg not properly defined. Make sure the spelling/capitalization are the exact same as in the recipe')	
	else: print('ostrich_egg properly defined')	

	try: penguin_fluff	
	except NameError: print('penguin_fluff not properly defined. Make sure the spelling/capitalization are the exact same as in the recipe')	
	else: print('penguin_fluff properly defined')	
    
	try: dodo_brain	
	except NameError: print('dodo_brain not properly defined. Make sure the spelling/capitalization are the exact same as in the recipe')	
	else: print('dodo_brain properly defined')	
    
	try: kiwi_talon	
	except NameError: print('kiwi_talon not properly defined. Make sure the spelling/capitalization are the exact same as in the recipe')	
	else: print('kiwi_talon properly defined')	
    
	if ostrich_egg == "one_scrambled" and penguin_fluff == "pinch" and dodo_brain == "one_whole" and kiwi_talon == "three_whole":	
		print("Fantastic job! You successfully created the Potion of Flight!")	
		img = image.imread('../im/PotionOfFlight.png')	
		imgplot = plt.imshow(img)	
		plt.axis('off')	
		plt.show()	

	else:	
		print("sadness. Something went wrong. Try again?")
