#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
photo1=cv2.imread("dog1.jpg")
photo2=cv2.imread("cat.jpg")

cv2.imshow("dog1",photo1)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow("cat",photo2)
cv2.waitKey()
cv2.destroyAllWindows()

photo1.shape
photo2.shape

photo1=cv2.resize(photo1,(512,512))
photo2=cv2.resize(photo2,(512,512))

temp1=photo1[10:190,95:265].copy()
temp2=photo2[50:230,205:375].copy()

photo1=cv2.resize(photo1,(512,512))
photo2=cv2.resize(photo2,(512,512))

photo1[10:190,95:265]=temp2
photo2[50:230,205:375]=temp1

cv2.imshow("swap1",photo1)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow("swap2",photo2)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:




