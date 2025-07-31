"""
Number List Operations

Ask user to input 10 numbers and store them in a list
Display the original list

Create and display:

List of even numbers
List of odd numbers
List of numbers greater than the average


Show statistics: sum, average, min, max

"""

def number_operations():
    numbers = []
    
    # Get 10 numbers from user
    print("Enter 10 numbers:")
    for i in range(10):
        # Your code here
        num = int(input(f"Number {i+1}: "))
        numbers.append(num)
                
    
    # Display original list
    print(f"Original numbers: {numbers}")
    
    # Create filtered lists
    even_numbers = [i for i in numbers if i % 2 == 0]
    odd_numbers = [i for i in numbers if i % 2 == 1]
    
    # Calculate average
    average = sum(numbers) / len(numbers)
    
    # Numbers greater than average
    above_average = [i for i in numbers if i > average]
    
    # Display results
    # Your code here
    while True:
        print("1 Even numbers\n2 Odd numbers\n3 Numbers greater than average\n4 Show statistics: sum, average, min, max\n5 Exit")
        choice = input("Choose option: ")
        if choice == "1":
            print(f"Even numbers: {even_numbers}")
        if choice == "2":
            print(f"Odd numbers: {odd_numbers}")
        elif choice == "3":
            print(f"Numbers greater than average ({average:.2f}): {above_average}")
        elif choice == "4":
            print(f"Sum: {sum(numbers)}")
            print(f"Average: {average:.2f}")
            print(f"Min: {min(numbers)}")
            print(f"Max: {max(numbers)}")
        elif choice == "5":
            break
        else :
            print("Error!")

if __name__ == "__main__":
    number_operations()