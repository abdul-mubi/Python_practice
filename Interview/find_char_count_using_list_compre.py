input1 = 'aaaabbbccd' #expecting out = a4b3c2d1

#This is my logic
dict_out = {}
out = [ dict_out.update({i:dict_out.get(i,0)+1}) for i in input1]
print(out)
final_out = ''.join([f"{char}{count}"for char,count in dict_out.items()])
print(dict_out)
print(final_out)
print('---------------------------------------------------------------')

#But actual correct logic is below:

pairs = [(char, str(input1.count(char))) for char in sorted(set(input1))]
print(pairs)

real_out = ''
for char, count in pairs:
    real_out += char + count

# One line solution for the above for loop
# real_out = ''.join([f"{char}{count}"for char,count in pairs])

print(real_out)