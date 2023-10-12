def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3


a = 'abdul123'
print(a.isalpha())
print(a.isalnum())
print(a.isascii())

print(a.isdecimal())
print(a.isdigit())
print(a.isnumeric())

print(a.islower())
print(a.isupper())

b = ''
b.split()
print(b)
print(f'len={len(b)}')

location = 'https://rc.ota.na.bosch-mobility-cloud.com/api/applications/fleet-management/devices/CCU_2750001244/logTriggers/81dfc427-361c-44dc-a575-d1037d3c8333'
id = location.split('/').pop()
print(id)


input = 'aaaabbccd'
print(input[8])
# print(input[9])

input = 'abdul123'
for i in input:
    print(i.isdecimal())
    print(i.isnumeric())
    print(i.isdigit())

print('------------------')
i = '528'
print(i.isdecimal())
print(i.isnumeric())
print(i.isdigit())
#Refer this link for difference in these 3 methods in string - https://www.learnbyexample.org/python-string-isdecimal-method/#:~:text=As%20you%20can%20see%2C%20the,%2C%20Roman%20Numerals%2C%20Currency%20Numerators.

latitude = ['9A', '35', '49', '0B']
hex_string = ''.join(latitude)
print(hex_string)
print('======================')
z = 'abdul'
print(z.capitalize())
print(z.upper())
