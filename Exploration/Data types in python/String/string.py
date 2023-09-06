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
print(input[9])