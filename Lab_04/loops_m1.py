arr = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

def predecessors(arr, size):
    predecessor_dict = {}
    for i in range(size):
        for j in range(size):
            if arr[i][j] == 1:
                if j not in predecessor_dict:
                    predecessor_dict[j] = [i]
                else:
                    predecessor_dict[j].append(i)
            else:
                if i not in predecessor_dict:
                    predecessor_dict[j] = []
    return predecessor_dict

size = 11
predecessor = predecessors(arr, size)
n = 7
n -= 1
d = 3
d -= 1

loop = []
stack = []

def insert(temp):
    if temp not in loop:
        loop.append(temp)
        stack.append(temp)

loop.append(d)
insert(n)
while(len(stack)>0):
    tmp = stack.pop()
    for i in predecessor[tmp]:
        insert(i)

for i in range(len(loop)):
    loop[i] = loop[i]+1
distinct_list = set(loop)
print(distinct_list)
