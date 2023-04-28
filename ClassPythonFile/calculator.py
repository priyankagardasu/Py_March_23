def addition(num1 , num2):
    '''this function returns addition of two integers... @kumar'''
    return num1 + num2

def subtraction(num1 , num2):
    return num1 - num2

def multiplication(num1 , num2):
    return num1 * num2

def division(num1 , num2):
    return num1 / num2

def floordivision(num1 , num2):
    return num1 // num2

def modulus(num1 , num2):
    return num1 % num2


def expo(num1 , num2):
    return num1 ** num2

def readInput():
    n1 = int(input('Enter n1: '))
    n2 = int(input('Enter n2: '))
    return n1,n2

def main():
    while True:
        print('*'*10 , 'WELCOME TO CALCULATOR SOFTWARE PROGRAM' , '*'*10)
        print('*'*10, 'MENU','*'*10)
        print('1.Addition\n 2.Subtration\n 3.Multiplication\n 4.Division\n 5.FloorDivision\n 6.Modulus\n 7.Expo\n -1.Exit')
        print('*'*20)

        ch = int( input("enter the choice: "))

        if(ch != -1): num1 , num2 = readInput()

        if ch == 1:
            res = addition(num1, num2)
            print(f'Addition of {num1} + {num2} = {res}')

        elif ch == 2:
            res = subtraction(num1, num2)
            print(f'subtraction of {num1}  - {num2} = {res}')
        elif ch == 3:
            res = multiplication(num1, num2)
            print(f'multiplication of {num1} * {num2} = {res}')

        elif ch == 4:
            res = division(num1, num2)
            print(f'division of {num1} / {num2} = {res}')

        elif ch == 5:
            res = floordivision(num1, num2)
            print(f'floordivision of {num1} // {num2} = {res}')

        elif ch == 6:
            res = modulus(num1, num2)
            print(f'modulus of {num1} % {num2} = {res}')

        elif ch == 7:
            res = expo(num1, num2)
            print(f'Exponentation of {num1} + {num2} = {res}')

        elif ch == -1:
            break
        else:
            print('Please enter valid choice from menu...')


if __name__ == '__main__':
    main()