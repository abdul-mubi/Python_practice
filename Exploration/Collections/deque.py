from collections import deque

# This is how we need to declare an empty deque
empty = deque()
print(empty)
print("-------------------------------------")

a = deque(['abdul',123,'m',52.025])
print(a)
print("-------------------------------------")

for i in a:
    print(i)
print("-------------------------------------")

a.append('mubeena')
print(a)
print(list(a))
print("-------------------------------------")

a.appendleft('starting_key')
print(a)
print(list(a))
print("-------------------------------------")

a.extend([1,2.3,70])
print(a)
print("-------------------------------------")

a.extendleft('Riyath')
print(a)
a.extendleft([1,2.3,70])
print(a)
print("-------------------------------------")

count = a.count(2.3)
print(count)
print("-------------------------------------")

index = a.index('starting_key',9,len(a)+5)
print(len(a))
print(index)
print("-------------------------------------")

b = a.copy()
print(b)
print("-------------------------------------")

b.insert(len(b)+5,'hehe')
print(b)
print(a)

b.insert(5,'hehe')
print(b)
print(a)
print("-------------------------------------")

print(b)
out = b.pop()
print(out)
print(b)

out = b.popleft()
print(out)
print(b)
print("-------------------------------------")

b. remove('abdul')
print(b)
print("-------------------------------------")

b.reverse()
print(b)
print("-------------------------------------")

b.rotate(1)
print(b)

b.rotate(2)
print(b)

b.rotate(-1)
print(b)

b.rotate(-2)
print(b)
print("-------------------------------------")

empty_with_max_defined = deque(maxlen=3)
empty_with_max_defined.extend('abc')
print(empty_with_max_defined)
empty_with_max_defined.appendleft(1)
print(empty_with_max_defined)
empty_with_max_defined.appendleft(2)
print(empty_with_max_defined)
empty_with_max_defined.append(3)
print(empty_with_max_defined)
print("-------------------------------------")


