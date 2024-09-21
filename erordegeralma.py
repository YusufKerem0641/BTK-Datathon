import pandas as pd

sutun = 'Degerlendirme Puani (error)'
# low_memory=False ile CSV dosyasını oku
df = pd.read_csv('hatali_train.csv', low_memory=False)

# Sayı olmayan değerleri NaN ile doldurma (temizleme)
df[sutun] = pd.to_numeric(df[sutun], errors='coerce')

# NaN değerleri sıfırla doldurma (veya başka uygun bir değer)
df[sutun].fillna(0, inplace=True)

# Hatalı puanı yüksek olan ID'leri alma
high_error_ids = df[df[sutun] > 25]['id'].tolist()
eksi_high_error_ids = df[df[sutun] < -25]['id'].tolist()

high_error_ids = high_error_ids + eksi_high_error_ids

# ID'leri yazdırarak kontrol et
print(f"High error len: {len(high_error_ids)} IDs: {high_error_ids}")

# Güncellenmiş CSV dosyasını oku
df = pd.read_csv(r'guncellenmis_train.csv', low_memory=False)

# 'high_error_ids' listesindeki id değerlerine sahip satırları sil
df['id'] = df['id'].astype(str)
high_error_ids = [str(i) for i in high_error_ids]
df = df[~df['id'].isin(high_error_ids)]

# Güncellenmiş veriyi kaydet
df.to_csv('guncellenmis_train.csv', index=False)

print("İşlem tamam, dosya başarıyla güncellendi.")
