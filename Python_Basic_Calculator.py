a = int(input('Enter 1st value: '))
b = int(input('Enter 2nd value: '))
c = a + b
print('This gives you addition', c)
d = a * b
print('This gives you multiplication', d)
e = a - b
print('This gives you subtraction', e)
try:
    f = a / b
    print('This gives you division', f, '//')
except ZeroDivisionError as e:
    print('"Division is not possible because you assigned-->zero to-->divide"//')
