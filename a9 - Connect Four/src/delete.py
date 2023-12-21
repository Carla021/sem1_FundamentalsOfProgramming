from texttable import Texttable

t = Texttable()

header = []
for i in range(11):
    header.append(chr(ord('A') + i))
t.header(header + ['/'])

rows = []
for i in range(11):
    rows.append(' ')

for i in range(11):
    t.add_row(rows + ['[' + str(i + 1) + ']'])

print(t.draw())

def process_command(command):
    command = command.strip()
    tokens = command.split(" ", maxsplit=1)
    command = tokens[0]

    if len(tokens) == 1:
        return command, ""

    tokens = tokens[1]
    tokens.strip()

    return command, tokens


def process_user_command(self, command):
    command = command.strip()
    tokens = command.split(" ", maxsplit=1)
    command = tokens[0]

    if len(tokens) == 1:
        return command, ""

    tokens = tokens[1]
    tokens.strip()

    return command, tokens


class Animal:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def __str__(self):
        return f'Salut sunt {self.nume}!'

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        return Animal(self.nume + other.nume, 5)

    def __lt__(self, other):
        return self.varsta < other.varsta





caine = Animal('caine', 10)
pisica = Animal('pisica', 12)

print(caine, '\n', pisica)
lista = [caine, pisica]

print(lista)

a = caine + pisica

print(a)
print(caine < a)


def f(l):
    if l == [1]:
        raise ValueError()

    for e in l:
        if e % 2 == 1:
            return True
    return False

assert f([1]) == True
