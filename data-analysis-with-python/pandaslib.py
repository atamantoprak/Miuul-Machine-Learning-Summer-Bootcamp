
##############################
# Pandas Series
##############################

import pandas as pd

s = pd.Series([10, 77, 12, 4, 5])
type(s)

s.index
s.dtype
s.size
s.ndim
s.values
type(s.values) # sonuna values yazdık ve indexle ilgilenmediğimizi belirttiğimiz için numpy array olarak döndürdü dikkat
s.head()       # ilk 5 veriyi verir içine farklı rakamlar yazılabilir
s.tail(3)      # Sondan başlayarak veri verir

##############################
# Veri Okuma (reading data)
##############################
import pandas as pd

# örneğin dış bir dosyayı okumak istiyorsak (csv, excel, html her türden olabilir) aşağıdaki gibi read ile yapılır. Diğer türler için pd üzerine gelip ctrl click yap aramaya read yaz
pd.read_csv("")

##############################
# Veriye Hızlı Bakış (Quick Look at Data)
##############################
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
df.shape
df.info()
df.columns
df.index
df.describe().T          # sondaki .T Transpozunu al demektir
df.isnull().values.any() # df değerlerinde hiç eksiklik  var mı
df.isnull().sum()
df["sex"].head()
df["sex"].value_counts()

##############################
# Pandas seçim işlemleri (selection in Pandas) önemli!!!!
##############################

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

df[0:13]
df.drop(0, axis=0).head()  #satırlardan 0. indexi sil

# fazla index seçimi yapmak için

delete_indexes = [1, 2, 3, 4]
df.drop(delete_indexes, axis=0).head(10)
#!! şuan atamadığımız için değişiklik kalıcı değil
# 1. yöntem
df = df.drop(delete_indexes, axis=0)
# 2. yöntem
df.drop(delete_indexes, axis=0, inplace=True)  #önemli bir çok metodla inplace kullanılabilir


##############################
# Değişkeni Indexe çevirmek
##############################

df["age"].head()
df.age.head()
df.index
df.index = df["age"]
df.drop("age",axis=1, inplace=True) # age artık bir index olarak eklendiği için değişkenlerden silebiliriz ve satıra ekledik sütundan silmeliyiz o yüzden axix=1 olmalı



##############################
# indexi değişkene çevirmek
##############################
#1.yol
df.index
df["age"] = df.index
df.head()
df.drop("age",axis=1, inplace=True) # tekrar sildik 2. yolu denicez

# 2. yol

df.reset_index().head() # indexte yer alan değeri sildi ve değişken olarak bir sütuna ekledi
df = df.reset_index()

##############################
# Değişkenler Üzerinde İşlemler
##############################
import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None) # 3 nokta olan yerleri tam gösterir noktaları kaldırır
df = sns.load_dataset("titanic")
df.head()

#... değişkeni dataframe içinde var mı yazımları
"age" in df
df["age"].head()
df.age.head()

## çok önemli not
type(df["age"].head())
#typeına bakınca pandas serisi olduğunu gördük ama bunun dataframe olarak kalmasını istersek çift köşeli parantez kullanırız

type(df[["age"]].head())

df[["age", "alive"]]

col_names = ["age","adult_male", "alive"]
df[col_names]

# değişken ekleme

df["age2"] = df["age"]**2
# bir değişken daha ekleyelim

df["age3"] = df["age"] / df["age2"]

# Değişken silme

df.drop("age3", axis=1).head() # head kullanıldığında sadece silinmiş gibi ekrana bastırılır ama bunu kaydetmek için head silinip axisten sonra inplace = True yazılmalı

# ÖNEMLİ / Belirli bir seçime göre seçme silme işlemi yapılmak isteniyorsa

df.loc[:, df.columns.str.contains("age")].head() # :, ifadesi tüm satırları seç demektir
# yazdırdığımızda içerisinde age geçen tüm değişkenleri buldu.
df.loc[:, ~df.columns.str.contains("age")].head()  # "age" içermeyenleri yazdır anlamına gelir


##############################
# iloc & loc (integer based selection & label based selection)
##############################


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()
sns.countplot(x="class", data=df)
plt.show(block=True)

# iloc: integer based selection(index bazlı çalışır)
df.iloc[0: 3] # sıfırdan 3. indexe kadar olan verileri alır

df.iloc[0, 0] # matriks olarak 0,0 ı aldı

# loc: label based selection

df.loc[0:3] # bu 3. indexi de aldı çünkü etiket olarak gördüğü 3ü de alır

df.iloc[0:3, 0:3]

df.loc[0:3, "age"]

col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names] # fancy

##############################
# Koşullu Seçim (conditional Selection)
##############################

import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

df["sex"].describe()

df[df["age"] > 50].head()
df[df["age"] > 50].count() # hepsine count attı
df[df["age"] > 50]["age"].count() # böyle yapınca sadece yaşı 50den büyük olan kaç kişi var onu öğrendik,

df.loc[df["age"] > 50, ["age","class"]].head()
df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age","class"]].head()# çift koşul yaşı 50 den büyük olanlar ve erkek olanları seçer
df.loc[(df["age"] > 50)
       & (df["sex"] == "male")
       & (df["embark_town"] == "Cherbourg"),
       ["age","class","embark_town"]].head()

df["embark_town"].value_counts()
#sadece southampton ve cherbourg olanları seç
df.loc[(df["age"] > 50)
       & (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
       ["age","class","embark_town"]].head()


##############################
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
##############################
# count()
# first()
# last()
# mean()
# median()
# min()
# max()
# std()
# var()
# sum()
# pivot table

import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

df["age"].mean() # yaş ortalaması

df.groupby("sex")["age"].mean()# df data frameini cinsiyete göre grupla ve yaş ortalamasını al anlamına gelir

df.groupby("sex").agg({"age": "mean"}) # bir üstteki amaçla aynı ama daha çok tercih edilmeli
df.groupby("sex").agg({"age":["mean", "sum"]})

df.groupby("sex").agg({"age": ["mean","sum"],
                       "survived": "mean"})
# survivedin ortalamasını aldık female 0.7 olduğu için kadınların %70 i hayattadır diyebiliriz

df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"],
                                                 "survived": "mean"})

df.groupby(["sex", "embark_town", "class"]).agg({
    "age": ["mean"],
    "survived": "mean",
    "sex": "count"})




##############################
# Pivot Table
##############################
# groupby a benzer

import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

df.pivot_table("survived","sex","embarked") # ilki değerler, 2. satır başlıkları 3. sütun başlıkları
df.pivot_table("survived","sex","embarked", aggfunc="std") # bir öncekinde değerleri mean olarak aldı burda standart sapma almasını belirttik

df.pivot_table("survived","sex", ["embarked", "class"])# satırlar tek index sütun başlıkları 2 indexli olmuş oldu

df["new_age"] = pd.cut(df["age"],[0, 10, 18, 25, 40, 90])  # sayısal bir değişkeni kategorik bir değişkene çevirmek için kullanılır örn yaş: 0-10 arası çocuk diye ayırabilecek kadar tanıyorsan yaş değişkenini,cut kullan ama değişken hakkında bilgib yoksa qcut kullan çeyrek olarak ayırır( neyi böleceğimi ver, nerelerden böleceğimi ver )

df.pivot_table("survived", "sex","new_age")
df.pivot_table("survived", "sex",["new_age","class"])
#son kod çıktısında satır sonunda bulunan ters slash çıktının alttan devam ettiğini söyler. Eğer çıktıyı yan yana istersek alttaki kodu yaz

pd.set_option('display.width',500)


##############################
# Apply ve Lambda
##############################
# apply ile satır yada sütunlarda otomatik olarak fonksiyon çalıştırmaya yarar

import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

# değişkenler üzerinde işlemler yapmak istediğimizi varsayalım
(df["age"]/10).head()
(df["age2"]/10).head()

for col in df.columns:
    if "age" in col:
        print(col)

for col in df.columns:
    if "age" in col:
        df[col] = df[col] / 10

df.head()
# for ile yapmak uzun yoldu şimdi apply ile yapalım
df[["age", "age2", "age3"]].apply(lambda x: x / 10).head()

# ya da
df.loc[:,df.columns.str.contains("age")].apply(lambda x: x / 10).head()

# apply ile def fonksiyonu da kullanılabilir sadece lambda değil

#kaydetmedik kaydedelim

df.loc[:, df.columns.str.contains("age")] = df.loc[:,df.columns.str.contains("age")].apply(lambda x: x / 10)
df.head()



##############################
# Birleştirme (join) işlemleri
##############################

import pandas as pd
import  numpy as np

m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99
# iki adet dataframe oluşturduk

pd.concat([df1, df2])
# bir üstteki işlemde indexler sıfırlanıp tekrar arttı bunun için;
pd.concat([df1, df2],ignore_index=True)
# axise default olarak 0 atandığı için alt alta birleştirme yapar


##############################
# Merge ile Birleştirme
##############################

df1= pd.DataFrame({"employees": ["john", "dennis", "mark", "maria"],
                   "group": ["accounting", "engineering", "engineering", "hr"]})

df2= pd.DataFrame({"employees": ["john", "dennis", "mark", "maria"],
                   "start_date": [2010, 2009, 2014, 2019]})

pd.merge(df1, df2)
# direkt employeese göre yaptı ama belirtmek istersek
pd.merge(df1, df2, on="employees")


# Amaç her çalışanın müdür bilgisine ulaşmak istiyoruz
df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({"manager": ["caner", "mustafa", "berkcan"],
                   "group": ["accounting", "engineering", "hr"]})
pd.merge(df3, df4) # farklı iki dataframe birleştirildi groupa göre yaptı bunu çünkü ortak olan o