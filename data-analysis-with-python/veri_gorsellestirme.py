#########################
# VERİ GÖRSELLEŞTİRME: MATPLOTLIB & SEABORN
#########################

#########################
# MATPLOTLIB
#########################

# Kategorik değişken: sütun grafik. countplot bar
# Sayısal değişken: hist, boxplot


#########################
# Kategorik değişken görselleştirme
#########################

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")

df.head()

df["sex"].value_counts().plot(kind="bar")
plt.show(block=True)

#########################
# sayısal değişken görselleştirme
#########################



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head()

plt.hist(df["age"])
plt.show(block=True)

plt.boxplot(df["fare"])
plt.show(block=True)
# kutu grafik genel dağılımın dışındaki verileri yakalar

#########################
# matplotlibin Özellikleri
#########################



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)


#########################
# plot
#########################

x = np.array([1, 8])
y = np.array([0, 150])
plt.plot(x, y)
plt.show(block=True)

plt.plot(x, y, "o")
plt.show(block=True)


#########################
# marker
#########################

y = np.array([13, 28, 11, 100])

plt.plot(y, marker="*")
plt.show(block=True)

#########################
#Line
#########################


y = np.array([13, 28, 11, 100])

plt.plot(y, linestyle="dotted", color="r")
plt.show(block=True)


#########################
# Multiple Lines
#########################
x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])

plt.plot(y, linestyle="dotted", color="r")
plt.plot(x)
plt.show(block=True)


#########################
# Labels
#########################

x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])
plt.plot(x, y)
# Ana Başlık
plt.title("Bu Ana Başlık")
plt.show(block=True)

# x eksenini isimlendirme

plt.xlabel("x ekseni ismi")

plt.ylabel("y ekseninin ismi")

plt.grid()
plt.show(block=True)

#########################
# Subplots
#########################

#plot 1

x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])

plt.subplot(1, 2, 1) # 1 satır 2 sütundan oluşan bir grafik yap ve bu 1. grafik anlamında bir yazımdır
plt.title("1")
plt.plot(x, y)


# plot 2

x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])

plt.subplot(1, 2, 2) # 1 satır 2 sütundan oluşan bir grafik yap ve bu 2. grafik anlamında bir yazımdır
plt.title("2")
plt.plot(x, y)
plt.show(block=True)


#########################
# SEABORN
#########################


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset("tips")
df.head()

df["sex"].value_counts()
sns.countplot(x=df["sex"], data=df)  # ilk argüman görselleştirmek istediğimiz değişkenin adı 2. ise veri seti ve bunları bir değişkene eşitlemelisin
plt.show(block=True)

# matplotlible şöyle

df["sex"].value_counts().plot(kind="bar")
plt.show(block=True)

#########################
# Sayısal değişken görselleştirme
#########################

sns.boxplot(x= df["total_bill"])
plt.show(block=True)

