def main():
    userInput = int(input("Enter number for Fibonacci Sequence: "))
    firstNum = 0
    secondNum = 1
    count = 1

    
    while count <= userInput:
        print(firstNum)
        secondNum += firstNum
        firstNum = secondNum - firstNum
        count += 1
        
    

main()