def mean(numbers):
    if numbers:
        if isinstance(numbers, dict):
            res=[]
            for value in numbers.values():
                res += value
            return sum(res)/len(res)
        else:
            return sum(numbers)/len(numbers)
    else:
        return 0


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecturer(self, lecturer, grade):
        if isinstance(lecturer, Lecturer) and self.courses_in_progress and lecturer.courses_attached:
            if isinstance(grade, int) and (0 <= grade <= 10) :
                lecturer.grades += [grade]
            else:
                print("Оценка введена неверно")
        else:
            return 'Ошибка'
    def __str__(self):
        info = str(f"Имя: {self.name}\n"
                   f"Фамилия: {self.surname}\n"
                   f"Средняя оценка: {mean(self.grades)}\n"
                   f"Курсы в процессе обучения: {', '.join(self.courses_in_progress)}\n"
                   f"Завершенные курсы: {', '.join(self.finished_courses)}\n")
        return info
    def __lt__(self, other):
        return mean(self.grades) < mean(other.grades)
    def __gt__(self, other):
        return mean(self.grades) > mean(other.grades)
    def __le__(self, other):
        return mean(self.grades) <= mean(other.grades)
    def __ge__(self, other):
        return mean(self.grades) >= mean(other.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {mean(self.grades)}"
    def __lt__(self, other):
        return mean(self.grades) < mean(other.grades)
    def __gt__(self, other):
        return mean(self.grades) > mean(other.grades)
    def __le__(self, other):
        return mean(self.grades) <= mean(other.grades)
    def __ge__(self, other):
        return mean(self.grades) >= mean(other.grades)


class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['1C']

student_2 = Student('Ron', 'Wuizli', 'your_gender')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Exel']
student_2.finished_courses += ['PHP']

lecturer_1 = Lecturer('Ivan', 'Ivanov')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Java']

lecturer_2 = Lecturer('Nikolay', 'Valuev')
lecturer_2.courses_attached += ['JS']

reviewer_1 = Reviewer('Petr', 'Petrov')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']

reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 8)

student_1.rate_lecturer(lecturer_1, 10)
student_1.rate_lecturer(lecturer_1, 8)
student_2.rate_lecturer(lecturer_1, 9)
student_1.rate_lecturer(lecturer_2, 5)

print(f"reviewer_1: {reviewer_1} ")
print(f"lecturer_1: {lecturer_1} ")
print(f"lecturer_2: {lecturer_2} ")
print(f"student_1: {student_1} ")
print(f"student_2: {student_2} ")

print("lecturer_1 < lecturer_2 ==>", lecturer_1 > lecturer_2)
print("student_1 > student_2 ==>", student_1 > student_2)