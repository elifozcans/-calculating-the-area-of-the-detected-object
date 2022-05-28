#  calculating the area of the detected object 
 object detection and calculating the area of the detected object

Bu çalışmada OPENCV ve NUMPY kütüphanelerini kullanarak bir resmin üzerinde belirli bir rengin algılanması amaçlanmış olup, belirlediğimiz renkte algılanan nesnelerin sayısı ve alanı hesaplanmıştır.
Çalışmada kullanılan örnek model rengi "kırmızı" olarak seçilmiş olup, alt ve üst değerler kırmızı renk için belirlenmiştir fakat kodlar üzerinde seçilen renge göre HSV renk değerleri belirlenerek istenilen renk üzerinde tespit edilen nesnenin alan hesabı yapılabilir.

Önemli notlar:
# Hue (Renk Özü), Saturation (Doygunluk) ve Value(Parlaklık) değerlerine göre belirten bir renk uzayı türü,maskeleme yapacağımız için RGB den HSV formatına dönüştürdük.
Faydalı kaynak: https://cvexplained.wordpress.com/2020/04/28/color-detection-hsv/#:~:text=The%20HSV%20values%20for%20true,10%20and%20160%20to%20180.

Değerli projeleriyle bana ilham kaynağı olan Prof. Bülent Sezen' e teşekkür ederim.


