def calculate():
    num1 = float(input('Enter first number:'))
    num2 = float(input('Enter second number:'))

    op = input('Enter operator:')
    if op == '+':
        addition(num1, num2)
    elif op == '-':
        subtraction(num1, num2)
    elif op == '/':
        division(num1, num2)
    elif op == '*':
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
