# start = 'A'
# end = 'C'
# nodes = 3
# str = '0010'
# arr = [
#     ['B', 'A'],
#     ['C', 'A'],
#     ['C', 'C']
# ]
# mapping = {'A':0, 'B':1, 'C':2}


nodes = int(input("Enter number of nodes : "))

start = input("Enter Start node : ")

end_node_count = int(input("Enter number of End nodes : "))
end_nodes = []
for i in range(end_node_count):
    end_nodes.append(input())
print(end_nodes)

print("Enter Array : ")
arr = []
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

strg = input("Enter string : ")


current = mapping[start]
for i in strg:
    i = int(i)
    current = mapping[arr[current][i]]

flag = False
for i in end_nodes:
    print(i)
    print(mapping[str(i)])
    print(current)
    if(mapping[i]==current):
        flag = True
        break

if flag:
    print(f'String {strg} is ACCEPTED')
else:
    print(f'String {strg} is NOT ACCEPTED')