import pandas as pd

sutun = 'Degerlendirme Puani (error)'
# low_memory=False ile CSV dosyasını oku
df = pd.read_csv('hatali_train.csv', low_memory=False)

# Sayı olmayan değerleri NaN ile doldurma (temizleme)
df[sutun] = pd.to_numeric(df[sutun], errors='coerce')

# NaN değerleri sıfırla doldurma (veya başka uygun bir değer)
df[sutun].fillna(0, inplace=True)

high_error_ids = df[df[sutun] > 20]['id'].tolist()
eksi_high_error_ids = df[df[sutun] < -20]['id'].tolist()

high_error_ids = high_error_ids + eksi_high_error_ids
# Sonuçları yazdırma
print(high_error_ids)

df = pd.read_csv(r'guncellenmis_train.csv', low_memory=False)

# 'high_error_ids' listesindeki id değerlerine sahip satırları sil
df = df[~df['id'].isin(high_error_ids)]

# Güncellenmiş veriyi kaydet
df.to_csv('guncellenmis_train.csv', index=False)

print("sildi")

