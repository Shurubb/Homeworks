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


def courses_rating(persons, course):
    res = 0
    lenth = 0
    for person in persons:
        if course in person.grades:
            if person.grades[course]:
                res += mean(person.grades[course])
                lenth += 1
    if lenth != 0:
        return res/lenth


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if isinstance(grade, int) and (0 <= grade <= 10) :
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
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
        self.grades = {}
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

students = [Student('Ruoy', 'Eman', 'your_gender'),
            Student('Boris', 'Yeltsin', 'your_gender')]
students[0].courses_in_progress += ['Python']
students[0].courses_in_progress += ['Git']
students[0].finished_courses += ['1C']
students[1].courses_in_progress += ['Python']
students[1].finished_courses += ['Exel']
students[1].finished_courses += ['PHP']

lecturers = [Lecturer('Ivan', 'Ivanov'),
            Lecturer('Nikolay', 'Valuev')]
lecturers[0].courses_attached += ['Python']
lecturers[0].courses_attached += ['Java']
lecturers[1].courses_attached += ['JS']

reviewers = [Reviewer('Petr', 'Petrov'),
             Reviewer('Ivan', 'Grozny')]
reviewers[0].courses_attached += ['Python']
reviewers[0].courses_attached += ['Git']
reviewers[1].courses_attached += ['Calc']
reviewers[1].courses_attached += ['Word']

reviewers[0].rate_hw(students[0], 'Python', 7)
reviewers[0].rate_hw(students[0], 'Python', 10)
reviewers[0].rate_hw(students[0], 'Git', 10)
reviewers[1].rate_hw(students[1], 'Python', 9)
reviewers[1].rate_hw(students[1], 'Python', 8)

students[0].rate_lecturer(lecturers[0], 'Python', 10)
students[0].rate_lecturer(lecturers[0], 'Python', 8)
students[1].rate_lecturer(lecturers[0], 'Python', 9)
students[1].rate_lecturer(lecturers[1], 'Java', 5)

print(f"reviewers[0]: {reviewers[0]} ")
print(f"lecturers[0]: {lecturers[0]} ")
print(f"lecturers[1]: {lecturers[1]} ")
print(f"students[0]: {students[0]} ")
print(f"students[1]: {students[1]} ")

print("lecturers[0] < lecturers[1] ==>", lecturers[0] > lecturers[1])
print("students[0] > students[1] ==>", students[0] > students[1])
print(f"\nСредняя оценка домашних работ по Python: {courses_rating(students, 'Python')}")
print(f"Средняя оценка лекторов по курсу Python: {courses_rating(lecturers, 'Python')}")