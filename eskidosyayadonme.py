import pandas as pd

# CSV dosyalarını oku
df_train = pd.read_csv(r"train.csv", low_memory=False)
df_guncellenmis = pd.read_csv('guncellenmis_train.csv', low_memory=False)

# 'Universite Not Ortalamasi' sütunundaki tüm değerleri güncelle
sutun = 'Basvuru Yili'

# Satır sayıları eşleşiyorsa, sütunu tamamen kopyala
if len(df_train) == len(df_guncellenmis):
    df_guncellenmis[sutun] = df_train[sutun].values
    print(f"'{sutun}' sütunu başarıyla güncellendi.")
else:
    print(f"Uyarı: Satır sayıları eşleşmiyor! df_train: {len(df_train)} satır, df_guncellenmis: {len(df_guncellenmis)} satır.")

# Temizlenmiş veriyi yeni bir CSV dosyasına kaydet
df_guncellenmis.to_csv('guncellenmis_train.csv', index=False)

print("Güncellenmiş veri 'guncellenmis_train.csv' dosyasına kaydedildi.")
