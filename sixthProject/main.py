def main():
    num = int(input("Enter number to calculate a factorial for: "))

    result = 1

    for i in range(1, num + 1):
        result *= i

    print("The result is: ", result)

main()