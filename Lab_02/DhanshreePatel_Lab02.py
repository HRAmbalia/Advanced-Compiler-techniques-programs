def find_paths(graph, start, targetnode):
    stack = [(start, [start])]
    paths = {target: [] for target in targetnode}
    while stack:
        current, path = stack.pop()
        if current in targetnode:
            paths[current].append(path)
        for succ in graph.get(current, []):
            stack.append((succ, path + [succ]))
    return paths

def find_dominators(paths):
    dominators = {}
    for node, path_list in paths.items():
        if not path_list:
            dominators[node] = []
        else:
            common = set(path_list[0])
            for path in path_list[1:]:
                common &= set(path)
                
            dominators[node] = list(common)
    return dominators

size = int(input())
arr = []
for i in range(size):
    a = []
    for j in range(size):
        a.append(int(input()))
    arr.append(a)
start = int(input())

successor = {}
for i in range(size):
    for j in range(size):
        if arr[i][j] == 1:
            if i not in successor:
                successor[i] = [j]
            else:
                successor[i].append(j)

predecessor = {}
for i in range(size):
    for j in range(size):
        if arr[i][j] == 1:
            if j not in predecessor:
                predecessor[j] = [i]
            else:
                predecessor[j].append(i)

i = list(range(size))
routes = find_paths(successor, start, i)
print(successor)
print(predecessor)
print(find_dominators(routes))