class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades.setdefault(subject, []).append(grade)

    def average(self):
        total, count = sum(map(sum, self.grades.values())), sum(map(len, self.grades.values()))
        return total / count if count else 0

    def letter_grade(self, avg):
        if avg>=90:
            return 'O'
        if avg>=80:
            return 'A'
        if avg>=70:
            return 'B'
        if avg>=60:
            return 'B+'
        if avg>=50:
            return 'C'
        
        
        else:
            return 'F'
    def gpa(self, avg):
        if avg>=90:
            return 10.0
        if avg>=80:
            return 9.0
        if avg>=70:
            return 8.0
        if avg>=60:
            return 7.0
        if avg>=50:
            return 6.0
        if avg>=40:
            return 0.0
        
    def display(self):
        avg = self.average()
        print(f"Student: {self.name}\nGrades: {self.grades}\nAverage: {avg:.2f}\nLetter Grade: {self.letter_grade(avg)}\nGPA: {self.gpa(avg):.2f}")

def main():
    student = Student(input("Enter student's name: "))
    while True:
        subject = input("Enter subject: ")
        if subject.lower() == 'submit': break
        try: student.add_grade(subject, float(input(f"Enter grade for {subject}: ")))
        except ValueError: print("Invalid input. Please enter a numeric grade.")
    student.display()

if __name__ == "__main__":
    main()
