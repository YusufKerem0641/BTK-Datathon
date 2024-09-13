import pandas as pd
import re

# Sadece harfleri tutan bir fonksiyon tanımlayın
def sadece_harfler(text):
    if isinstance(text, str):
        # Sadece harfleri tutan, geri kalan her şeyi çıkaran regex
        return re.sub('[^a-zA-Z]', '', text)
    return text  # Eğer değer string değilse, olduğu gibi döndür

ceviri_tablosu = str.maketrans("ÇŞçşĞğİiüÜöÖ", "CScsGgIiuUoO")

# Harf çevirme fonksiyonu
def ingilizce_harften_turkceye(adi):
    if isinstance(adi, str):  # Eğer değer bir string ise
        return adi.translate(ceviri_tablosu)
    return adi  # Eğer string değilse, olduğu gibi döndür

# CSV dosyasını oku
df = pd.read_csv('guncellenmis_train.csv',low_memory=False)

# Hangi sütun üzerinde işlem yapmak istiyorsanız onu seçin
sutun = 'Lise Bolumu'
df[sutun] = df[sutun].apply(ingilizce_harften_turkceye)
# Seçili sütundaki harf olmayan her şeyi çıkarın
df[sutun] = df[sutun].apply(sadece_harfler)

# Güncellenmiş veriyi yeni bir CSV dosyasına kaydet
df.to_csv('guncellenmis_train.csv', index=False)

print("Harf olmayan karakterler çıkarıldı ve yeni dosyaya kaydedildi.")
