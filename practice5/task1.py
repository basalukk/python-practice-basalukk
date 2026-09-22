name = "Illia"
surname = "Basalukk"
group = "IT-31"
year = 2009


def print_card():
    """Prints the student's personal information."""
    print(f"Name: {name} {surname}")
    print(f"Group: {group}")
    print(f"Birth year: {year}")


print(f"{name} {surname}, {group}")

print("--- no parameters, call 1 ---")
print_card()

print("--- no parameters, call 2 ---")
print_card()

print("--- no parameters, call 3 ---")
print_card()


def print_card_args(name, surname, group, year):
    """Prints student information received through parameters."""
    print(f"{name} {surname}, {group}, {year}")


print("--- positional arguments ---")
print_card_args("Illia", "Basalukk", "IT-31", year)

print("--- keyword arguments ---")
print_card_args(
    year=year,
    group="IT-31",
    surname="Basalukk",
    name="Illia"
)

print("--- mixed arguments ---")
print_card_args("Illia", "Basalukk", group="IT-31", year=year)


def print_card_default(name, surname, year, group="IT-31"):
    """Prints student information with a default group."""
    print(f"{name} {surname}, {group}, {year}")


print("--- default group ---")
print_card_default("Illia", "Basalukk", year)


print("--- missing arguments error ---")
try:
    print_card_args("Ivan")
except TypeError as error:
    print(f"TypeError: {error}")