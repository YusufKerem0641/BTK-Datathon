import pandas as pd
import re


# Baştaki ve sondaki harf olmayan her şeyi silen, fazla boşlukları düzelten fonksiyon
def temizle(text):
    if isinstance(text, str):
        # Baştaki ve sondaki harf olmayan karakterleri sil
        text = re.sub(r'^[^a-zA-ZığüşöçĞÜŞÖÇİ]+|[^a-zA-ZığüşöçĞÜŞÖÇİ]+$', '', text)

        # Fazla boşlukları tek boşluğa indir
        text = re.sub(r'\s+', ' ', text).strip()

        return text
    return text


# CSV dosyasını oku
df = pd.read_csv('test_x.csv', low_memory=False)

# Tüm sütunlara temizleme fonksiyonunu uygula
df = df.apply(lambda col: col.map(temizle))

# Güncellenmiş verileri yeni bir CSV dosyasına kaydet
df.to_csv('test_x.csv', index=False)

print("Baştaki/sondaki harf olmayan karakterler ve fazla boşluklar temizlendi, dosya kaydedildi.")

def turkce_to_ingilizce(text):
    if isinstance(text, str):
        # Türkçe karakterleri İngilizce karakterlere çeviriyoruz
        turkce_karakterler = 'çÇğĞıİöÖşŞüÜ'
        ingilizce_karsiliklar = 'cCgGiIoOsSuU'
        cevirim_tablosu = str.maketrans(turkce_karakterler, ingilizce_karsiliklar)
        return text.translate(cevirim_tablosu)
    return text

# CSV dosyasını oku
df = pd.read_csv('test_x.csv', low_memory=False)

# Tüm DataFrame üzerinde Türkçe karakterleri sil
df = df.apply(lambda col: col.map(turkce_to_ingilizce))

# Güncellenmiş veriyi yeni bir CSV dosyasına kaydet
df.to_csv('test_x.csv', index=False)