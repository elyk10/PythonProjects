def mergeSort(ls):
    if len(ls) <= 1:
        return ls
    
    middle = len(ls)//2
    left = mergeSort(ls[:middle])
    right = mergeSort(ls[middle:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result



def main():
    ls = [2, 1, 55, 3, 20, 5]
    print(ls)
    print(mergeSort(ls))


main()