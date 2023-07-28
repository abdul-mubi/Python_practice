def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3


a = 'abdul'
a.isalpha()
a.isalnum()
a.isascii()

a.isdecimal()
a.isdigit()
a.isnumeric()

a.islower()
a.isupper()

b = ''
b.split()
print(b)
print(f'len={len(b)}')

location = 'https://rc.ota.na.bosch-mobility-cloud.com/api/applications/fleet-management/devices/CCU_2750001244/logTriggers/81dfc427-361c-44dc-a575-d1037d3c8333'
id = location.split('/').pop()
print(id)
