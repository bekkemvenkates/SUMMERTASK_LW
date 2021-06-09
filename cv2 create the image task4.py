#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2

#Draws a black image and then draws a line from top right corner to bottom left.
myImg = np.zeros((512,512,3),np.uint8)



myImg = cv2.line(myImg,(0,512),(512,0),(0,52,150),2)
myImg=cv2.rectangle(myImg,(25,25),(200,200),(0,255,0),3)
myImg = cv2.circle(myImg,(350,350),105,(255,255,255),3)
myImg=cv2.putText(myImg,"hi,vimal sir ",(90,190),cv2.FONT_ITALIC,2,(0,0,255),2)
cv2.imshow("myImg",myImg)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




