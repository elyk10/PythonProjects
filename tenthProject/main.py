def insertSort(ls):

    for i in range(1,len(ls)):
        temp = ls[i]
        j = i - 1

        while j >= 0 and ls[j] > temp:
            ls[j + 1] = ls[j]
            j -= 1

        ls[j + 1] = temp

    return ls



def main():
    ls = [1, 4, 3, 7, 2, 10, 8]

    print(ls)
    print(insertSort(ls))

main()