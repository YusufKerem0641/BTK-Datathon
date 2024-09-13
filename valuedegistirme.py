import pandas as pd

# CSV dosyasını oku
df = pd.read_csv('guncellenmis_train.csv', low_memory=False)

sutun= 'Basvuru Yasi'

# Lise Turu sütunundaki benzer değerleri düzeltmek için bir eşleştirme yap
df[sutun] = df[sutun].replace({
"50.0":"Gelecekten",
"51.0" : "Gelecekten",
})

# Temizlenmiş verileri yeni bir CSV dosyasına kaydet
df.to_csv('guncellenmis_train.csv', index=False)

print("Temizlenmiş veri 'guncellenmis_train.csv' dosyasına kaydedildi.")
