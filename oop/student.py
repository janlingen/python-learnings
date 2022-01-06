class Student:
    all_studs = []

    def __init__(self, name, grade):
        self.name = name
        self._grade = grade
        Student.all_studs.append(self)

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, x):
        if 0 <= x <= 100:
            self._grade = x
        else:
            raise ValueError("New grade not in the accepted range of [0-100].")

    @staticmethod
    def calculate_average_grade(students):
        if len(students) == 0:
            return -1
        else:
            total = 0
            for student in students:
                total += student._grade
            return total/len(students)

    @classmethod
    def get_average_grade(cls):
        return cls.calculate_average_grade(cls.all_studs)

    @classmethod
    def get_best_student(cls):
        best_stud = None
        best_grad = 0
        for student in cls.all_studs:
            if student._grade > best_grad:
                best_stud = student
                best_grad = student._grade
        return best_stud
