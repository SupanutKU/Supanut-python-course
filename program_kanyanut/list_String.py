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
lst[1] = 17
lst += [4, 5, 6]
lst.pop(0)
lst.sort()
lst = lst * 2
lst.insert(3, 25)
print("Final list:", lst)

#Exercise3 string
string = input("Enter a string: ")
print("Length:", len(s))
print("Repeated 10 times:", string * 10)
if string:
    print("First character:", string[0])
print("First 3 characters:", string[:3])
print("Last 3 characters:", string[-3:])
print("Backwards:", string[::-1])
if len(string) >= 7:
    print("Seventh character:", string[6])
else:
    print("String too short for seventh character")
print("Without first and last:", string[1:-1])
print("Uppercase:", string.upper())
print("Replace a with e:", string.replace('a', 'e'))