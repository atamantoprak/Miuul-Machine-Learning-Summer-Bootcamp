############################
# Görev 1: Verilen değerlerin veri yapılarını inceleyiiniz
############################
from typing import List

x = 8

y = 3.2

z = 8j + 18

a = "hello world"

b = True

c = 23 < 22

l = [1, 2, 3, 4]

d = {"Name": "Jake",
     "age": 27,
     "address": "downtown"}

t = {"machine learning", "data science"}

s = {"Python", "Machine learning", "Data Science"}

liste = [x, y, z, a, b, c, l, d, t, s]

for i in liste:
    h = type(i)
    print(h)

############################
# Görev 2: Verilen String ifadenin tüm harflerini büyük harfe çeviriniz.
# virgül ve nokta yerine space koyunuz
# kelime kelime ayırınız
############################
text = "The goal is to turn data into information and information into insight"
upletter = text.upper()
upletter.split()

############################
# Görev 3: Verilen listeye aşağıdaki adımları uygulayınız
############################

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Adım1: Verilen listenin eleman sayısına bakınız.
# Adım2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
# Adım3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
# Adım4: Sekizinci indeksteki elemanı siliniz.
# Adım5: Yeni bireleman ekleyiniz.
# Adım6: Sekizinci indekse"N" elemanını tekrar ekleyiniz.

len(lst)

lst[0]
lst[10]
lst[0: 4]
lst.pop(8)
lst.insert(8, "N")

############################
# Görev 4: veilen sözlük yapısına aşağıdaki adımları uygulayınız
############################

dict = {"Christian": ["America", 18],
        "Daisy": ["England", 12],
        "Antonio": ["Spain", 22],
        "Dante": ["Italy", 25]}

dict.keys()
dict.values()
dict["Daisy"][1] = 13
dict.update({"Ahmet": ["Turkey", 24]})
dict.pop("Antonio")

############################
# Görev 5: Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyon yazınız.
############################

l = [2, 13, 18, 93, 22]


def fonk(arg):
    even_list = []
    odd_list = []

    for i in arg:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    return odd_list, even_list


fonk(l)

############################
# Görev 6: listede verilen ilk  öğrenciyi mühendislik sonraki öğrencileri ise tıp fakültesinde sıralayın
############################

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for i, ogr in enumerate(ogrenciler, 1):
    if i <= 3:
        print("Mühendislik Fakültesi {}. öğrenci:{}".format(i, ogr))
    else:
        print("Tıp Fakültesi {} . öğrenci: {}".format(i - 3, ogr))

############################
# Görev 7:Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yeralmaktadır.
# Zip kullanarak ders bilgilerini bastırınız.
############################

ders_kod = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]
dersveri = zip(kredi, ders_kod, kontenjan)
for kredi,ders_kod,kontenjan in dersveri:
    print("Kredisi {} olan {} kodlu dersin kontenjanı {} kişidir".format(kredi, ders_kod,kontenjan))





############################
# Görev 8: aşağıdaki setlerden 1. 2. yi kapsıyor ise ortak elemanlarını değilse 2.nin 1.den farkını yazdıracak bir fonksiyon yaz
############################


kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])


def kümeler(küme1, küme2):
    if küme1.issuperset(küme2):
        birleşim = (küme1.intersection(küme2))
        print(birleşim)
    else:
        fark = (küme2.difference(küme1))
        print(fark)

kümeler(kume1, kume2)