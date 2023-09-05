my_dict = {'a':1, 'b':2, 'c':3}

keys_list = my_dict.keys()
print(keys_list)
print(list(keys_list))
values_list = my_dict.values()
print(values_list)
print(list(values_list))

print(my_dict.items())

print(my_dict['a'])

if 'd' not in my_dict:
    my_dict['d'] = 4

print(my_dict)
