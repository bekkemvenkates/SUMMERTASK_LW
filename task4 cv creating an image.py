#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


image=np.zeros((500,500,3))
cv2.imshow("i2",image)
cv2.waitKey()
cv2.destroyAllWindows()


# In[3]:


image.shape


# In[4]:


image[0:500,0:500]=(0,29,19)
cv2.imshow("i2",image)
cv2.waitKey()
cv2.destroyAllWindows()


# In[5]:


image=cv2.circle(image,(80,80),100,(255,255,255),7)
image=cv2.rectangle(image,(100,200),(350,325),(0,0,0),3)
image=cv2.line(image,(100,200),(135,100),(0,0,0),3)
image=cv2.line(image,(170,200),(135,100),(0,0,0),3)
image=cv2.line(image,(170,200),(170,325),(0,0,0),3)
image=cv2.line(image,(135,100),(350,100),(0,0,0),3)
image=cv2.line(image,(350,200),(350,100),(0,0,0),3)


cv2.imshow("final_image",image)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:




