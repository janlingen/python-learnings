def pairs_sum_to_target(list1, list2, target):
    result = []
    for x in range(len(list1)):
        for y in range(len(list2)):
            if list1[x] + list2[y] == target:
                result.append([x, y])
    return result
    