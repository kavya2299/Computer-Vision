
# coding: utf-8

# ### Importing libraries
# * cv2 is imported for using image and video files and to do some processing on them.
# * matplotlib is a tool used here to visualize the images.
# * os is used to deal with system and to retrieve files from the current hardware.

# In[1]:

import cv2
import matplotlib.pyplot as plt
import os
print("all libraries imported")


# In[9]:

path=input("Enter the path:")
print(path) #to ensure that the path of images is the same as what is typed in 

# a function to load only images that are in the directory given by the path
def load_images(path):
    return(os.path.join(path,f) for f in os.listdir(path) if f.endswith(".jpg")) # f for files 

filenames=load_images(path)
print("images loaded")

# getting a list of images read by cv2 in terms of their pixel values
images=[]
for file in filenames:
    images.append(cv2.imread(file,-1))
print("images read in unchanged mode")

#to see or display a particular image 
#either use cv2 or use matplotlib since the latter is way more efficient and friendly than the former
index=input("Enter a number from 1 to 12500 to see an image:")
def display_img(index):
    #cv2.imshow("image",images[index])
    # if the imshow function does not work, use matplotlib
    plt.imshow(images[index],cmap=plt.cm.binary)
display_img(int(index))
# to write images to the directory specified in .png format    
num=0
for image in images:
    cv2.imwrite(os.path.join(path, str(num),'.jpg'),image)
print("images written in .png format in the path")


# In[ ]:



