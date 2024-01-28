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

graph = {0: [1], 1: [2, 3], 2: [4], 3: [4], 4: [5], 5: []}
start = 0
paths = {}
for i in range(size):
    paths[i] = find_paths(graph, start, i)

common_elements = {}
for key, lists_of_lists in paths.items():
    if not lists_of_lists:
        common_elements[key] = []
    else:
        # Initialize with the first list
        common_elements[key] = lists_of_lists[0]
        for sublist in lists_of_lists[1:]:
            common_elements[key] = list(set(common_elements[key]) & set(sublist))

for key, common_list in common_elements.items():
    print(f"Key {key}: {common_list}")