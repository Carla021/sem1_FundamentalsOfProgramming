import copy
import random

from domain.student import Student
from domain.student_validators import StudentValidator
from repository.studentrepo import StudentRepo


class Services:
    def __init__(self, repo):
        self._repo = repo
        self.__changes = 0
        self.__history = []
        self.__history.append(copy.deepcopy(self._repo.get_all()))
        self.__validator = StudentValidator()

    def add(self, student: Student):
        """
        this function adds a new student and saves the changes in the history
        """
        self.__validator.validate(student)
        self._repo.add(student)
        self.__history.append(copy.deepcopy(self._repo.get_all()))
        self.__changes += 1

    def filter(self, group: int):
        '''
        this function deletes all students from a given group
        '''
        for student in self._repo.get_all():
            if student.group == group:
                self._repo.delete_student(student.id)
        self.__changes += 1
        self.__history.append(copy.deepcopy(self._repo.get_all()))

    def undo(self):
        if self.__changes == 0:
            raise ValueError("No changes applied!")

        self.__changes -= 1
        self._repo.change_data(copy.deepcopy(self.__history[len(self.__history) - 2]))
        self.__history.pop()

    def get_all(self):
        return self._repo.get_all()

    def get_all_to_dict(self):
        return self._repo.get_all_to_dict()

    @staticmethod
    def generate_students(n: int):
        """
        Generates n students instances
        :param n: int
        :return: A list of n students
        """
        name = ["Vlad", "Roxana", "Bogdan", "Ion", "Lorena", "Bianca", "Sorin", "David", "Daria", "Carla"]
        result = []

        while n > 0:
            id = random.randint(-100, 101)
            group = random.randint(911, 918)
            student_name = name[random.randint(0, 9)]
            result.append(Student(id, student_name, group))
            n -= 1

        return result


def test_add():
    repo = StudentRepo()
    service = Services(repo)
    student = Student(4, "George", 911)
    service.add(student)
    all_students_check = {4: student}
    assert repo.get_all_to_dict() == all_students_check


if __name__ == "__main__":
    test_add()
