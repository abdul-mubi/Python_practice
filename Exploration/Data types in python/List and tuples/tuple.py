my_tuple = ((1,2,3),(4,5,6),(1,2,3))
print(my_tuple[0][0])
print(my_tuple[1])

print(len(my_tuple))
print(len(my_tuple[0]))

print(my_tuple.index((4,5,6)))

print(my_tuple.count((1,2,3)))

#swap 2 variable without using 3rd parameter
#Using Tuple
a = 15
b = 20
print('Before swapping:')
print(f'a = {a}, b = {b}')

(a,b) = (b,a)
print('After swapping:')
print(f'a = {a}, b = {b}')

#Using List
x = 1
y = 2
print('Before swapping:')
print(f'x = {x}, y = {y}')
[x,y] = [y,x]

print('After swapping:')
print(f'x = {x}, y = {y}')
print('-------------------------------------------------------------')
def get_values():
    return 10, 20, 30

values = get_values()
print(type(values))
print(values[0]) 

