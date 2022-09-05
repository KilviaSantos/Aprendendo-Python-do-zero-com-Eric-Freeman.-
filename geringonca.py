import random
# Geringonça

characters = ['a','m','a','n','a','p','l','a','n','a','c']

output = ''
length = len(characters)
index = 0
while (index < length):
    output = output + characters[index]
    index = index + 1

length = length * -1
index = -2

while ( index >= length):
    output = output + characters[index]
    index = index - 1

print(output)
