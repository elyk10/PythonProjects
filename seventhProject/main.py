def main():
    num = int(input("Enter number to print the prime numbers up to: "))

    for i in range(1, num + 1):
        prime = False
        for j in range(2, i + 1):
            if i % j == 0 and i != j:
                prime = False
                break
            else:
                prime = True

        if prime:
            print("Prime number: ", i)


main()