def successors(arr, size):
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
    return successor_dict

def find_paths(graph, start_node, target_node):
    stack = [(start_node, [start_node])]
    paths = []
    while stack:
        current, path = stack.pop()
        if current == target_node:
            paths.append(path)
        else:
            for succ in graph.get(current, []):
                if succ not in path:
                    stack.append((succ, path + [succ]))
    return paths

def find_common(paths):
    common = {}
    for key, lst in paths.items():
        if not lst:
            common[key] = []
        else:
            common[key] = lst[0]
            for tmp in lst[1:]:
                common[key] = list(set(common[key]) & set(tmp))
    return common

def main():
    # length = int(input("Enter size : "))
    length = 11
    # arr = []
    # for i in range(size):
    #     a = []
    #     for j in range(size):
    #         a.append(int(input()))
    #     arr.append(a)
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

    successor = successors(arr, length)
    paths = {}
    for i in range(length):
        paths[i] = find_paths(successor, i, length-1)
    post_dominators = find_common(paths)
    for i, j in post_dominators.items():
        j.remove(i)
        j.sort(reverse = False)
        j.append('Exit')
        print(i, j)

if __name__=="__main__":
    main()