import pandas as pd

# low_memory=False ile CSV dosyasını oku
df = pd.read_csv('guncellenmis_train.csv', low_memory=False)
d = 'Bölüm'
# 'Universite Turu' sütununu büyük harfe çevir
df[d] = df[d].str.upper()

# Değişiklikleri yeni bir CSV dosyasına kaydet
df.to_csv('guncellenmis_train.csv', index=False)
