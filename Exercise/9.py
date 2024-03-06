class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def calculate_average(self):
        total_marks = sum(self.marks.values())
        return total_marks / len(self.marks)

    def get_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return 'A'
        elif 80 <= average < 90:
            return 'B'
        elif 70 <= average < 80:
            return 'C'
        elif 60 <= average < 70:
            return 'D'
        else:
            return 'F'

    def display_info(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Average Marks:", self.calculate_average())


# Example usage:
student_marks = {'Math': 85, 'Science': 90, 'History': 75}
student1 = Student("John", "S001", student_marks)
student1.display_info()
print("Grade:", student1.get_grade())
