
'''def greetUser():
    print('Hi Ahmet!')
    print('Welcome my home')

print('Start')
greetUser()
print('Finish')'''


'''def greetUser(name):
    print(f'Hi {name}!' )
    print('Welcome my home')

greetUser('Yavuz')
greetUser('Havva')
greetUser('Hasan')'''


'''def greetuser (firstName, lastName):
    print(f'Hi {firstName}, {lastName} !')
    print('Welcome to my room .')

greetuser('Yavuz', 'Mollahamzaoğlu')'''


'''def greetuser (firstName, lastName):
    print(f'Hi {firstName}, {lastName} !')
    print('Welcome to my room .')

greetuser(lastName='Yavuz',firstName= 'Mollahamzaoğlu')'''


'''calculateCost(total=50, shipping=5, discount=0.1)    #keyword argümandenir kodun okunrluluğunu arttırır.'''


'''def greetuser (firstName, lastName, message):
    print(f'Hi {firstName}, {lastName} !')
    print(message)

greetuser('Yavuz', 'Mollahamzaoğlu', 'Welcome to my home.')'''



'''def getGreetuser(firstName, lastName):
    return  f'Hi{firstName, lastName}!'

print('Start')
getGreetuser(greetUser('Ahmet', message= 'Welcome my home', lastName = 'Yıldırım')
getGreetuser(greetUser('Ebru', 'Yılmaz')
greetingMessage = getGreetuser('Yavuz', 'Mollahamzaoğlu')
print(greetingMessage)
print('Finish')'''



'''email = 'yavuzmollahamzaoglu@outlook.com'

if email.count('@') != 0:
    print('Your email is valid')
else:
    print('Your email is not valid.')'''



email = 'yavuzmollahamzaoglu@outlook.com'


'''def validateEmail(email):
    pass              # hiç birşey yapma anlamına gelir hata vermez



if validateEmail(email):
    print('Your email is valid')
else:
    print('Your email is not valid.')'''


'''def validateEmail(email):
    if email.count('@')  != 0:
        return True
    return False



if validateEmail(email):
    print('Your email is valid')
else:
    print('Your email is not valid.')'''


def validateEmail(email):
    if email.count('@')  != 0:
        return True

    numberOfDots = email.count('.', email.find('@'))           # email. find işlemi ile @ den sonas gelicek noktaları sayıyor .
    if numberOfDots == 1:
        return True
    return False



if validateEmail(email):
    print('Your email is valid')
else:
    print('Your email is not valid.')

