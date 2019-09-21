
# coding: utf-8

# In[13]:

import cv2
import matplotlib.pyplot as plt
import os
print("imports done")


# In[14]:

# for reading an image in three different ways
color = cv2.imread(r'C:\Users\hp\Desktop\Kavya\NIT TRICHY\Data Science\Cat Classifier\dogs-vs-cats\test1\1.jpg',1) # color image
grayscale = cv2.imread(r'C:\Users\hp\Desktop\Kavya\NIT TRICHY\Data Science\Cat Classifier\dogs-vs-cats\test1\1.jpg',0) # grayscaled image
unchanged = cv2.imread(r'C:\Users\hp\Desktop\Kavya\NIT TRICHY\Data Science\Cat Classifier\dogs-vs-cats\test1\1.jpg',-1) # unchanged image
#comment these two lines, it is just a demo of how the pixels appear
print (color.shape)
print("pixel intensities:\n",color)


# In[28]:

#to display images
#windows are named differently
cv2.namedWindow('color', cv2.WINDOW_NORMAL) #to create a window and load an image to it later, this is a resizable window
cv2.imshow('color',color)
cv2.imshow('gray',grayscale)
cv2.imshow('unchanged',unchanged)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('e'): # wait for 'e' key to save and exit
    cv2.imwrite('me.png',color)
    cv2.destroyAllWindows()
#cv2.waitKey(0) #waits indefinitely for a keystroke
#cv2.destroyWindow('color') #to destroy a specific window
#cv2.destroyAllWindows() #to destroy all the windows


# In[29]:

#to write an image into the path as a png file
cv2.imwrite(r'C:\Users\hp\Desktop\Kavya\NIT TRICHY\Data Science\Cat Classifier\dogs-vs-cats\test1\rename1.png',color)


# In[30]:

#use matplotlib for plotting images 
#use of subplots
plt.subplot(1,3,1)
plt.imshow(color, cmap ='gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis 
#comment the above line to check how it works without

plt.subplot(1,3,2)
plt.imshow(grayscale, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis 
#comment the above line to check how it works without

plt.subplot(1,3,3)
plt.imshow(unchanged, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis 
#comment the above line to check how it works without
plt.show()


# In[ ]:



