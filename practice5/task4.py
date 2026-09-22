def read_grade(prompt):
    """Read an integer grade from 0 to 100."""
    while True:
        try:
            grade = int(input(prompt))

            if 0 <= grade <= 100:
                return grade

            print("Invalid grade. Enter a number from 0 to 100.")

        except ValueError:
            print("Invalid input. Enter an integer.")


def to_letter(grade):
    """Convert a 100-point grade to an ECTS letter."""
    if grade >= 90:
        return "A"

    if grade >= 82:
        return "B"

    if grade >= 74:
        return "C"

    if grade >= 64:
        return "D"

    if grade >= 60:
        return "E"

    return "F"


def average(grades):
    """Return the arithmetic mean of grades."""
    return sum(grades) / len(grades)


def count_above(grades, limit):
    """Count grades strictly greater than the given limit."""
    count = 0

    for grade in grades:
        if grade > limit:
            count += 1

    return count


def print_report(name, group, grades):
    """Print a report about the student's grades."""
    avg = average(grades)
    letter = to_letter(round(avg))

    best = max(grades)
    worst = min(grades)
    above_average = count_above(grades, avg)

    print()
    print(f"Student: {name}")
    print(f"Group: {group}")
    print(f"Grades: {grades}")
    print(f"Average: {avg:.2f}")
    print(f"Letter grade: {letter}")
    print(f"Best grade: {best}")
    print(f"Worst grade: {worst}")
    print(f"Grades above average: {above_average}")


def main():
    """Run the grade processing program."""
    name = "Illia"
    group = "IT-31"

    number_of_grades = max(3, len(name))

    grades = []

    print(f"{name} {group}")

    print(f"Enter {number_of_grades} grades:")

    for i in range(number_of_grades):
        grade = read_grade(f"Grade {i + 1}: ")
        grades.append(grade)

    print_report(name, group, grades)


main()