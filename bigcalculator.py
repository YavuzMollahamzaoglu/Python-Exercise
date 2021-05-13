def calculate():
    num1 = float(input('Enter first number:'))
    num2 = float(input('Enter second number:'))

    op = input('1 = Addition\n2 = Subtraction\n3 = Division\n4 = Multiplication\n Enter Operator: ')
    if op == '1':
        addition(num1, num2)
    elif op == '2':
        subtraction(num1, num2)
    elif op == '3':
        division(num1, num2)
    elif op == '4':
        multiplication(num1, num2)
    else:
        print('Invalid Operator')


def addition(first_num, second_num):
    print(f'{first_num} + {second_num} = {first_num + second_num}')

def subtraction(first_num, second_num):
    print(f'{first_num} - {second_num} = {first_num - second_num}')

def multiplication(first_num, second_num):
    print(f'{first_num} * {second_num} = {first_num * second_num}')

def division(first_num, second_num):
    print(f'{first_num} / {second_num} = {first_num / second_num}')

calculate()
#fdsafdsa
