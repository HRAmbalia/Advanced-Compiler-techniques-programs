## LAB - 06-a

# NAME : AMBALIA HARSHIT
# SUBJECT : ACT
# ROLL NO. : MT001
# AIM : Find Dominance frontier

# Input : Number of blocks, Block matrix
# Output : DOminance frontier for all the blocks

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

def find_join_nodes(arr, length):
    transpose_matrix = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
    join_nodes = []
    for i in range(length):
        if(transpose_matrix[i].count(1)>1):
            join_nodes.append(i)
    return join_nodes

def dominator_frontier(dominators, join_nodes):
    dominator_frontiers = {node: set() for node in range(11)}
    for node in range(11):
        children = set()
        for child in range(node + 1, 11):
            if child in dominators[node]:
                children.add(child)

        for child in children:
            dom_child = set(dominators[child])
            dom_child.difference_update(dominators[node])
            for ancestor in dom_child:
                if ancestor not in join_nodes:
                    dominator_frontiers[child].add(ancestor)
    # Adding join nodes to dominator frontiers
    for join_node in join_nodes:
        for node in dominator_frontiers:
            if join_node in dominators[node]:
                dominator_frontiers[node].add(join_node)
    return dominator_frontiers

# def find_immediate_dominator(dominators, x):
#     for _, value in dominators.items():
#         if (x in value):
#             index = value.index(x)
#             return value[index-1]

# def traverse(dominators, immdiate_dominator, pred): 
#     for _, value in dominators.items():
#         if pred in value:
#             start_index = value.index(pred) if pred in value else None
#             end_index = value.index(immdiate_dominator) if immdiate_dominator in value else None
#             sublist = value[start_index:end_index + 1] if start_index is not None and end_index is not None else []
#             print(sublist)

# for join_node in join_nodes:
#     immdiate_dominator = find_immediate_dominator(dominators, join_node)
#     for pred in predecessor.get(join_node, []):
#         # print(pred, dominators, immdiate_dominator, pred)
#         traverse(dominators, immdiate_dominator, pred)

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
    print(f'Successor : {successor}')
    paths = {}
    for i in range(length):
        paths[i] = find_paths(successor, 0, i)
    dominators = find_dominators(paths)
    print(f'Dominators : {dominators}')
    join_nodes = find_join_nodes(arr, length)
    print(f'Join nodes : {join_nodes}')
    df = dominator_frontier(dominators, join_nodes)
    print(f'Dominator Frontier : {df}')

if __name__=="__main__":
    main()