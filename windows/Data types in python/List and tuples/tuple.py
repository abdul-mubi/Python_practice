my_tuple = ((1,2,3),(4,5,6),(1,2,3))
print(my_tuple[0][0])
print(my_tuple[1])

print(len(my_tuple))
print(len(my_tuple[0]))

print(my_tuple.index((4,5,6)))

print(my_tuple.count((1,2,3)))

a = 15
b = 20
print('Before swapping:')
print(f'a = {a}, b = {b}')

(a,b) = (b,a)
print('After swapping:')
print(f'a = {a}, b = {b}')

