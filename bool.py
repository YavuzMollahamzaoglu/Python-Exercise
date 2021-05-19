
a = 1
a == 1
print(a == 1)

print(bool('elma'))
print(bool(0))



b = ''
print(bool(b))



kullanıcı = input('Kullanıcı adınız:')

if bool(kullanıcı) == True:
    print('Teşekkürler')
else:
    print('Bu alan boş bırakılamaz')


kullanıcı_adı = input("Kullanıcı adınız: ")
parola = input("Parolanız: ")

if kullanıcı_adı == "aliveli":
    if parola == "12345678":
        print("Programa hoşgeldiniz")
    else:
        print("Yanlış kullanıcı adı veya parola!")

else:
    print("Yanlış kullanıcı adı veya parola!")
