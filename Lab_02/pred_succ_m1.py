arr = [
[-1, 1, -1, -1, -1, -1],
[-1, -1, 1, 1, -1, -1],
[-1, -1, -1, -1, 1, -1],
[-1, -1, -1, -1, 1, -1],
[-1, -1, -1, -1, -1, 1],
[-1, -1, -1, -1, -1, -1],
]
size = 6

successor = []
for i in range(size):
    temp = []
    for j in range(size):
        if(arr[i][j]==1):
            temp.append(j)
    successor.append(temp)
    successorD = {}
    var = 0
for i in successor:
    successorD.update({var:i})
    var += 1
print(successorD)

predecessor = {0 :[0]}
temp = 0
for i in successor:
    for j in i:
    # print(f'Predecessor of {j} is {temp}')
        if j not in predecessor.keys():
            predecessor[j] = [temp]
        else:
            predecessor[j].append(temp)
    temp += 1
print(predecessor)