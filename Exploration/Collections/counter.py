from collections import Counter

c = Counter('aaddffgg')
print(c)

c = Counter(['abdul','mubi','rayan', 'abdul'])
print(c)

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

