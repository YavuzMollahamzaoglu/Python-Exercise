'''for i in range(10,0,-1):
    print(i)



print(*range(10))
print(*range(10), sep=',')



while True:
    s = input("Bir sayı girin: ")
    if s == "iptal":
        break

    if len(s) <= 3:
        continue

    print("En fazla üç haneli bir sayı girebilirsiniz.")'''


firs_text ='fdsajklghfskljdfklaerwq'
second_text = 'rewıutrutowerpvzxcmö'              # burdaki işlemle birlikte iki metni karşılaştırarak içlerindeki farkı bulabiliriz.
for s in firs_text:
    if not s in second_text:
        print(s)


