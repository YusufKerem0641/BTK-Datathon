import pandas as pd

# CSV dosyasını oku
df = pd.read_csv('guncellenmis_train.csv', low_memory=False)

sutun = 'Burs Aldigi Baska Kurum'

# 'Burs Aldigi Baska Kurum' sütunundaki değerlerde 'KYK' kelimesi geçiyorsa 'KYK' olarak güncelle
df[sutun] = df[sutun].apply(lambda x: 'TIP' if 'KREDI VE YURTLAR' in str(x).upper() else x)

# Temizlenmiş verileri yeni bir CSV dosyasına kaydet
df.to_csv('guncellenmis_train.csv', index=False)

print("Temizlenmiş veri 'guncellenmis_train.csv' dosyasına kaydedildi.")
