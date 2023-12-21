# Determine the age of a person, in number of days.
# Take into account leap years, as well as the date of birth and current date (year, month, day).
# Do not use Python's inbuilt date/time functions.


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


def daysOfCurrentYearCalculation(monthsYears, monthCurrentDate):
    ageOfPerson = 0
    for i in range(0, monthCurrentDate):
        ageOfPerson += monthsYears[i]
    return ageOfPerson


def daysOfBirthYearCalculation(monthsYears, monthBirthDate):
    ageOfPerson = 0
    for i in range(monthBirthDate, 12):
        ageOfPerson += monthsYears[i]
    return ageOfPerson


def main():
    yearDateOfBirth = int(input())
    monthBirthDate = int(input())
    dayBirthDate = int(input())
    yearCurrentDate = int(input())
    monthCurrentDate = int(input())
    dayCurrentDate = int(input())
    ageOfPerson = calculateAgeOfPerson(dayBirthDate, dayCurrentDate, monthBirthDate, monthCurrentDate, yearCurrentDate, yearDateOfBirth)

    print(ageOfPerson)


def calculateAgeOfPerson(dayBirthDate, dayCurrentDate, monthBirthDate, monthCurrentDate, yearCurrentDate, yearDateOfBirth):

    monthsLeapYears = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    monthsYears = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ageOfPerson = 0
    for i in range(yearDateOfBirth + 1, yearCurrentDate):
        if isLeapYear(i):
            ageOfPerson += 366
        else:
            ageOfPerson += 365
    
    if yearCurrentDate > yearDateOfBirth:
        if isLeapYear(yearCurrentDate):
            ageOfPerson += daysOfCurrentYearCalculation(monthsLeapYears, monthCurrentDate)
        else:
            ageOfPerson += daysOfCurrentYearCalculation(monthsYears, monthCurrentDate)
    ageOfPerson += dayCurrentDate
    if yearCurrentDate > yearDateOfBirth:
        if isLeapYear(yearCurrentDate):
            ageOfPerson += daysOfBirthYearCalculation(monthsLeapYears, monthBirthDate)
        else:
            ageOfPerson += daysOfBirthYearCalculation(monthsYears, monthBirthDate)
    ageOfPerson -= dayBirthDate
    return ageOfPerson


main()

# def test1():
#     assert calculateAgeOfPerson(21, 11, 3, 10, 2022, 2003) == 7144
#     assert calculateAgeOfPerson(21, 21, 3, 3, 2022, 2022) == 0
#
# def main_test() :
#     test1()
#
# main_test()