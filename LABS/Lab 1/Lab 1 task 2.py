a=float(input('Enter a number'))
b=float(input('Enter second number'))
op=input('Enter the operator')
if op=='-':
    print('Subtraction:',a-b)
elif op=='+':
    print('Addition:',abs(-a-b))
elif op=='*':
    print('Multiplication:',a*b)
elif op=='/':
    print('Division:',a/b)
else:
    print('Incorrect operator!')