
def addition(n1,n2):
    return f'addition: {n1+n2}'

def multiplication(n1,n2):
    return f'multiplication : {n1 * n2}'

def division(n1:int,n2:int) -> float:
    return f'division : {n1 / n2}'

def readInput():

    num1 = int(input('Enter NUM1: '))
    num2 = int(input('Enter NUM2: '))

    return (num1,num2)

if __name__ == '__main__':

    n1,n2 = readInput()

    addRes = addition(n1,n2)
    multRes = multiplication(n1,n2)
    divRes = division(n1,n2)

    print(addRes , multRes , divRes , sep= '\n')
    