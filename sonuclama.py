import pandas as pd

# Orijinal CSV dosyasının yolu
input_file = r'sonuc.csv'

# Çıkış CSV dosyasının yolu
output_file = 'sonuc1.csv'

# Orijinal CSV dosyasını oku
df = pd.read_csv(input_file, low_memory=False)

# İstenilen sütunları seç (örneğin 'sütun1' ve 'sütun2')
selected_columns = df[['id', 'Degerlendirme Puani']]

# Yeni CSV dosyasına yaz
selected_columns.to_csv(output_file, index=False)

print(f"{output_file} dosyası başarıyla oluşturuldu.")
