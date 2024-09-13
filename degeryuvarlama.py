import pandas as pd
import numpy as np

# CSV dosyasını oku
df = pd.read_csv('guncellenmis_train.csv', low_memory=False)

# 'burs' sütunundaki değerleri sayısal hale getir
df['Burslu ise Burs Yuzdesi'] = pd.to_numeric(df['Burslu ise Burs Yuzdesi'], errors='coerce')

# Yuvarlama fonksiyonunu tanımla
def yuvarla_burs(deger):
    if deger == 999:
        return deger
    else:
        return min([0, 25, 50, 100], key=lambda x: abs(x - deger))

# 'burs' sütunundaki değerleri yuvarla
df['Burslu ise Burs Yuzdesi'] = df['Burslu ise Burs Yuzdesi'].apply(yuvarla_burs)

# Temizlenmiş verileri yeni bir CSV dosyasına kaydet
df.to_csv('guncellenmis_train.csv', index=False)

print("Güncellenmiş veri 'guncellenmis_train.csv' dosyasına kaydedildi.")
