student_list = []
mentor_list = []
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        student_list.append(self)

    def avarage_student_score(self):  # Подсчет среднего балла за лекции Студентов
        avg = []
        for value in self.grades.values():
             avg.extend(value)
        res = sum(avg) / len(avg)
        return round(res, 2)


    def rate_lector(self, lector, course, grade):  # Оцениваем Лекторов
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        stud = f'Имя: {self.name}\nФамилия:  {self.surname}\nСредняя оценка за леции: {self.grades}\nКурсы в процессе изучения:  {self.courses_in_progress}\n' \
               f'Завершенные курсы: {self.finished_courses}'
        return stud



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_in_progress = []
        self.grades = {}
        mentor_list.append((self))

    def avarage_lector_score(self):  # Подсчет среднего балла за лекции Лекторов
        avg = []
        for value in self.grades.values():
             avg.extend(value)
        res = sum(avg) / len(avg)
        return round(res, 2)




    def __str__(self):  # Перевод в магический метод
        lec = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за леции: {self.avarage_lector_score()}'
        return lec


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):  # Оцениваем Студентов
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        rev = f'Имя: {self.name}\nФамилия: {self.surname}'
        return rev


def student_rates(student_list, course='Python'):
    asd = []
    for stud in student_list:
        if course in stud.grades.keys():
            for grade in stud.grades.values():
                asd += grade
                result = sum(asd)/len(asd)
                return result

def mentor_rates(mentor_list, course='Python'):
    asd = []
    for men in mentor_list:
        if course in men.grades.keys():
            for grade in men.grades.values():
                asd += grade
                result = sum(asd)/len(asd)
                return result


first_student = Student('Ivan', 'Ivanov', 'male')
first_student.courses_in_progress += ['Python', 'JavaScript']
first_student.finished_courses += ['EnglishDom', 'Git']
second_student = Student('Danil', 'Danilov', 'male')
second_student.courses_in_progress += ['Python', 'Java']
second_student.finished_courses += ['EnglishDom']

first_mentor = Lecturer('Roman', 'Romanov')
first_mentor.courses_attached += ['Python', 'JavaScript']
second_mentor = Lecturer('Ilya', 'Ilyin')
second_mentor.courses_attached += ['Python','Java']

first_reviewer = Reviewer('Alexander','Alexandrov')
first_reviewer.courses_attached += ['Python', 'JavaScript']
second_reviewer = Reviewer('Peter','Petrov')
second_reviewer.courses_attached += ['Python', 'JavaScript']
first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Python', 6)
first_reviewer.rate_hw(first_student, 'Python', 6)
second_reviewer.rate_hw(second_student, 'Python', 8)
second_reviewer.rate_hw(second_student, 'Python', 6)
second_reviewer.rate_hw(second_student, 'Python', 4)
first_student.rate_lector(first_mentor, 'Python', 10)
first_student.rate_lector(first_mentor, 'Python', 3)
first_student.rate_lector(first_mentor, 'Python', 5)
second_student.rate_lector(second_mentor, 'Python', 10)
second_student.rate_lector(second_mentor, 'Python', 4)
second_student.rate_lector(second_mentor, 'Python', 3)

print(first_student)

