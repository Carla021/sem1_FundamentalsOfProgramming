'''
The sequence a = a1, ..., an with distinct integer elements is given. Determine all subsets of at least two elements with the property:
    The elements in the subset are in increasing order
    Any two consecutive elements in the subsequence have at least one common digit
'''

def commonDigit(number1: int, number2: int):
    appArr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    while number1 > 0:
        appArr[number1 % 10] = 1
        number1 //= 10

    while number2 > 0:
        if appArr[number2 % 10] == 1:
            appArr[number2 % 10] += 1
        number2 //= 10

    for i in range(len(appArr)):
        if appArr[i] == 2:
            return True

    return False


def check_condition(solution_list: list, current_index: int):

    for index in range(0, current_index):
        if solution_list[index] == solution_list[current_index]:
            return 0

    for index in range(1, current_index + 1):
        if solution_list[index] < solution_list[index - 1]:
            return 0

    for index in range(1, current_index + 1):
        if commonDigit(solution_list[index], solution_list[index - 1]) == False:
            return 0

    return 1


def print_solutions(solution_list: list, current_index: int):
    for i in range(current_index + 1):
        print(solution_list[i], end = ' ')
    print(' ', end = "\n")


def next_elem(x: list, a: list):
    if x[-1] is None:
        return a[0]

    index = a.index(x[-1])

    if index < len(a) - 1:
        return a[index + 1]

    return None


def back_iter(a: list):
    solution = [None]

    while len(solution) > 0:
        el = next_elem(solution, a)

        while el is not None:
            solution[-1] = el
            if check_condition(solution, len(solution) - 1):
                if len(solution) >= 2:
                    print(solution)

                solution.append(None)
                break

            el = next_elem(solution, a)

        if el is None:
            solution = solution[:-1]

'''
def backtracking_iterative(solution_list: list, n: int, a: list):
    current_index = 0
    while current_index > -1:
        if current_index < n:
            solution_list.append(a[current_index])
            if check_condition(solution_list, current_index):
                if current_index > 0:
                    print_solutions(solution_list, current_index)
                current_index += 1
            else:
                current_index -= 1
                solution_list.pop()
        else:
            current_index -= 1
            solution_list.pop()
'''


def backtracking_recursive(solution_list: list, n: int, a: list, current_index: int):
    for index in range(0, n):
        solution_list.append(a[index])
        if check_condition(solution_list, current_index):
            if current_index > 0:
                print_solutions(solution_list, current_index)
            '''
            if len(solution_list):
                solution_list.pop()
            '''
            backtracking_recursive(solution_list, n, a, current_index + 1)
        else:
            if len(solution_list):
                solution_list.pop()
    if len(solution_list):
        solution_list.pop()


def main():
    solution_list = []
    a = [23, 24, 46, 77, 88, 89, 100, 123, 125, 36]
    #a = [23, 24, 26, 88]
    #n = int(input("n = "))
    n = 10
    #for i in range(0, n):
    #    value = int(input())
    #    a.append(value)
    option = int(input("enter 1 - iterative backtracking; 2 - recursive backtracking: "))
    if option == 1:
        back_iter(a)
    else:
        backtracking_recursive(solution_list, n, a, 0)


main()

'''
Time Complexity: O(2^n). Total number of subsets generated are 2^n,
So Time Complexity is O(2^n). 
'''