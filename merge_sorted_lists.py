def merge_sorted_lists(list1, list2):
    merged_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    return merged_list
list1=[2,3,4,5,6,7,8,9,10]
list2=[11,12,13,14,15,16,17]
merged_list=merge_sorted_lists(list1, list2)
print(merged_list)




