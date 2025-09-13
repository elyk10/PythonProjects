def bubbleSort(ls):
    for i in range(0, len(ls)):
        for j in range(0, len(ls) - i - 1):
            if ls[j] > ls[j + 1]:
                temp = ls[j]
                ls[j] = ls[j+1]
                ls[j+1] = temp

    return ls

def main():
    ls = [3, "hello", 44, 5, 9, 1]
    ls = bubbleSort(ls)
    print(ls)

main()


