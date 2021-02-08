# contains unit test functions for each module

def debug(cauldron):
  from PIL import Image
  #import test 
	
  if cauldron == 23:

	image = Image.open('potion.jpg')
	image.show()
	# open method used to open different extension image file 
	 print("You did it! Great job finding all of the bugs!")
	  
  
  else:
	  print("This spell still has bugs. Try to find some more!")