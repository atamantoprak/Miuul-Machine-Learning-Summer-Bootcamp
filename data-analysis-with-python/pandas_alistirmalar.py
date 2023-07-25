#### 1 ####
# titanic veri setini tanımla
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = sns.load_dataset("titanic")
df.head()

#### 2 ####
# titanic veri setindeki kadın ve erkek yolcuların sayısın bulunuz

df["sex"].value_counts()
df["sex"].value_counts()["male"]

#### 3 ####
# her bir sütuna ait unique değerlerin sayısını bulunuz.
df.nunique()

[df[col].nunique() for col in df.columns]

#### 1 ####
# pclass değikeninin unique değerlerinin sayısını bulunuz

df['pclass'].nunique()

df.pclass.unique()
#### 5 ####
# pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz

df[["pclass", "parch"]].nunique()

#### 6 ####
# embarked değişkeninin tipini kontrol ediniz. tipini category olarak değiştiriniz ve tekrar kontrol ediniz
#az sayıda unique değerden oluşan string tipinde bir değişken var ise veri tipini category olarak değişltirmek bellek avantajı ve işlem hızı sağlar

df["embarked"].dtype
df["embarked"] = df["embarked"].astype("category")
df["embarked"].dtypes

#### 7 ####
# Embarked değeri C olanların tüm bilgilerini gösteriniz
df.loc[df["embarked"] == "C"]
# veya
df[df["embarked"] == "C"]

#### 8 ####
# embarked değeri S olmayanların tüm bilgilerini gösteriniz
df.loc[df["embarked"] != "C"]
#veya
df[~(df["embarked"] == "C")]



#### 9 ####
# Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz
df.loc[(df["age"] < 30) & (df["sex"] == "female")]
#veya
df[(df["age"] < 30) & (df["sex"]== "female")]

#### 10 ####
#Fare değeri 500 den büyük olan veya yaşı 70 den büyük olan yolcuların bilgilerini gösteriniz

df.loc[(df["fare"] > 500) | (df["age"] > 70)]

#### 11 ####
# her bir değişkendeki boş değerlerin toplamını bulunuz

df.isnull().sum()


#### 12 ####
# who değişkenini dataframe den çıkarınız
df.drop("who",axis=1).head()

#### 13 ####
# Deck değişkeninin boş değerlerini deck değişkeninin en çok tekrar eden değeriyle (mod) doldurun

df["deck"].fillna(df["deck"].mode()[0], inplace=True)

#### 14 ####
# age değişkenindeki boş değerleri değişkenin medyanı ile doldurun

df["age"] = df["age"].fillna(df["deck"].median())

#### 15 ####
# survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerinibulunuz.
df.groupby(["pclass","sex"]).agg({"survived":["mean","sum","count"]})

#### 16 ####
# 30 yaşından küçük olanlara 1, yaşı 30'a eşit olanlara 0 verecek bir fonksiyon yazın bu fonksiyonu kullanarak titanic veri setinde age_flag adında bir değişken oluşturunz(apply ve lambda fonk kullan)

df["age_flag"] = df["age"].apply(lambda x: 1 if x <30 else 0)
df.head()
#### 17 ####
#Seaborn veri seti içerisinden Tips veri setini tanımlayınız

df= sns.load_dataset("tips")

#### 18 ####
#Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.

df.groupby("time").agg({"total_bill":[ "min","max","mean"]})
# df.groupby("time")["total_bill"].agg(["sum","min","max","mean"])

#### 19 ####
# Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz

df.groupby(["day","time"]).agg({"total_bill": [ "sum", "min","max","mean"]})

#### 20 ####
# Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz

df_female_lunch = df[(df['time'] == 'Lunch') & (df['sex'] == 'Female')]
df_female_lunch.groupby('day').agg({'total_bill': ['sum', 'min', 'max', 'mean', 'count'], 'tip': ['sum', 'min', 'max', 'mean', 'count']})

#### 21 ####
#size'i3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)

df.loc[(df["size"]< 3) & (df["total_bill"] > 10), "total_bill"].mean()

#### 22 ####
# total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin

df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
df.head()

#### 23 ####
# total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni birdata frame'e atayınız

df_top30 = df.sort_values(by="total_bill_tip_sum", ascending=False).head(30)

 #df.sort_values(by='total_bill_tip_sum', ascending=False).iloc[:30]

