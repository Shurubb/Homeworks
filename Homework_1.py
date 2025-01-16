class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lectures(self, lecture, grade):
        if isinstance(lecture, Lecturer) and self.courses_in_progress and lecture.courses_attached:
            if isinstance(grade, int) and (0 <= grade <= 10):
                lecture.grades += [grade]
            else:
                print("Оценка введена неверно")
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

lecturer_1 = Lecturer('Ivan', 'Ivanov')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Nikolay', 'Valuev')
lecturer_2.courses_attached += ['Java']

reviewer_1 = Reviewer('Petr', 'Petrov')
reviewer_1.courses_attached += ['Python']

reviewer_1.rate_hw(best_student, 'Python', 9)

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

best_student.rate_lectures(lecturer_1, 10)
best_student.rate_lectures(lecturer_2, 9)

print("student:", best_student.grades)
print("lec_1:", lecturer_1.grades)
print("lec_2:", lecturer_2.grades)
print(best_student.grades)
