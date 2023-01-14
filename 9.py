with open('9.txt') as file:
    n, k = [int(elem) for elem in file.readline().split(' ')]
    arr = []
    for line in file:
        coord = int(line)
        if len(arr) == 0:
            arr.append((coord, 0))
            continue
        arr = [elem for elem in arr if coord-elem[0] <= k]
        min_num_before = min([elem[1] for elem in arr])
        arr.append((coord, min_num_before+1))
    print(arr[-1][1])
