print("=== PERSONAL INFORMATION VALIDATOR ===")
Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
Phone_Number = input("Enter your phone number: ")

name_validator = True
for char in Name:
    print(char, char.isalpha())
    if char.isalpha() == True or char == " ":
        name_validator = True
    else:
        name_validator = False
        break

age_validator = True
if 18 <= Age and Age <= 65:
    age_validator = True
else:
    age_validator = False

phone_validator = True
if len(Phone_Number) != 10:
    phone_validator = False

for char in Phone_Number:
    if char.isdigit() == False:
        phone_validator = False
        break

print("Validation Results:")
if name_validator == True:
    print("Name: Valid (contains only letters and spaces)")
else:
    print("Name: InValid (not contains only letters and spaces)")

if age_validator == True:
    print(f"Valid ({Age} years old)")
else:
    print("InValid")

if phone_validator == True:
    print("Phone: Valid (10-digit number)")
else:
    print("InValid")

print()
print("Formatted Information:")
print(f"Name: {Name.upper()}")
if 18 <= Age and Age <=30:
    print("Young Adult (18-30)")
else:
    print("Adult (30-65)")
print(f"Phone: +66-{Phone_Number}")