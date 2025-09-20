def main():
    file = open("grades.txt", "w")

    loop = True

    while loop:
        subject = input("Enter the subject: ")
        grade = input("Enter the grade: ")
        try:
            gradeNumber = int(grade)
        except:
            print("Not valid input.")
            continue
        file.write((subject + ": " + grade + "\n"))
        moveForward = input("Do you have more to enter (yes/no)?")
        if moveForward != "yes":
            loop = False

    file = open("grades.txt", "r")
    lines = file.readlines()
    total = 0
    for line in lines:
        total += int(line.split(":")[1].strip())

    print("Your average is: ", total/len(lines))

    file.close()

main()