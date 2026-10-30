# Program 6: List Operations

numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])
print("Total Elements:", len(numbers))
print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# Adding an element
numbers.append(60)
print("After Adding:", numbers)

# Removing an element
numbers.remove(20)
print("After Removing:", numbers)

# Sorting
numbers.sort()
print("Sorted List:", numbers)

# Loop through list
print("List Elements:")

for item in numbers:
    print(item)
