# [(1,2),(3,4)(5,6)] convert this into dictionary dict: {{1:2},{3:4},{5:6}}

a = [(1,2), (3,4), (5,6)]
b = {}
for i in a:
    b.update({i[0]: i[1]})

print('////////////////////////copy///////////////////////////////////')
    
print(b)
c = b.copy()
print(c)

print('//////////////////////////update/////////////////////////////////')

c.update({7:8})
print(c)
print(b)

print('////////////////////////fromkeys///////////////////////////////')

eg_key  = ['key1', 'key2']
d = {}.fromkeys(eg_key,[])
print(d)

eg_key_string = 'key3'
e = c.fromkeys(eg_key_string,' ')
print(e)
print(c)

print('////////////////////////get///////////////////////////////')

val = b.get(1)
print(val)

print('/////////////////////////pop//////////////////////////////////')
print(c)
pop_value = c.pop(1)
print(c)
print(f'pop_value = {pop_value}')

print('/////////////////////////popitem//////////////////////////////////')
print(c)
popitem_val = c.popitem()
print(c)
print(f'popitem_val = {popitem_val}')

print('/////////////////////////setdefault//////////////////////////////////')
print(c)
set_default = c.setdefault(9,10)
print(c)
print(f'set_default-{set_default}')

x = c.setdefault(9,20)
print(c)
print(x)


print('//////////////////////////clear////////////////////////////////')
b.clear()
print(b)

