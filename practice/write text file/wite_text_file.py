import os
path = os.path.dirname(os.path.abspath(__file__)) + '/file.txt'

with open(path, 'w') as add:
    add.write('Abdul\n')
    add.write('Mubi')

with open(path,'r') as read:
    ans = read.read()
    print(ans)

path2 = os.path.dirname(os.path.abspath(__file__)) + '/file2.txt'

with open(path2, 'w') as test:
    test.write('Mubi')