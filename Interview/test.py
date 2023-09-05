a = 'a1b2d3u4l5'
b_list = []
c_list = []
for i in a:
    if i.isdigit():
        b_list.append(i)
    elif i.isalpha():
        c_list.append(i)

print(b_list)
print(c_list)