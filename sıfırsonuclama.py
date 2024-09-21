import pandas as pd

# CSV dosyasını oku
df = pd.read_csv('sonuc1.csv')

# "Degerlendirme Puani" sütunundaki verileri sayısal değerlere dönüştür
df['Degerlendirme Puani'] = pd.to_numeric(df['Degerlendirme Puani'], errors='coerce')

# Negatif değerleri 0 yap
df['Degerlendirme Puani'] = df['Degerlendirme Puani'].apply(lambda x: max(x, 0))

# Güncellenmiş veriyi yeni bir CSV dosyasına kaydet
df.to_csv('sonuc1.csv', index=False)

print("Negatif değerlendirme puanları 0'a güncellendi ve dosya kaydedildi.")
