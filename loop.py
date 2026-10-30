# Program 2: For Loop

print("Numbers from 1 to 10")

for i in range(1, 11):
    print(i)


# Program 3: While Loop

print("\nWhile Loop")

i = 1

while i <= 10:
    print(i)
    i += 1


# Program 4: Multiplication Table

num = int(input("\nEnter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
