arr = [
[-1, 1, -1, -1, -1, -1],
[-1, -1, 1, 1, -1, -1],
[-1, -1, -1, -1, 1, -1],
[-1, -1, -1, -1, 1, -1],
[-1, -1, -1, -1, -1, 1],
[-1, -1, -1, -1, -1, -1],
]
size = 6
start = 0


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

def find_paths(graph, start_node, target_node):
    stack = [(start_node, [start_node])]
    paths = []

    while stack:
        current_node, current_path = stack.pop()

        if current_node == target_node:
            paths.append(current_path)
        else:
            for successor in graph.get(current_node, []):
                stack.append((successor, current_path + [successor]))

    return paths

def find_dominators(paths):
    common_elements = {}
    for key, lists_of_lists in paths.items():
        if not lists_of_lists:
            common_elements[key] = []
        else:
            # Initialize with the first list
            common_elements[key] = lists_of_lists[0]
            for sublist in lists_of_lists[1:]:
                common_elements[key] = list(set(common_elements[key]) & set(sublist))
        
    return common_elements

successor = successors(arr, size)
predecessor = predecessors(arr, size)
paths = {}
for i in range(size):
    paths[i] = find_paths(successor, start, i)
dominators = find_dominators(paths)

print(f'Successor : {successor}')
print(f'Predecessor : {predecessor}')
print(f'Dominators : {dominators}')