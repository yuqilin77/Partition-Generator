import copy

def extend_partitions(some_partitions, a_new_element):
    returned_partitions = []
    for _partition in some_partitions:  # e.g., _partition = [[0], [11]]
        for i in range(len(_partition)):  # e.g., i points to [0]
            new_partition = copy.deepcopy(_partition)
            new_partition[i].append(a_new_element)  # e.g., get [[0, 22], [11]]
            returned_partitions.append(new_partition)

# (Including [a_new_element]): returned_partition includes all partitions
# of S union {a_new_element} that contain [a_new_element]

# e.g., For the example above, returned_partition includes
# [[0, 11], [22]] and [[0], [11], [22]]]

    for _partition in some_partitions:  # e.g., [[0, 11]]
        appended_partition = copy.deepcopy(_partition)
        appended_partition.append([a_new_element])
        returned_partitions.append(appended_partition)
    # e.g., append [[0, 11], [22]] in the example

    return returned_partitions

def all_partitions_of(a_list):
    start=[[[int(a_list[0])]]]
    for i in range(len(a_list)-1):
        start=extend_partitions(start, a_list[i+1])
    return start



# OF all_partitions_of() ===========  print("[[[]]]<-->" + str(all_partitions_of([])) + '\n')  # one list--consisting of []

print("[[[333]]]<-->" + str(all_partitions_of([333])) + '\n')

print('all_partitions_of([0,22]):')
print(all_partitions_of([0,22]))
print("[[[0, 22]], [[0], [22]]]\n")

print('all_partitions_of([0,11,22]):')
print(all_partitions_of([0,11,22]))
print("[[[0, 22], [11]], [[0], [11, 22]], [[0, 11, 22]], [[0], [11], [22]], [[0, 11], [22]]]\n")

print('all_partitions_of([0,11,22,33]):')
print(all_partitions_of([0,11,22,33]))


print('all_partitions_of([7,8,1,3,5]):')
print(all_partitions_of([7,8,1,3,5]))

