
parola = 'yavuz200'

soru = input('parolanız:')

if soru == parola:
    print('doğru parola!')

elif soru != parola:
    print('Yanlış Parola')



sayı = input('Sayı:')

if int(sayı) >= 100:
    print('Sayı 100 veya 100den büyüktür.')

elif int(sayı) <= 100:
    print('sayı 100 veya 100den küçüktür')
