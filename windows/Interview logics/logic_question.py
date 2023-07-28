input_list = []
result_list = []
input_dict = {}

list_len = input('Define len of list')

for i in range(int(list_len)):
    input_list.append(input('type number'))
print('All inputs are taken')

for i in input_list:
    digit_len = len(i)
    print(digit_len)
    if digit_len in input_dict:
        input_dict[digit_len].append(i)
    else:
        new_value_list = []
        new_value_list.append(i)
        input_dict.update({digit_len : new_value_list})

sort = sorted(input_dict.keys())
for key in sort:
    result_list.extend(input_dict[key])

print(f'Result is {result_list}')
