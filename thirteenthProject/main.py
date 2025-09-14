import math

def calcAverage(ls):
    sum = math.fsum(ls)
    return sum / len(ls)


def main():
    print(calcAverage([1,2,3]))
    print(calcAverage([2,5,6,7,9]))


main()

