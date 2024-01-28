arr = [
[-1, 1, -1, -1, -1, -1],
[-1, -1, 1, 1, -1, -1],
[-1, -1, -1, -1, 1, -1],
[-1, -1, -1, -1, 1, -1],
[-1, -1, -1, -1, -1, 1],
[-1, -1, -1, -1, -1, -1],
]
size = 6

successor_dict = {}
for i in range(size):
    for j in range(size):
        if arr[i][j] == 1:
            if i not in successor_dict:
                successor_dict[i] = [j]
            else:
                successor_dict[i].append(j)
        else:
            if i not in successor_dict:
                successor_dict[i] = []
print(successor_dict)

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
print(predecessor_dict)

