#Add numbers in a string

user_data = input('Type input: ')
output = 0
num = ''
for char in user_data:
    if char.isdigit():
        num += char
    elif len(num) > 0 and num.isnumeric():
        output += int(num)
        num = ''

if len(num) > 0:
        output += int(num)

print(output)