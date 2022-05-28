# -*- coding: utf-8 -*-
"""
Created on Sun May 29 01:03:15 2022

@author: Elif
"""

import cv2
import numpy as np
import imutils
 
# Grab the image

img = cv2.imread("C:/Users/Emre/Desktop/Elif/books.png")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # Hue (Renk Özü), Saturation (Doygunluk) ve Value(Parlaklık) değerlerine göre belirten bir renk uzayı türü
#maskeleme yapacağımız için HSV formatına dönüştürdük

kirmizi_alt_deger = np.array([0,120,100]) #
kirmizi_ust_deger = np.array([10, 255, 255])

mask = cv2.inRange(hsv,kirmizi_alt_deger,kirmizi_ust_deger) #maskaleme yaptık
#sadece parantez içerisindeki değerleri bul

cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts) #bulduğu kontürlerin alanları
sayac = 0
for c in cnts: #kontür alanını hesaplamadı
    alan = cv2.contourArea(c)
    print('Alan:  ', alan)
    if alan > 100: sayac += 1

    cv2.drawContours(img,[c],-1,(0,255,0),3) #bulduğu kontürlerin etrafını çiz

print("Domates sayısı = ", sayac)

while True:
      cv2.imshow("Image", img)

      if cv2.waitKey(1) & 0xFF == ord('q'):
          break