class Student:

    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def displayInfo(self):
        print(f"The student, {self.name} age {self.age} has the following grades: {self.grades}")

    def averageGrade(self):
        sum = self.grades.sum()
        return sum / len(self.grades)
    

def main():
    loop = True

    students = [Student("Kyle", 15, [99, 98, 96])]

    while loop:
        addStudent = input("Would you like to add a student to the database (yes/no)?")
        if addStudent == "yes":
            name = input("What is there name? ")
            age = input("What is their age? ")
            numOfGrades = int(input("How many grades would you like to input? "))
            grades = []
            for i in range(0, numOfGrades):
                grades.append(int(input("Enter grade: ")))

            students.append(Student(name, age, grades))
        else:
            loop = False

    print("Now displaying all students:")
    for i in students:
        i.displayInfo()

main()