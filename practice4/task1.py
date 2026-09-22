print("Illia Basalukk, IT-31")

d = 11
c = 8

count = 0
total = 0
product = 1
even = 0
odd = 0

print("Numbers from 11 to 31:", end=" ")

for number in range(d, 32):
    print(number, end=" ")

    count += 1
    total += number
    product *= number

    if number % 2 == 0:
        even += 1
    else:
        odd += 1

average = total / count

print()
print(f"Count: {count}")
print(f"Sum: {total}")
print(f"Product: {product}")
print(f"Average: {average:.2f}")
print(f"Even: {even}, odd: {odd}")

# while version

count_while = 0
total_while = 0
product_while = 1
even_while = 0
odd_while = 0

number = d

while number <= 31:
    count_while += 1
    total_while += number
    product_while *= number

    if number % 2 == 0:
        even_while += 1
    else:
        odd_while += 1

    number += 1

average_while = total_while / count_while

print()
print("# while version")
print(f"Count: {count_while}")
print(f"Sum: {total_while}")
print(f"Product: {product_while}")
print(f"Average: {average_while:.2f}")
print(f"Even: {even_while}, odd: {odd_while}")

print()
print("Countdown:", end=" ")

for number in range(c, 0, -1):
    print(number, end=" ")

print()