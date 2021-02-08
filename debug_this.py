## debug this spell

# Imports PIL module  
from PIL import Image 


def add_quantity(cauldron, ingredient, desired_weight_to_add):
	""" adds a specified quantity of the new ingredient to the cauldron. 
		Returns if cauldron doesn't contain that ingredient yet """
	if ingredient not in cauldron:
		print("ingredient: " +str(ingredient) + " not yet in cauldron")
		return

	cauldron[ingredient] = cauldron[ingredient] + desired_weight_to_add
	print(str(desired_weight_to_add) + " of " + str(ingredient) + " added to cauldron")
	

def add_ingredient(cauldron, new_ingredient, amount):
	""" adds a specified amount of a new ingredient into the cauldron
		Returns if ingredient is already in cauldron """
	if new_ingredient in cauldron:
		print("ingredient: " + str(new_ingredient) + " already in cauldron")
		return

	cauldron[new_ingredient] = amount
	print("new ingredient " + str(new_ingredient) + " added to cauldron")
	


def main():
	''' Use predefined functions add_quantity and add_ingredient to add 
		the correct amount of each ingredient to make the correct potion
		Recipe:
		 		5 unicorn haris
	 			3 spider eyes
				10 dragon scales
	 			1 lionfish spine
	'''

	# initialize cauldron (dictionary) with one unit of each ingredient
	cauldron = dict(unicorn_hair=1, spider_eyes=1, dragon_scale=1)

	# add the correct amount of each ingredient
	add_quantity(cauldron, "unicorn_hair", 4)
	add_quantity(cauldron, "spider_eyes", 2)
	add_quantity(cauldron, "dragon_scale", 9)
	#add_quantity(cauldron, "lionfish_spine", 1)

	# add one last ingredient: one lionfish spine
	add_ingredient(cauldron, "lionfish_spine", 1)


	if sum(cauldron.values()) == 19:
		print("potion complete") 
		# open method used to open different extension image file 
		im = Image.open("potion.jpg")  
		im.show() 
	else:
		print("potion incomplete")


if __name__ == "__main__":
	main()



