#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2

nature1=cv2.imread("msd.jpg")

cv2.imshow("no1",nature1)
cv2.waitKey()
cv2.destroyAllWindows()


# In[2]:


nature2=cv2.imread("vimal.jpg")

cv2.imshow("no2",nature2)
cv2.waitKey()
cv2.destroyAllWindows()


# In[3]:


nature1=cv2.resize(nature1,(512,512))
nature2=cv2.resize(nature2,(512,512))


# In[4]:



fimage=cv2.hconcat([nature1,nature2])

cv2.imshow("merged_image",fimage)
cv2.waitKey()
cv2.destroyAllWindows()

