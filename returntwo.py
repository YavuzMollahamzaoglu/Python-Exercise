
'''def bilgi_ver():
    print('İşlem başarılı!')

bilgi_ver()
bilgi_ver()
bilgi_ver()
bilgi_ver()'''


'''def selamla(isim = 'Yavuz'):
    print('Merhaba' + isim)

selamla()'''



'''def topla(x, y):
    print(f'x + y = {x + y}')

topla(3,6)'''



'''def ortalama_hesapla(liste):
    toplam = sum(liste)               #listedeki sayıları toplar
    adet = len(liste)
    ortalama = toplam / adet
    print(f'Girilen sayıların ortalaması : {ortalama}')

ortalama_hesapla([1, 3, 5, 6, 7])'''


'''def buyuk_harfe_cevir(metin):
    metin = metin.upper()
    print(metin)

buyuk_harfe_cevir('fdsafasdf')'''


'''def indirim_yap(fiyat, yuzde):
    indirim_miktarı = fiyat * (yuzde / 100)
    indirimli_fiyat = fiyat - indirim_miktarı
    print(f'İndirimli tutar : {indirimli_fiyat}')

indirim_yap(50, 50)'''


'''def topla(x, y):
    print(x + y)              # burda fonksiyonu değere atayamayız error verir return kalıbını kullanmak gerekir .
    
sonuc = topla(3, 8)
print(sonuc)'''


def topla(x, y):
    return x + y
                              # burda ise return sayesinde değişken içinde kullanabiliyoruz.
sonuc = topla(3, 8)
print(sonuc)



def ortalama_hesapla(x, y):
    return (x + y) / 2
print(type(ortalama_hesapla))




def buyuk_harfe_cevir(metin):
    return metin.upper()
a = buyuk_harfe_cevir('AfdaFDASfdDDSAfdas')
print(a)