num1 = int(input('enter your number'))
print('operater ')
operater = input('enter your operater ')
num2 = int(input('enter your number'))

def calculater():
    if operater == '+':
        print(num1+num2)
    elif operater == '-':
        print (num1-num2)
    elif operater == '*':
        print (num1*num2)
    elif operater == '/':
        if num1 != 0:
             print (num1/num2)
        else:
            print('zero divison error')
    else:
        print('invalid input')

calculater()