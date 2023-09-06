#input = 'aaaabbbccda' output = 'a4b3c2d1a1'

def logic_fun(input_str):
    count = 1
    out = ''
    
    for i in range(1,len(input_str)):
        if input_str[i] == input_str[i-1]:
            count += 1
        else:
            out = out + input_str[i-1] + str(count)
            count = 1

    out += input_str[-1] + str(count)
    return out

input_str = 'aaaabbbccdddad'
output_str = logic_fun(input_str)
print(output_str)


