''' Use predefined functions add_ingredient and remove_ingredient to add 
	the correct amount of each ingredient to make the correct potion
	Recipe:
	 		5 unicorn haris
 			3 spider eyes
			10 dragon scales
 			1 lionfish spine
'''

# Imports PIL module  
from PIL import Image 
import cauldron_functions as cf




# initialize cauldron (dictionary) with one unit of each ingredient
cauldron = dict(unicorn_hair=1, spider_eyes=1, dragon_scale=1)

# add the correct amount of each ingredient
cf.add_quantity(cauldron, "unicorn_hair", 4)
cf.add_quantity(cauldron, "spider_eyes", 2)
cf.add_quantity(cauldron, "dragon_scale", 9)
#add_quantity(cauldron, "lionfish_spine", 1)

# add one last ingredient: one lionfish spine
cf.add_ingredient(cauldron, "lionfish_spine", 1)


if sum(cauldron.values()) == 19:
	print("potion complete") 
	# open method used to open different extension image file 
	im = Image.open("potion.jpg")  
	im.show() 
else:
	print("potion incomplete")




