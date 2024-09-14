import pandas as pd

# CSV dosyasını oku
df = pd.read_csv('guncellenmis_train.csv', low_memory=False)

# Türkçe ayları İngilizceye çevirme fonksiyonu
def ayirici(data):
    if isinstance(data, str):
        ayiricilar = [".", ",", "/", " ", "-"]  # ":" ekleyerek saati de dahil ettik
        listData = []

        # Veriyi ayırıcılarla bölmek
        for ayirici in ayiricilar:
            listData = data.split(ayirici)
            if len(listData) > 2:
                break

        if len(listData) > 2:
        # Yılın iki veya dört basamaklı olabileceğini kontrol et
            parca = listData[2]
            parca = parca.split(" ")[0]
            parca = parca.strip()  # Eğer başında veya sonunda boşluk varsa temizler
            if len(parca) == 4 and parca.isdigit():  # 4 basamaklı yıl
                return int(parca)  # Yılı integer olarak döndür
            if len(listData[0]) == 4 and parca.isdigit():
                return int(listData[0])  # Yılı integer olarak döndür
            elif len(parca) == 2 and parca.isdigit():  # 2 basamaklı yıl
                return int("19" + parca) if int(parca) > 50 else int("20" + parca)  # Integer olarak döndür
            print(listData)
    return None

df['Dogum Tarihi'] = df['Dogum Tarihi'].astype(str)
df['Basvuru Yili'] = df['Basvuru Yili'].astype(str)
df['Basvuru Yasi'] = df['Basvuru Yasi'].astype(str)
# 'Dogum Tarihi' ve 'Basvuru Yili' sütunlarındaki tarihleri çevir ve integer yap
df['Dogum Tarihi'] = df['Dogum Tarihi'].apply(ayirici)
df['Basvuru Yili'] = df['Basvuru Yili'].apply(ayirici)

# Başvuru yaşını hesaplama (yıl farkını bulmak)
def hesapla_basvuru_yasi(row):
    if row['Dogum Tarihi'] is not None and row['Basvuru Yili'] is not None:
        yas = row['Basvuru Yili'] - row['Dogum Tarihi']
        return yas if yas > 18 else "Gelecekten"
    return "Bilinmiyor"  # Eğer tarih verisi eksikse

df['Basvuru Yasi'] = df.apply(hesapla_basvuru_yasi, axis=1)

# Yeni sütunu kontrol etmek için
print(df[['Basvuru Yili', 'Dogum Tarihi', 'Basvuru Yasi']].head(60))

# Yeni veriyi kaydetmek isterseniz
df.to_csv('guncellenmis_train.csv', index=False)

print("Veri kaydedildi ve yaşlar hesaplandı.")
