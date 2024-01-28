arr = []
nodes = 3
for i in range(nodes):
    a =[]
    for j in range(2):
        a.append(input())
    arr.append(a)

print(arr)

names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
mapping = {}
for i in range(nodes):
    mapping.update({names[i]:i})

print(mapping)