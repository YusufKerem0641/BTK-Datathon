import pandas as pd

input_file = r'sonuc1.csv'
output_file = 'sonuc.csv'

# Orijinal CSV dosyasını oku
df = pd.read_csv(input_file, low_memory=False)

# 'Neural Network (2)' sütununu sayısal değerlere dönüştür (hataları NaN yapar)
df['Neural Network (2)'] = pd.to_numeric(df['Neural Network (2)'], errors='coerce')

# NaN değerleri 0 ile değiştir
df['Neural Network (2)'] = df['Neural Network (2)'].fillna(0)

# Negatif değerleri 0 ile değiştir
df['Neural Network (2)'] = df['Neural Network (2)'].clip(lower=0)

# Değişiklikleri yeni CSV dosyasına kaydet
df.to_csv(output_file, index=False)

print(f"{output_file} dosyası başarıyla oluşturuldu.")
