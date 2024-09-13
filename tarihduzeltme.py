def ayirici(data):
    ayiricilar = [".", ",", "/", " ", "-"]  # ":" ekleyerek saati de dahil ettik
    listData = []

    # Veriyi ayırıcılarla bölmek
    for ayirici in ayiricilar:
        listData = data.split(ayirici)
        if len(listData) > 2:
            break

    # Yılın iki veya dört basamaklı olabileceğini kontrol et
    for parca in listData:
        parca = parca.split(" ")[0]
        parca = parca.strip()  # Eğer başında veya sonunda boşluk varsa temizler
        if len(parca) == 4 and parca.isdigit():  # 4 basamaklı yıl
            return parca
        elif len(parca) == 2 and parca.isdigit():  # 2 basamaklı yıl
            return "19" + parca if int(parca) > 50 else "20" + parca  # 50'den büyükse 1900'lü yıllar

    return None


# Testler
print(ayirici("1.Jan.2002 00:00"))  # 2002
print(ayirici("1/1/97"))  # 1997
print(ayirici("9/1/99 0:00"))  # 1999
print(ayirici("12-05-21 14:30"))  # 2021
print(ayirici("05-07-1985 23:59"))  # 1985
