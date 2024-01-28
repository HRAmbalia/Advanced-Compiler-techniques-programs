def find_difference(list1, list2):
  result = []
  for i in range(len(list1)):
    if(list1[i]==1):
        result.append(list1[i] - list2[i])
    else:
        result.append(0)
  return result


# Example usage:

list1 = [0, 1, 0, 0, 1, 0, 1]
list2 = [0, 0, 0, 0, 1, 1, 0]
difference = find_difference(list1, list2)

print(difference)
