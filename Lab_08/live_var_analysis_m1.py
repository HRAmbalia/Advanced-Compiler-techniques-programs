definition_dict = {
    0 : [],
    1 : ['i', 'j', 'a'],
    2 : [],
    3 : ['a'],
    4 : ['i'],
    5 : [],
}

use_dict = {
    0 : [],
    1 : ['m', 'n', 'u1'],
    2 : ['i', 'j'],
    3 : ['u2'],
    4 : ['a', 'j'],
    5 : [],
}

successor_set = [
    [1],
    [2],
    [3, 4],
    [4],
    [5, 2],
    [],
]

number_of_blocks = 6
order_list = [5, 4, 3, 2, 1, 0]

live_in_set = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
live_out_set = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}


##########################################################


def find_union(list_of_lists):
    union_result = set()
    for inner_list in list_of_lists:
        union_result = union_result.union(set(inner_list))
    union_list = list(union_result)
    return union_list

def find_difference(live_in_list, definition_list):
    set1 = set(live_in_list)
    set2 = set(definition_list)
    difference = set1.difference(set2)
    result_list = list(difference)
    return result_list

for iteration_number, i in enumerate(order_list):
    if(iteration_number<=5):
        temp_liveout = []
        for j in successor_set[i]:
            temp_liveout.append(live_in_set[j])
        live_out_set[i] = find_union(temp_liveout)
        
        temp_livein = []
        temp_livein.append(use_dict[i])
        temp_livein.append(find_difference(live_out_set[i], definition_dict[i]))
        live_in_set[i] = find_union(temp_livein)

print(live_out_set)
print(live_in_set)


