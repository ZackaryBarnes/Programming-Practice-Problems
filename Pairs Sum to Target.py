import os
os.system("clear")

# Pairs Sum to Target problem from ProgrammingExpert.io

def pairs_sum_to_target(list1, list2, target):
    pairs_list = []

    for list1_item in range(len(list1)):
        for list2_item in range(len(list2)):
            if list1[list1_item] + list2[list2_item] == target:
                pairs_list.append([list1_item, list2_item])

    return pairs_list

# Test case
list1 = [1, -2, 4, 5, 9]
list2 = [4, 2, -4, -4, 0]
target = 5

print(pairs_sum_to_target(list1, list2, target))