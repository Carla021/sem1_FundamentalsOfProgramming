import pickle
import random

from domain.student import Student


class RepoException(Exception):
    pass


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


class StudentRepo(object):
    def __init__(self):
        self._data = {}

    def add(self, new_student: Student):
        '''
        adds a new student only if it doesn't already exist in repo
        :param new_student: the student that will be added
        '''
        if new_student.id in self._data:
            raise RepoException("Student already in repo")
        self._data[new_student.id] = new_student

    def delete_student(self, student_id: int):
        self._data.pop(student_id)

    def get_all(self):
        return list(self._data.values())

    def get_all_to_dict(self):
        return self._data

    def __len__(self):
        return len(self._data)

    def change_data(self, students):
        self._data.clear()
        for student in students:
            self.add(student)


class StudentRepoBinFile(StudentRepo):
    def __init__(self, file_name="repository/students.bin"):
        super().__init__()
        self._file_name = file_name
        # self.generate_random(10)
        self.load_file()

    def add(self, new_student: Student):
        '''
        this function adds a new student
        '''
        # call the add() method on the super class
        super().add(new_student)
        self._save_file()

    def load_file(self):
        # r - read, b - binary
        input_file = open(self._file_name, "rb")
        students = pickle.load(input_file)

        for student in students:
            super().add(student)
        input_file.close()

    def _save_file(self):
        # w - write mode (overwrite), b - binary mode
        fout = open(self._file_name, "wb")
        pickle.dump(self.get_all(), fout)
        fout.close()

    def delete_student(self, student_id):
        super().delete_student(student_id)
        self._save_file()

    def generate_random(self, n):
        for student in generate_students(n):
            self.add(student)

    def change_data(self, students):
        super().change_data(students)
        self._save_file()


class StudentRepoTextFile(StudentRepo):

    def __init__(self, file_name="repository/students.txt"):
        super().__init__()
        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        """
        load the students from a text file
        :return:
        """
        lines = []

        try:
            fin = open(self._file_name, "rt")
            lines = fin.readlines()
            fin.close()
        except IOError:
            pass

        for line in lines:
            current_line = line.split(",")
            new_student = Student(int(current_line[0].strip()), current_line[1].strip(), int(current_line[2].strip()))
            super().add(new_student)

    def _save_file(self):
        """
        Save all students to a text file
        :return:
        """
        fout = open(self._file_name, "wt")

        for student in self.get_all():
            student_string = str(student.id) + "," + str(student.name) + "," + str(student.group) + "\n"
            fout.write(student_string)

        fout.close()

    def add(self, new_student: Student):
        '''
        adds a new student
        :param new_student: the added student
        '''
        super().add(new_student)
        self._save_file()

    def delete_student(self, student_id):
        super().delete_student(student_id)
        self._save_file()

    def change_data(self, students):
        super().change_data(students)
        self._save_file()

def test_add():
    repo = StudentRepo()
    student = Student(1, "Ion", 912)
    repo.add(student)
    ex = {1: student}
    assert ex == repo.get_all_to_dict()


if __name__ == "__main__":
    test_add()