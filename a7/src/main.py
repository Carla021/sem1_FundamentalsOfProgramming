from repository.studentrepo import StudentRepo, generate_students
from repository.studentrepo import StudentRepoBinFile
from repository.studentrepo import StudentRepoTextFile
from services.services import Services
from ui.ui import UI


if __name__ == "__main__":

    UI._print_second_menu()
    command = UI._input_command()

    if command not in ["text", "memory", "binary"]:
        raise ValueError("Invalid implementation method")

    elif command == "text":
        repository = StudentRepoTextFile("repository/students.txt")
    elif command == "binary":
        repository = StudentRepoBinFile("repository/students.bin")
    elif command == "memory":
        repository = StudentRepo()
        for student in generate_students(10):
            repository.add(student)

    services = Services(repository)
    ui = UI(services)

    ui.start()
