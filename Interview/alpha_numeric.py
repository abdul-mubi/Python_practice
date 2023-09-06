input = 'Apple price is $250.25' #exp out = $250.25
out = ''
for i in input:
    if not i.isalpha():
        out += i
print(out)
print(out.strip())