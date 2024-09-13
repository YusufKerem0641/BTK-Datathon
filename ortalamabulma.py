import pandas as pd

pd.set_option('display.max_rows', None)  # Tüm satırları göster
pd.set_option('display.max_columns', None)  # Tüm sütunları göster

# CSV dosyasını oku
df = pd.read_csv('guncellenmis_train.csv', low_memory=False) # 'veri.csv' dosyasının yolunu buraya ekleyin
df2 = pd.read_csv('test_x.csv', low_memory=False) # 'veri.csv' dosyasının yolunu buraya ekleyin
ortalama_ve_sayi2 = df2.groupby('Bölüm')
listeadi=ortalama_ve_sayi2.groups.keys()
# Her bölüm için 'değerlendirme puanı' ortalamasını hesapla
ortalama_ve_sayi = df.groupby('Bölüm').agg(
    Ortalama_Puan=('Degerlendirme Puani', 'mean'),
    Veri_Sayısı=('Degerlendirme Puani', 'count')
    )
filtrelenmis_veriler = ortalama_ve_sayi[ortalama_ve_sayi['Veri_Sayısı'] > 50]
ortalama_ve_sayi_sorted = filtrelenmis_veriler.sort_values(by='Ortalama_Puan', ascending=False)

# Sonuçları yazdır

for i in ortalama_ve_sayi_sorted.index:
    ortalama = ortalama_ve_sayi_sorted.at[i, 'Ortalama_Puan']  # Ortalamayı al
    if ortalama > 80:
        deger = "80 - 85"
    elif ortalama > 75:
        deger = "75 - 80"
    elif ortalama > 70:
        deger = "70 - 85"
    elif ortalama > 65:
        deger = "65 - 70"
    elif ortalama > 60:
        deger = "60 - 65"
    elif ortalama > 55:
        deger = "55 - 60"
    elif ortalama > 50:
        deger = "50 - 55"
    elif ortalama > 45:
        deger = "45 - 50"
    elif ortalama > 40:
        deger = "40 - 45"
    elif ortalama > 35:
        deger = "35 - 40"
    elif ortalama > 30:
        deger = "30 - 35"
    elif ortalama > 25:
        deger = "25 - 30"
    elif ortalama > 20:
        deger = "20 - 25"
    elif ortalama > 15:
        deger = "15 - 20"
    elif ortalama > 10:
        deger = "10 - 15"
    elif ortalama > 5:
        deger = "5 - 10"
    print(f"\'{i}\': \'{deger}\',")
    #for i2 in listeadi:
     #   if i2 in i:
      #      if i2 != i:
       #         print(f"\'{i2}\': \'{deger}\',")
print(ortalama_ve_sayi_sorted.sum())

