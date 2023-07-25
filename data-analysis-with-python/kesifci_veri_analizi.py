######################################
# GELİŞMİŞ FONKSİYONEL KEŞİFÇİ VERİ ANALİZİ (ADVANCED FUNCTİONAL EDA)
######################################

# 1. Genel Resim
# 2. Kategorik Değişken Analizi (Analysis of Categorical Variables)
# 3. Sayısal Değişken Analizi   (Analysis of numerical Variables)
# 4. Hedef Değişken Analizi     (Analysis of Target Variable)
# 5. Korelasyon Analizi         (Analysis of Correlation)

###################
# Genel Resim
###################

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = sns.load_dataset("titanic")

df.head()
df.tail()
df.shape  # satır, sütun sasyısı verir
df.info()
df.columns               # değişken isimlerini verir
df.index                 # index bilgisi verir
df.describe().T          # sayısal değişkenlerin betimsel verilerini (mean,std vs) verir
df.isnull().values.any() # eksik değer var mı yok mu
df.isnull.sum()          # eksik değer sayısı


# yukarıdaki özelliklerden ihtiyacımız olanlar doğrultusunda bir fonksiyon yazabiliriz

def check_df(dataframe, head=5):
    print("################### Shape ################")
    print(dataframe.shape)
    print("################### Types ################")
    print(dataframe.dtypes)
    print("################### Head ################")
    print(dataframe.head(head))
    print("################### Tail ################")
    print(dataframe.tail(head))
    print("################### NA ################")
    print(dataframe.isnull().sum())
    print("################### quantiles ################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)


check_df(df)


######################################
# Kategorik Değişken Analizi (Analysis of Categorical Variables) !!! önemli
######################################



import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = sns.load_dataset("titanic")

df.head()

df["embarked"].value_counts()
df["sex"].unique() # değişkenin benzersiz sınıflarını verir
df["sex"].nunique()# değişkenin sınıf sayısını verir

# amaç kategorik yani sınıfsal değişkenleri ayırt edebilmek
# kategorik değişkenler bool embark survived gibi sınıflara sahip olanlardır ama aralarında int olmasına rağmen sınıfsal olan survived gibi değişkenler var bunları da seçebilmemiz gerekiyor

# categoric değişken seçimi

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object","bool"]]

# cat olan ama num formunda olanları yakalama

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]
# 10 olması rastgeledir yapılan projeye göre değerlendirilebilir

#veri tipinde object ve kategorik tipte olan ama bir bilgi içermeyecek kadar fazla sınıf sayısına sahipse bunları eliyoruz(bunlara kardinal denir)


cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category""object"]]

cat_cols = cat_cols + num_but_cat
# cat_but_car boş küme çıktı eğer veri olsaydı onu cat_cols dan çıkarmalıydık
cat_cols = [col for col in cat_cols if col not in cat_but_car]

def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name:dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################################")

cat_summary(df,"sex")

for col in cat_cols:
    cat_summary(df, col)

# def fonksiyonuna yeni bir özellik ekleyelim ve grafik olarak ekrana yazdırsın
def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name:dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)# sütun grafik yapmaya yarar
        plt.show(block=True)

cat_summary(df, "sex",plot=True)

for col in cat_cols:
    if df[col].dtypes == "bool":
        print(f"{df[col].dtypes} grafiğe sahip değildir")
    else:
        cat_summary(df,col,plot=True)

## veya bool tipini es geçmek yerine onu integer değere dönüştürmeyi dneyebiliriz

for col in cat_cols:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
        cat_summary(df, col, plot=True)
    else:
        cat_summary(df,col,plot=True)



######################################
# Sayısal Değişken Analizi   (Analysis of numerical Variables)
######################################

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = sns.load_dataset("titanic")

df.head()

df[["age", "fare"]].describe().T

num_cols = [col for col in df.columns if df[col].dtypes in ["int64", "float64"]]

#bunların birkaçını kategoriklerle inceliyoruz bu yüzden;
num_cols = [col for col in num_cols if col not in cat_cols]

# yukarıdaki gibi bir çok verinin bilgisini almak istersek kolaylık açısından bir fonksiyon yazalım

def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)
    if plot:
        dataframe[numerical_col].hist()
        plt.show(block=True)
num_summary(df, "age")

for col in num_cols:
    num_summary(df, col, plot=True)



######################################
# Değişkenlerin Yakalanması Ve İşlemlerin Genelleştirilmesi
######################################


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = sns.load_dataset("titanic")

df.head()

#docstring

def grab_col_names(dataframe, cat_th=10, car_th=20):
    """
    veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir

    :param dataframe:dataframa
              Değişken isimlerinin alınmak istendiği dataframe'dir
    :param cat_th:   int, float
              numerik fakat kategorik olan değişkenler için sınıf eşik değeri
    :param car_th: int, float
              kategorik fakat kardinal değişkenler için sınıf eşik değeri
    :return:
        cat_cols: list
                kategorik değişken listesi
        num_cols: list
                numerik değişken listesi
        cat_but_car: list
                lategorik görünümlü kardinal değişken listesi

    Notes
    ------
    cat_cols + num_cols + cat_but_car= toplam değişken sayısı
    num_but_cat cat_cols'un içerisindedir.
    """

##Kategorik değişken seçim
    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]

    cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category""object"]]

    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

## numerik değişken seçim
    num_cols = [col for col in df.columns if df[col].dtypes in ["int64", "float64"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f"Observations:{dataframe.shape[0]}")
    print(f"Variables:{dataframe.shape[1]}")
    print(f"cat_cols:{len(cat_cols)}")
    print(f"num_cols:{len(num_cols)}")
    print(f"cat_but_car:{len(cat_but_car)}")
    print(f"num_but_cat:{len(num_but_cat)}")

    return cat_cols, num_cols, cat_but_car

cat_cols, num_cols, cat_but_car = grab_col_names(df)

def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name:dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################################")

cat_summary(df,"sex")

for col in cat_cols:
    cat_summary(df, col)



def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)
    if plot:
        dataframe[numerical_col].hist()
        plt.show(block=True)

for col in num_cols:
    num_summary(df, col, plot=True)

######################################
# hedef Değişken Analizi (Analysis of Target Variable)
######################################


df.groupby("sex")["survived"].mean()

def target_summary_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({"TARGET MEAN": dataframe.groupby(categorical_col)[target].mean()}))

target_summary_with_cat(df, "survived", "sex")

# burdan yorumla kadın olmanın hayatta kalma üzerinde etkisi olabilir diyebiliriz.

#elimizde kategorik değişkenler mevcıt olduğu için döngüyle gezelim

for col in cat_cols:
    target_summary_with_cat(df, "survived", col)



######################################
# hedef Değişkenin Sayısa Değişkenlerle Analizi
##################################

df.groupby("survived")["age"].mean()
# veya
df.groupby("survived").agg({"age":"mean"})

def target_summary_with_num(dataframe, target, numerical_col):
    print(pd.DataFrame(df.groupby(target).agg({numerical_col:"mean"})), end="\n\n\n")

target_summary_with_num(df, "survived", "age")

for col in num_cols:
    target_summary_with_num(df, "survived", col)


######################################
# Korelasyon Analizi (Analysis of Correlation)
##################################

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = pd.read_csv("C:/Users/atama/PycharmProjects/data_analysis_with_python/data.csv")
df = df.iloc[:, 1:-1]
df.head()

num_col = [col for col in df.columns if df[col].dtypes in [int, float]]

# korelasyon hesabı yapacağız. Korelasyon iki değişkenin birbiriyle ilişkisidir
# 1 ve -1 arasındadır 1 ve -1 e yaklaştıkça ilişki kuvvetlidir 0'a yaklaştıkça ilişki azalır
# yüksek kolerasyonlu veriler neredeyse birbirinin aynısı anlamına geldiği için genellikle biri çalışmadan silinir

corr = df[num_col].corr()

sns.set(rc={"figure.figsize": (12, 12)})
sns.heatmap(corr, cmap="RdBu")
plt.show(block=True)

# koyu mavi pozitif güçlü kolerasyon kırmızı negatif güçlü kolerasyon

######################################
# Yüksek Kolerasyonlu Değişkenlerin Silinmesi
##################################

# her projede olmasa da bazı projelerde bu uygulama gereklidir

#korelasyonların yönüyle ilgilenmediğimiz için hepsini mutlak değere alıyoruz

cor_matrix = df.corr(numeric_only=True).abs()

#çıktı matrisi köşegene göre simetrik olacak şekilde aynı verileri veriyor bu yüzden üst üçgensel matris yapıyoruz

upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool_))

# sütunlardaki elemanlardan herhangi biri %90 dan büyükse onu silen bir fonksiyon yazalım(%90ı biz belirledik

drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col]>0.90)]
cor_matrix[drop_list]
df.drop(drop_list, axis=1)

def high_correlated_cols(dataframe, plot=False, corr_th=0.90):
    corr = dataframe.corr()
    cor_matrix = corr.abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool_))
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > corr_th)]
    if plot:
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.set(rc={"figure.figsize": (15, 15)})
        sns.heatmap(corr, cmap="RdBu")
        plt.show(block=True)
    return drop_list

high_correlated_cols(df)

drop_list = high_correlated_cols(df, plot=True)
df.drop(drop_list, axis=1)
high_correlated_cols(df.drop(drop_list, axis=1), plot=True)


