

# Meden NumPy (why NumPy)
# NumPy Array'i oluşturmak(Creating NumPy Arrays)
# NumPy Array Özellikleri (Attirbutes of numpy Arrays)
# Yeniden Şekillerndirme(Reshaping)
# Index Seçimi (Index Selection)
# Slicing
# Fancy Index
# Numpy'da koşullu işlemler(conditions on numpy)
# Matematiksel işlemler(Mathematical Operations)

# Sabit tipte veriler tutar her biri için tip, boyut bilgisi tutmaz ve yüksek seviyeden vektörel işlemler yapabilir, hızlıdır.


a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

# numpy
# bitirme sorularından birinin denemsi
import numpy as np
from functools import reduce
num_list = np.arange(1, 10)
filter_list =[0, 1, 2, 4, 5, 7, 8]
final_list = reduce(lambda x, y: x*y, filter_list)

a =np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a * b

#####################################
# NumPy Array'i oluşturmak
#####################################
import numpy as np


np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))

np.zeros(10, dtype=int)
np.random.randint(0, 10, size=10)
np.random.normal(10, 4, (3, 4))# ortalama , standart sapma, boyut


#####################################
# NumPy Array Özellikleri
#####################################
# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size=5)
a.ndim
a.shape
a.size
a.dtype

#####################################
# Yeniden Şekillendirme (Reshaping)
#####################################

np.random.randint(1, 10, size=9)
np.random.randint(1, 10, size=9).reshape(3, 3)



#####################################
# Index seçimi (Index Selection) önemli konu
#####################################
a = np.random.randint(10, size=10)
a[0]
a[0:5]
a[0] = 999

m = np.random.randint(10, size=(3, 5))

m[0, 0]
m[1, 1]
m[2, 3]
m[2, 3] = 999
m[2,3] = 2.9
m[:, 0] # tüm satırlar 0. sütun
m[1, :] # birinci satır tüm sütunlar
m[0:2, 0:3]



#####################################
# Fancy Index
#####################################
import numpy as np

v = np.arange(0, 30, 3) # 0 dan 30 a kadar 3 er 3 er artan bir liste

catch = [1, 2, 3]
v[catch]


#####################################
# Numpy'da koşullu ifadeler (conditions ın Numpy)
#####################################

import numpy as np

v = np.array([1, 2, 3, 4, 5])

# klasik döngü ile
ab = []
for i in v:
     if i < 3:
         ab.append(i)

# Numpy ile
v < 3

v[v < 3]
v[v == 3]




#####################################
# Matematiksel işlemler
#####################################


import numpy as np

v = np.array([1, 2, 3, 4, 5])

v / 5
v * 5 / 10
v ** 2


np.subtract(v, 1)
np.add(v, 1)
np.mean(v)
np.sum(v)
np.max(v)
np.var(v) # varyans

# iki bilinmeyenli denklem çözümü
# 5*x0 + x1 = 12
# x0 + 3*x1 = 10
a = np.array([[5, 1], [1, 3]])
b = np.array([12, 10])
np.linalg.solve(a, b)


