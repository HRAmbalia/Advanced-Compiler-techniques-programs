## LAB - 02

# NAME : AMBALIA HARSHIT
# SUBJECT : ACT
# ROLL NO. : MT001
# AIM : Find Successors, Predecessors and Dominators from given block matrix

# Input : Block matrix
# Output : Find Successors, Predecessors & Dominators

# Understanding : 
# -> Firstly finding Successors & Predecessors from block matrix.
# -> For dominators, 
#       Finding all the possible paths from starting node to that particular node.
#       Taking common in all those path which is nothing but dominators.
#       Repeating this process for all the blocks.


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
        current, path = stack.pop()
        if current == target_node:
            paths.append(path)
        else:
            for succ in graph.get(current, []):
                stack.append((succ, path + [succ]))
    print(paths)
    return paths

def find_dominators(paths):
    common = {}
    for key, lst in paths.items():
        if not lst:
            common[key] = []
        else:
            common[key] = lst[0]
            for tmp in lst[1:]:
                common[key] = list(set(common[key]) & set(tmp))
        
    return common


if __name__=="__main__":
    # size = int(input("Enter size : "))
    # arr = []
    # for i in range(size):
    #     a = []
    #     for j in range(size):
    #         a.append(int(input()))
    #     arr.append(a)
    size = 6
    start = 0
    arr = [
        [-1, 1, -1, -1, -1, -1],
        [-1, -1, 1, 1, -1, -1],
        [-1, -1, -1, -1, 1, -1],
        [-1, -1, -1, -1, 1, -1],
        [-1, -1, -1, -1, -1, 1],
        [-1, -1, -1, -1, -1, -1],
    ]

    successor = successors(arr, size)
    predecessor = predecessors(arr, size)
    paths = {}
    for i in range(size):
        paths[i] = find_paths(successor, start, i)
    dominators = find_dominators(paths)

    print(f'Successor : {successor}')
    print(f'Predecessor : {predecessor}')
    print(f'Dominators : {dominators}')