import os 
path = os.path.join(os.path.dirname(os.path.abspath(__file__)))

print(os.path.dirname(os.path.abspath(__file__)))

with open('file1.txt') as file:
    list_data = file.readlines()
print(list_data)
for data in list_data:
    if data.strip() == 'success':
        with open('file2.txt','w') as filenew:
            filenew.write('\nhello world2')
            print('added')