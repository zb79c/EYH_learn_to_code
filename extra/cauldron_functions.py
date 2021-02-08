'''These functions allow you to add new ingredients or remove
   ingredients from your cauldron
'''
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
	