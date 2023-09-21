a = [1, 2.5, 'abdul', True]

a.append('Mubi')
print(a)

a.extend([2,3,4])
print(a)

a.extend([(8,5,2),(3,6,9)])
print(a)

a.extend('Rayan')
print(a)

a.insert(0,50)
print(a)

a.remove(50)
print(a)

pop_value = a.pop()
print(pop_value)

pop_value2 = a.pop(3)
print(pop_value2)

index_value = a.index('abdul')
print(index_value)

#throughing an error -> ValueError: 'Abdul' is not in list
'''
index_value = a.index('Abdul')
print(index_value)

'''
count_value = a.count('a')
print(count_value)

#sorting, max and min is not possible as 'a' list has string, floating and boolean values, getting this error ->  TypeError: '<' not supported between instances of 'str' and 'float'
'''
sort_value = a.sort()
print(sort_value)

maximum_value = max(a)
print(maximum_value)

manimum_value = min(a)
print(manimum_value)

'''

reverse_value = a.reverse()
print(reverse_value)
print(a)

# if you use the copy() method to create a copy of the list a and assign it to deep_copy_of_the_list, any changes made to deep_copy_of_the_list will not affect a
deep_copy_of_the_list = a.copy()
print(deep_copy_of_the_list)
deep_copy_of_the_list.append('added')
print(deep_copy_of_the_list)
print(a)

# In Python, when you assign a list a to another variable b using the assignment operator (=), 
# the reference of a is assigned to b. 
# This means that both a and b will refer to the same underlying list object. 
# Any changes made to the list through one variable will be reflected in the other variable as well. 

b = a
b.append('added1')
print(b)
print(a)

length = len(a)
print(length)

# half_length = length/2 - it will through type error as length/2 retutns float value
half_length = length//2
print(half_length)
first_half = a[:half_length]
second_half = a[half_length:]

print(first_half)
print(second_half)

a.clear()
print(a)

del a



