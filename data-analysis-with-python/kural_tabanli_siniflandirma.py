#############################################
# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
#############################################

#############################################
# İş Problemi
#############################################
# Bir oyun şirketi müşterilerinin bazı özelliklerini kullanarak seviye tabanlı (level based) yeni müşteri tanımları (persona)
# oluşturmak ve bu yeni müşteri tanımlarına göre segmentler oluşturup bu segmentlere göre yeni gelebilecek müşterilerin şirkete
# ortalama ne kadar kazandırabileceğini tahmin etmek istemektedir.

# Örneğin: Türkiye’den IOS kullanıcısı olan 25 yaşındaki bir erkek kullanıcının ortalama ne kadar kazandırabileceği belirlenmek isteniyor.


#############################################
# Veri Seti Hikayesi
#############################################
# Persona.csv veri seti uluslararası bir oyun şirketinin sattığı ürünlerin fiyatlarını ve bu ürünleri satın alan kullanıcıların bazı
# demografik bilgilerini barındırmaktadır. Veri seti her satış işleminde oluşan kayıtlardan meydana gelmektedir. Bunun anlamı tablo
# tekilleştirilmemiştir. Diğer bir ifade ile belirli demografik özelliklere sahip bir kullanıcı birden fazla alışveriş yapmış olabilir.

# Price: Müşterinin harcama tutarı
# Source: Müşterinin bağlandığı cihaz türü
# Sex: Müşterinin cinsiyeti
# Country: Müşterinin ülkesi
# Age: Müşterinin yaşı

################# Uygulama Öncesi #####################

#    PRICE   SOURCE   SEX COUNTRY  AGE
# 0     39  android  male     bra   17
# 1     39  android  male     bra   17
# 2     49  android  male     bra   17
# 3     29  android  male     tur   17
# 4     49  android  male     tur   17

################# Uygulama Sonrası #####################

#       customers_level_based        PRICE SEGMENT
# 0   BRA_ANDROID_FEMALE_0_18  1139.800000       A
# 1  BRA_ANDROID_FEMALE_19_23  1070.600000       A
# 2  BRA_ANDROID_FEMALE_24_30   508.142857       A
# 3  BRA_ANDROID_FEMALE_31_40   233.166667       C
# 4  BRA_ANDROID_FEMALE_41_66   236.666667       C


#############################################

import pandas as pd

# persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösterelim

df = pd.read_csv("datasets/persona.csv")
df.head()

# Kaç unique SOURCE vardır? Frekansları nedir?

df["SOURCE"].nunique()
df["SOURCE"].value_counts()

# Kaç unique PRICE vardır?

df["PRICE"].nunique()

#Hangi PRICE'dan kaçar tane satış gerçekleşmiş?

df["PRICE"].value_counts()

# Hangi ülkeden kaçar tane satış olmuş?

df["COUNTRY"].value_counts()

# Ülkelere göre satışlardan toplam ne kadar kazanılmış?

df.groupby("COUNTRY").agg({"PRICE": "sum"})

df.groupby("SOURCE")["SOURCE"].count()
#veya df.SOURCE.value_counts()

# Ülkelere göre PRICE ortalamaları nedir?

df.groupby("COUNTRY").agg({"PRICE": "mean"})

# SOURCE'lara göre PRICE ortalamaları nedir?

df.groupby("SOURCE")["PRICE"].mean()

# COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?

df.groupby(["COUNTRY","SOURCE"]).agg({"PRICE": "mean"})

# COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?

liste=["COUNTRY", "SOURCE", "SEX", "AGE"]
agg_df = df.groupby(liste).agg({"PRICE": "mean"})

# Çıktıyı PRICE'a göre sıralayalım

agg_df.sort_values(by="PRICE", ascending=False)

# Indekste yer alan isimleri değişken ismine çevirelim

agg_df = agg_df.reset_index()

# AGE değişkenini kategorik değişkene çevirip agg_df'e ekleyelim

agg_df["AGE_CUT"] = pd.cut(agg_df["AGE"], bins = [0, 18, 23, 30, 40, agg_df["AGE"].max()], labels=["0-18","19-23","24-30","31-40","41-"+ str(agg_df["AGE"].max())])


#Yeni level based müşterileri tanımlayalım ve veri setine değişken olarak ekleyelim.

agg_df.drop(['AGE', 'PRICE'], axis=1).values

# bu metod harfler arasına verilen string ifadeyi ekler

liste = ['A', 'B', 'C']
'-'.join(liste)

# ilk yöntem
agg_df["CUSTOMER_LEVEL_BASED"] = ["_".join(i).upper() for i in agg_df.drop(['AGE', 'PRICE'], axis=1).values]

#2. yöntem
# agg_cols=["COUNTRY","SOURCE","SEX","AGE_CAT"]
# [col[0].upper()+"_"+col[1].upper()+"_"+col[2].upper()+"_"+col[3].upper() for col in agg_df[agg_cols].values ]

#3. yöntem

# agg_df['COUNTRY'].astype(str) + "_" + \
# agg_df['SOURCE'].astype(str) + "_" + \
# agg_df['SEX'].astype(str) + "_" + \
# agg_df['AGE_CAT'].astype(str)
agg_df.head()

# Gereksiz değişkenleri çıkaralım:

agg_df = agg_df[["CUSTOMER_LEVEL_BASED", "PRICE"]]
agg_df = agg_df.groupby('CUSTOMER_LEVEL_BASED')['PRICE'].mean().reset_index()

# Yeni müşterileri (USA_ANDROID_MALE_0_18) segmentlere ayıralım.

agg_df['SEGMENT'] = pd.qcut(agg_df.PRICE, q=4, labels=['D', 'C', 'B','A'])
agg_df.head()

agg_df.groupby('SEGMENT').agg({'PRICE': 'mean'}).reset_index()

# Yeni gelen müşterileri sınıflandıralım ne kadar gelir getirebileceğini tahmin edelim
#33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?

new_user = 'TUR_ANDROID_FEMALE_31-40'

agg_df[agg_df['CUSTOMER_LEVEL_BASED'] == new_user]
