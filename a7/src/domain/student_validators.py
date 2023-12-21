from domain.exceptions import StudentValidationException


class StudentValidator:
    @staticmethod
    def _is_group_valid(group):
        return int(group) == group and group > 0

    @staticmethod
    def _is_id_valid(id):
        return int(id) == id

    def validate(self, student):
        errors = []
        if not StudentValidator._is_group_valid(student.group):
            errors.append('Invalid group')
        if not StudentValidator._is_id_valid(student.id):
            errors.append('Invalid id')

        if len(errors) > 0:
            raise StudentValidationException(errors)

'''
def process_command(user_command):
    # remove leading and trailing whitespace
    user_command = user_command.strip()
    #split the command into two - command word and params
    tokens = user_command.split(maxsplit=1)
    command_word = tokens[0]
    
    if len(tokens) > 1:
        tokens = tokens[1].split(" ")
        for i in range(len(tokens)):
            tokens[i] = tokens[i].strip()
        # command parameters
        command_params = tokens
    else:
        command_params = []
    return command_word, command_params
'''

def process_command(command):
    command = command.strip()
    tokens = command.split(" ", maxsplit=1)
    command = tokens[0]

    if len(tokens) > 1:
        tokens = tokens[1].split(" ")
        for i in range(len(tokens)):
            tokens[i] = tokens[i].strip()
        return command, tokens

    return command, ""

def process_user_command(command):
    command = command.strip()
    tokens = command.split(" ", maxsplit=1)
    command = tokens[0]

    if len(tokens) == 1:
        return command, ""

    tokens = tokens[1].strip()
    return command, tokens


