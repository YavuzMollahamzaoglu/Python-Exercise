while True:
    parola = input('Parolanızı giriniz:')

    if not parola :
        print('parola bölümü boş bırakılamaz')

    elif len(parola) > 8 or len(parola) < 3:
        print('Parola 8 karakterden uzun 3 karakterden kısa olmamalı')

    else:
        print('Yeni parolanız: ', parola)
        break