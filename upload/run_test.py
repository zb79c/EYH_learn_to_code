# contains unit test functions for each module

def debug(cauldron):
  import cv2
  import numpy as np
  from matplotlib import pyplot as plt
  #import test 
	
  if cauldron == 23:
		# open method used to open different extension image file 
	  print("You did it! Great job finding all of the bugs!")
	  img = cv2.imread("potion.jpg")
	  plt.imshow(img)
	  plt.axis('off')
	  plt.show()
  
  else:
	  print("This spell still has bugs. Try to find some more!")