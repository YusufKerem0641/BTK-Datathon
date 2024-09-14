import pandas as pd

# CSV dosyasını oku
df = pd.read_csv('guncellenmis_train.csv', low_memory=False)
sutun = 'Basvuru Yasi'
# Bölüm sütunundaki her bir değerin kaç kere tekrarlandığını bul
frekanslar = df[sutun].value_counts()

# 140'tan az olan değerleri tespit et
az_bulunanlar = frekanslar[frekanslar < 55].index

# 140'tan az bulunan değerleri "Diğer" ile değiştir
df[sutun] = df[sutun].replace(az_bulunanlar, 'Gelecekten')

# Güncellenmiş verileri yeni bir CSV dosyasına kaydet
df.to_csv('guncellenmis_train.csv', index=False)

print("140'tan az bulunan değerler 'Diğer' olarak değiştirildi ve dosya kaydedildi.")
