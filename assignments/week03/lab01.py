# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
if age >= 60:
    print("Senior")
elif age >= 20:
    print("Adult")
elif age >=13:
    print("Teenager")
else:
    print("Child")
