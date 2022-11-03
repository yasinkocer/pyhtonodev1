import cv2 as cv

img = cv.imread ("resim.jpg",0)
img_yukseklik = img.shape[0]
img_genislik = img.shape[1]
cv.imshow("original",img)
cv.waitKey()

for a in range (0,img_yukseklik):
    for b in range (0,img_genislik):
        img[a][b] = 255-img[a][b]
cv.imshow("inverted",img)
cv.waitKey()
