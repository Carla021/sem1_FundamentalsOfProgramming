def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def dateCalculation(monthsYears, day, year):
    for i in range(len(monthsYears)):
        if day <= monthsYears[i]:
            print(year, i + 1, day)
            break
        else:
            day -= monthsYears[i]


def main():
    monthsLeapYears = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    monthsYears = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = int(input())
    day = int(input())

    if isLeapYear(year):
        dateCalculation(monthsLeapYears, day, year)
    else:
        dateCalculation(monthsYears, day, year)

main()