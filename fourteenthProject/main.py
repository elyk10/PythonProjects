from datetime import date

def main():
    loop = True

    while loop:
        action = int(input("Enter 1 to write in your diary, 2 to read from, and 3 to exit: "))
        match action:
            case 1:
                fileName = input("Enter file name: ")
                file = open(fileName, "a")
                entry = input("Enter diary entry: ")
                file.write(entry)
                timeStamp = input("Would you like to use a timestamp (yes/no)?")
                if timeStamp == "yes":
                    file.write(str(date.today()))
            case 2:
                fileName = input("Enter file name: ")
                try:
                    file = open(fileName, "r")
                except:
                    print("File not found")
                    loop = False
            case 3:
                loop = False
            case _:
                print("Invalid input, program will exit.")
                loop = False

main()