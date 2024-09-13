import pandas as pd

# CSV dosyasını oku
df = pd.read_csv('test_x.csv', low_memory=False)

# 'Universite Turu' sütunu 'devlet' olan satırlarda 'burs' sütununu 'd' olarak güncelle
df.loc[df['Universite Turu'].str.contains('DEVLET', case=False, na=False), 'Burslu ise Burs Yuzdesi'] = 999

# Temizlenmiş verileri yeni bir CSV dosyasına kaydet
df.to_csv('guncellenmis_train.csv', index=False)

print("Güncellenmiş veri 'guncellenmis_train.csv' dosyasına kaydedildi.")
