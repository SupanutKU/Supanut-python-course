
"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("Nut", 19, "Bangkok", "Thailand")  # name, age, city, country
    hobbies = ["Football"]
    
    # Your code here
    while True :
        print("1 Display into, 2 Add Hobby, 3 Remove Hobby, 4 Edit Age, 5 Exit")
        choice = input("Choose option: ")
        if choice == "1":
            print("Name: ", person[0])
            print("Age: ", person[1])
            print("City: ", person[2])
            print("Country: ", person[3])
            print("Hobbies: ", hobbies)
        if choice == "2":
            add_hobbies = input("Insert new hobbies : ")
            hobbies.append(add_hobbies)
        elif choice == "3":
            del hobbies[0]
        elif choice == "4":
            age = int(input("Insert new age: "))
            person_list = list(person)
            person_list[1] = age
            person = tuple(person_list)
        elif choice == "5":
            break
        else :
            print("Error!")


if __name__ == "__main__":
    personal_info_manager()