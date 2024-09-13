import pandas as pd

sutun = 'Dogum Tarihi'
# low_memory=False ile CSV dosyasını oku
df = pd.read_csv('test_x.csv', low_memory=False)

# 'Universite Turu' sütunundaki benzersiz değerleri ve frekanslarını göster
universite_turu_degerleri = df[sutun].value_counts()

# Sonuçları yazdır
print(universite_turu_degerleri.head(60))
df2 = pd.read_csv(r'guncellenmis_train.csv', low_memory=False)

# 'Universite Turu' sütunundaki benzersiz değerleri ve frekanslarını göster
universite_turu_degerleri2 = df2[sutun].value_counts()

# Sonuçları yazdır
print(universite_turu_degerleri2.head(60))
