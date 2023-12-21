class Student:
    '''
        Add a new student. Each student must have:
            -> a valid id
            -> a name
            -> a group
        '''

    def __init__(self, id: int, name: str, group: int):
        self.__id = id
        self.__name = name
        self.__group = group

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def group(self):
        return self.__group

    @id.setter
    def id(self, new_id):
        self.__id = new_id

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @group.setter
    def group(self, new_group):
        self.__group = new_group

    def __str__(self):
        return str(self.__id) + "," + self.__name + "," + str(self.__group)


def test_student():
    new_student = Student(22, "Ion", 915)
    assert new_student.id == 22, "error!"
    assert new_student.name == "Ion", "error!"
    assert new_student.group == 915, "error!"
    assert str(new_student) == "22,Ion,915", "error!"

    new_student.group = 916
    assert str(new_student) == "22,Ion,916", "error!"


if __name__ == "__main__":
    test_student()


