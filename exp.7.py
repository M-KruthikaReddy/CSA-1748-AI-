set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Set 1:", set1)
print("Set 2:", set2)
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)
difference_set = set1.difference(set2)
print("Difference between set1 and set2:", difference_set)
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference between set1 and set2:", symmetric_difference_set)
subset_check = set1.issubset(set2)
print("Set 1 is subset of set 2:", subset_check)
