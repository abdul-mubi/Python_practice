a = 'abdul is a superstar we know that my'
list_a = a.split(' ')
first_ans = []

for val in range(len(list_a)-1,-1,-1):
    first_ans.append(list_a[val])
    if val !=0 and val%2 != 0:
        switch_val = list_a[val]
        second_ans = ''
        for i in range(len(switch_val)-1,-1,-1):
            second_ans = second_ans + switch_val[i]
        first_ans.remove(list_a[val])
        first_ans.append(second_ans)

print(first_ans)