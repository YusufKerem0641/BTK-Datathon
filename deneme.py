import pandas as pd

sutun = 'Bölüm'
# low_memory=False ile CSV dosyasını oku
df = pd.read_csv('guncellenmis_train.csv', low_memory=False)


def alan_belirle(bolum):
    # Boş değerleri kontrol et ve string'e dönüştür
    if isinstance(bolum, float):
        bolum = ''

    # Anahtar kelimelerle kategorileri belirle
    muhendislik_kelimeler = ['MUHENDIS', 'ENDUSTRI', 'TEKNOLOJI', 'PROGRAMCILIK', 'BILISIM', 'BILGISAYAR']
    saglik_bilimleri_kelimeler = ['TIP', 'HEMSIRE', 'ECZACI', 'ACIL', 'AGIZ', 'DIS', 'AMELIYATHANE', 'ANESTEZI',
                                  'BESLENME', 'FIZYOTERAPI', 'EBELIK', 'ODYOLOJI', 'VETERINER']
    hukuk_kelimeler = ['HUKUK', 'ADLI']
    sosyal_bilimler_kelimeler = ['ISLETME', 'IKTISAT', 'MALIYE', 'SOSYOLOJI', 'PSIKOLOJI', 'TARIH', 'FELSEFE',
                                 'GAZETECILIK', 'COGRAFYA', 'ISTATISTIK', 'SIYASET', 'KAMUYONETIMI', 'EKONOMI',
                                 'EKONOMETRI', 'ULUSLARARASI', 'HALKLA', 'REKLAMCILIK', 'ILETISIM', 'SANATTARIHI',
                                 'GORSELILETISIM', 'SOSYAL', 'ULUSLARASITICARET']
    dogal_kelimeler = ['DIL', 'EDEBIYAT', 'TURKDILIVEEDEBIYATI', 'ALMAN', 'ARAP', 'INGILIZ', 'MUTERCIM',
                                 'TERCUMAN','MATEMATIK','FIZIK','KIMYA','BIYOLOJI']
    mimarlik_tasarim_kelimeler = ['MIMARLIK', 'ICMIMARLIK', 'CEVRE', 'SEHIR', 'PEYZAJ', 'TASARIM']
    egitim_kelimeler = ['OGRETMEN', 'EGITIM', 'COCUKGELISIMI']

    # Kategorilere göre sınıflandırma
    for kelime in muhendislik_kelimeler:
        if kelime in bolum:
            return 'Mühendislik ve Teknoloji'

    for kelime in saglik_bilimleri_kelimeler:
        if kelime in bolum:
            return 'Sağlık Bilimleri'

    for kelime in hukuk_kelimeler:
        if kelime in bolum:
            return 'Hukuk'

    for kelime in egitim_kelimeler:
        if kelime in bolum:
            return 'Eğitim'

    for kelime in sosyal_bilimler_kelimeler:
        if kelime in bolum:
            return 'Sosyal Bilimler'

    for kelime in mimarlik_tasarim_kelimeler:
        if kelime in bolum:
            return 'Mimarlık ve Tasarım'

    for kelime in dogal_kelimeler:
        if kelime in bolum:
            return 'Dogal Bilimler'

    return 'Diger'

# Bölümlerin alanlarını belirleyin
df[sutun] = df[sutun].apply(alan_belirle)

df.to_csv('guncellenmis_train.csv', index=False)

