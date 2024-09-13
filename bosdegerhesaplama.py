import pandas as pd

# CSV dosyasını yükleyin
df = pd.read_csv('test_x.csv')

# 'sutun_adi' sütunundaki boş (NaN) değerlerin sayısını hesaplayın
bos_deger_sayisi = df['Daha Önceden Mezun Olunduysa, Mezun Olunan Üniversite'].isna().sum()

print(f"'sutun_adi' sütunundaki boş değer sayısı: {bos_deger_sayisi}")
