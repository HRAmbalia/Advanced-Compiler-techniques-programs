def find_union(list_of_lists):
  result = []
  for i in range(len(list_of_lists[0])):
    max_value = max([list_of_lists[j][i] for j in range(len(list_of_lists))])
    result.append(max_value)
  return result

list_of_lists = [[1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
union = find_union(list_of_lists)
print(union)
