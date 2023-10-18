from collections import Counter

c = Counter('ccaaddffgg')
print(c)
print(sorted(c))
print(c.most_common())

c = Counter(['abdul','mubi','rayan', 'abdul'])
print(c)
for key,value in c.items():
    print(f"key={key}, value={value}")

c = Counter({'red':2,'blue':5})
print(c)

c = Counter(a=4, b=2, c=0, d=-2)
c.elements()
print(c)
out_list = sorted(c)
print(out_list)

c = Counter(['abdul','mubi','rayan', 'abdul']).most_common()
print(c)
c = Counter(['abdul','mubi','rayan', 'abdul']).most_common(2)
print(c)
c = Counter(['abdul','mubi','rayan', 'abdul']).most_common(1)
print(c)
c = Counter('abracadabra').most_common(3)
print(c)

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=5)
c.subtract(d)
print(c)
d.subtract(c)
print(d)

c = Counter(a=4, b=2, c=0, d=-2)
total = c.total()
print(c)
print(total)

c = Counter({'red':2,'blue':5})
c.update({'black':4})
c.update({'red':4})
print(c)

c = Counter(['abdul','mubi','rayan', 'abdul'])
print(c)
c.update(['abdul'])
print(c)

