a = 'my name is adithya' # out = My Name Is Adithya, without using build-in functions

capital = True
result = ''

for i in a:
    if i == ' ':
        capital = True
        result = result + i
    elif i != ' ' and capital:
        result = result + i.upper()
        capital = False
    else:
        result = result + i

print(result)