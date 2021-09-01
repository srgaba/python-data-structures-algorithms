def insertion(list):
    length = len(list)
    for i in range(0, length):
        for y in reversed(range(1, i+1)):
            if list[y-1] > list[y]:
                tmp = list[y-1]
                list[y-1] = list[y]
                list[y] = tmp
            else:
                break 
    return list


print(insertion([0, 4, 1, 3, 6, 10, 5, 2]))