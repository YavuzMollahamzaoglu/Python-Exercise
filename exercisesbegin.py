'''count = 0
for number in range(1,12):                        #range aralığı belirlememize yardımcı olur
    if number %2 == 0:
        count += 1
        print(number)
print(f'We have {count} even numbers')'''      #range'i ne kadar uzatırsak okadar sayı yazar ekrana.


'''hours = int(input('Enter hours: '))
rate = float(input('Enter Rate: '))
pay = hours * rate
print('Pay: ', pay)'''


'''weight = 17
height = 12.0
print(weight // 2)
print(height / 3)'''


'''cels = float(input('Enter the tempature in Celsius: '))
fahr = cels * 1.8 + 32
print('Tempature in Fahrenheit: ',fahr)'''             # burda celse tanımladığımız işlemle fahreneitı buluyoruz .

'''hours = int(input('Enter hours: '))
rate = float(input('Enter Rate: '))

if hours > 40:
    pay = (hours - 40)*rate*1.5 + 40 * rate       #fazladan çalışma için ikramiye ekliyoruz normal saatlerin haricimde 1.5 katı para ödüyorruz
else:
    pay = hours * rate
print('Pay: ', pay)'''
'''try:
    hours = int(input('Enter hours: '))
    rate = float(input('Enter Rate: '))
except:
    print('Error, please enter numeric input!')
    quit()               #yanlış type girdiğimiz için kullanıcıyı uyarıyor ve kodu kapatıyoruz.
if hours > 40:
    pay = (hours - 40)*rate*1.5 + 40 * rate
else:
    pay = hours * rate
print('Pay: ', pay)              #niye tanımlama hatası alıyorum.'''

'''try:
    grade = float(input('Enter Score: '))
except:
    print('Wrong score.')
    quit()
if grade < 0 or grade > 1.0:
    print('Score out of range!')
elif grade >= 0.9:
    print('A')
elif grade >= 0.8:
    print('B')
elif grade >= 0.7:
    print('C')
elif grade >= 0.6:
    print('D')
else:
    print('F')'''


'''count = 0
total = 0

while True:
    str_val = input('Enter a number:')
    if str_val == 'done':
        break
    try:
        val = float(str_val)
    except:
        print('Invalid input')                # while döngüsü durduramıyorum 3 numara yazmam gerekirken devam ediyor .
        continue
    total = total + val
    count = count + 1

print(total, count, total/count)'''













