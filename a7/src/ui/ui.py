from domain.exceptions import StudentValidationException
from domain.student import Student
from repository.studentrepo import RepoException
from services.__init__ import *


class UI:
    def __init__(self, service):
        self._service = service

    def add(self, student: Student):
        try:
            self._service.add(student)
        except StudentValidationException as e:
            print(e.msg)
        except RepoException as re:
            print(re)

    def display_students(self):
        for student in self._service.get_all():
            print(str(student))

    def filter(self, group):
        self._service.filter(group)

    def undo(self):
        try:
            self._service.undo()
        except ValueError as e:
            print(e)

    @staticmethod
    def _print_menu():
        print("\n1. Add a student")
        print("2. Display students")
        print("3. Filter the lists")
        print("4. Undo")
        print("0. Exit the program\n")

    @staticmethod
    def _print_second_menu():
        print("1. Text file repository")
        print("2. Binary file repository")
        print("3. Memory repository")

    def _input_command():
        command = input(">")
        return command

    def start(self):
        while True:
            self._print_menu()
            option = self.get_input()
            if option == 1:
                id = int(input("id: "))
                name = input("name: ")
                group = int(input("group: "))
                self.add(Student(id, name, group))

            elif option == 2:
                self.display_students()

            elif option == 3:
                group = int(input("group: "))
                self.filter(group)

            elif option == 4:
                self.undo()

            elif option == 0:
                print("Exiting...")
                return
            else:
                print("Invalid input")

    def get_input(self):
        try:
            option = int(input(">"))
            return option
        except ValueError as ve:
            print(ve)
            return self.get_input()
