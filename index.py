print('1. Addition: + \n'
      '2. Subtraction: - \n'
      '3. Multiplication: * \n'
      '4. Division: / \n')


Num1 = float(input('Enter The First Number \n'))
op = input('Enter Operator \n')
Num2 = float(input('Enter the Second Number \n'))

if op == '+':
    print(Num1 + Num2)
elif op == '-':
    print(Num1 - Num2)
elif op == '*':
    print(Num1 * Num2)
elif op == '/':
    print(Num1 / Num2)
else:
    print('Invalid Input')