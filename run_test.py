# contains unit test functions for each module

def debug(cauldron):
	import matplotlib.pyplot as plt
	import matplotlib.image as image
	
	if cauldron == 23:
		img = image.imread('potion.png')
		imgplot = plt.imshow(img)
		plt.axis('off')
		plt.show()

		print("You did it! Great job finding all of the bugs!")
	else:
		print("This spell still has bugs. Try to find some more!")