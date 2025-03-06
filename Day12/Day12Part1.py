import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    data = file.read()

char_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                '{','}','"',':','[',']','(',')',',']

for char in char_list:
    data = data.replace(char, 'x')
    
data_list = data.split('x')

while '' in data_list:
    data_list.remove('')

for i in range(len(data_list)):
    data_list[i] = int(data_list[i])

print(sum(data_list))