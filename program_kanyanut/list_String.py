#Exercise1
nums_str = input("Enter integers separated by spaces: ").split()
numbers = [int(x) for x in nums_str]
print("Total items:", len(numbers))
if numbers:
    print("Last item:", numbers[-1])
print("Reversed list:", numbers[::-1])
if 5 in numbers:
    print("Yes 5 in Number")
else:
    print("No otherwise")
print("Number of 5s:", numbers.count(5))
if len(numbers) > 2:
    trimmed = numbers[1:-1]
    trimmed.sort()
    print("Sorted (without first & last):", trimmed)
else:
    print("Not enough elements to remove first and last.")
count_less_5 = 0
less_than_5 = [n for n in numbers if n < 5]
print("Numbers less than 5:", less_than_5)

#Exercise2
lst = [8, 9, 10]
lst[1] = 17            # Set second entry to 17
lst += [4, 5, 6]       # Add 4, 5, 6 to the end
lst.pop(0)             # Remove first entry
lst.sort()             # Sort the list
lst = lst * 2          # Double the list
lst.insert(3, 25)      # Insert 25 at index 3
print("Final list:", lst)

#Exercise3 string
s = input("Enter a string: ")

# 1. Total number of characters
print("Length:", len(s))

# 2. String repeated 10 times
print("Repeated 10 times:", s * 10)

# 3. First character
if s:
    print("First character:", s[0])

# 4. First three characters
print("First 3 characters:", s[:3])

# 5. Last three characters
print("Last 3 characters:", s[-3:])

# 6. String backwards
print("Backwards:", s[::-1])

# 7. Seventh character or message
if len(s) >= 7:
    print("Seventh character:", s[6])
else:
    print("String too short for seventh character")

# 8. String without first and last characters
print("Without first and last:", s[1:-1])

# 9. All caps
print("Uppercase:", s.upper())

# 10. Replace 'a' with 'e'
print("Replace a with e:", s.replace('a', 'e'))