#put all these nested loop in single loop
l2 = [1,2,[1,3,[2,4,[3], 34]]]

print(type(l2))
out_list = []

def func(input):
    for i in input:
        if type(i) == list:
            func(i)
        else:
            out_list.append(i)
            
func(l2)
print(out_list)