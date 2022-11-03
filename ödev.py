import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img = cv.imread ("resim.jpg",0)
img_yukseklik = img.shape[0]
img_genislik = img.shape[1]
Histogram =np.zeros([256])
for a in range (0,img_yukseklik):
    for b in range (0,img_genislik):
        Histogram [img[a,b]] +=1
plt.plot(Histogram)
plt.title("HİSTOGRAM")
plt.show()