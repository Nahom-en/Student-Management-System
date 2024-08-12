# storing credientials in 'ID' and 'password' form
import json
import random


#RANDOM NUMBER GENERATOR FOR STUDENTS WHEN ADMIN ADD NEW STUDENT TO REGISTER
def generate_unique_id():
    return random.randint(1000, 9999)

# Example usage
unique_id = generate_unique_id()
print(unique_id)

admin = {
    "1234": {
        "lastname": "Doe",
        "givenname": "John",
        "password": "1234",
    },
    "5678": {
        "lastname": "Smith",
        "givenname": "Jane",
        "password": "5678"
    }
}

student = {}
"""student = {
    "id": {
        "givenname": "s",
        "password": "s",
        "lastname": "s",
        "student_tel": "09",
        "student_email": "na@example.com",
        "parent_givenname": "S",
        "parent_lastname": "s",
        "parent_email": "s@example.com",
        "parent_tel": "0911",
        "Grades": {
            "test": {
                "English": 85,
                "Amharic": 90,
                "Maths": 88,
                "Physics": 92,
                "Chemistry": 87,
                "Geography": 80
            },
            "mid": {
                "English": 85,
                "Amharic": 90,
                "Maths": 88,
                "Physics": 92,
                "Chemistry": 87,
                "Geography": 80
            },
            "test2": {
                "English": 85,
                "Amharic": 90,
                "Maths": 88,
                "Physics": 92,
                "Chemistry": 87,
                "Geography": 80
            },
            "Activity": {
                "English": 85,
                "Amharic": 90,
                "Maths": 88,
                "Physics": 92,
                "Chemistry": 87,
                "Geography": 80
            },
            "Final": {
                "English": 85,
                "Amharic": 90,
                "Maths": 88,
                "Physics": 92,
                "Chemistry": 87,
                "Geography": 80
            },
            "Total": {
                "English": 85,
                "Amharic": 90,
                "Maths": 88,
                "Physics": 92,
                "Chemistry": 87,
                "Geography": 80
            }
        }
    }
}

"""


def regadmin():
    unique_id = generate_unique_id()
        #auto generate again if unique id is given for admin 
    while unique_id in admin:
        unique_id = generate_unique_id()
        
    ask1 = input(f"{unique_id} assigned for Admin.\nEnter Admin's Given name: ").title()
    while ask1 not str:
        ask1 = input("Invalid Characts hasbeen used\nPlease enter Admin's given name: ").title()
    admin[unique_id]['givenname'] = ask1
    
    ask2 = input("Enter Admin's Last name: ").title()
    while ask2 not str:
        ask2 = input("Invalid Characts hasbeen used\nPlease enter Admin's Last name: ").title()
    admin[unique_id]['lastname'] = ask2 
    
    ask3 = input("Enter Admin's position: ").title()
    while ask3 != str:
        ask3 = input("Invalid Characts hasbeen used\nPlease enter Admin's position: ").title()
    admin[unique_id]['position'] = ask3
    return "New Admin has been Registered Sucessfully!"
    
    


def adminlogin(id):
    choice = int(input(
        f"Welcome{student[id]['givenname']}\n1) Register new student.\n"
        "2) Register new admin.\n"
        "3) Check students result.\n"
        "4) Insert student grade.\n"
        "5) Edit Student grade.\n"
        "Please enter your choice: "
    ))
    while choice not in [1, 2, 3, 4, 5]:
        choice = int(input(
        f"Please Enter Correct choice\n1) Register new student.\n"
        "2) Register new admin.\n"
        "3) Check students result.\n"
        "4) Insert student grade.\n"
        "5) Edit Student grade.\n"
        "Please enter your choice: "
    ))
    if choice ==1:
        #Generate Random ID number
        unique_id = generate_unique_id()
        #auto generate again if unique id is given for student 
        while unique_id in student:
            unique_id = generate_unique_id()
        ask1 = input(f"{unique_id} assigned for student.\nEnter student Given name: ").title()
        while ask1 not str:
            ask1 = input("Invalid Characts has been used\nPlease enter student given name: ").title()
        student[unique_id]['givenname'] = ask1
        
        
        ask2 = input("Enter student last name: ").title()
        while ask2 not str:
            ask2 = input("Invalid Characts has been used\nPlease enter student last name: ").title()
        student[unique_id]['lastname'] = ask2
        
        ask3 = input("Enter student email(Enter to skip): ").title()
        student[unique_id]['student_email']=ask3
        
        ask4 = input("Enter student Phone number: ").title()
        while ask4 != int:
            ask4 = input("Invalid Characts has been used\nPlease enter student Phone number: ").title()
        student[unique_id]['student_tel']= ask4
        
        
        
        ask5 = input("Enter parent Given name: ").title()
        while ask5 != str:
            ask5 = input("Invalid Characts has been used\nPlease enter parent given name: ").title()
        student[unique_id]['parent_givenname'] = ask5
        
        
        ask6 = input("Enter parent last name: ").title()
        while ask6 != str:
            ask6 = input("Invalid Characts has been used\nPlease enter parent last name: ").title()
        student[unique_id]['parent_lastname'] = ask6
        
        ask7 = input("Enter parent email(Enter to skip): ").title()
        student[unique_id]['parent_email'] = ask7
        
        ask8 = input("Enter parent Phone number: ").title()
        while ask8 != int:
            ask8 = input("Invalid Characts has been used\nPlease enter parent Phone number: ").title()
        student[unique_id]['parent_tel'] = ask8
        return "Sucessfully Registered!"
        
        
        
        
        
    elif choice ==2:
        print(regadmin())
    elif choice ==3:
        pass
    elif choice ==4:
        pass
    elif choice ==5:
        pass
    
    
    
    
    choice = int(input(
        f"Welcome{student[id]['givenname']}\n1) Check Test 1 results (10%).\n"
        "2) Check Mid results (20%).\n"
        "3) Check Test 2 results (10%).\n"
        "4) Check Activities results (15%).\n"
        "5) Check Final results (50%).\n"
        "6) Check Total results (100%).\n"
        "Please enter your choice: "
    ))
    
    # Loop until a valid choice is entered
    while choice not in [1, 2, 3, 4, 5, 6]:
        choice = int(input(
            "Invalid selection. Please select correctly\n"
            "1) Check Test 1 results (10%).\n"
            "2) Check Mid results (20%).\n"
            "3) Check Test 2 results (10%).\n"
            "4) Check Activities results (15%).\n"
            "5) Check Final results (50%).\n"
            "6) Check Total results (100%).\n"
            "Please enter your choice: "
        ))





def studentlogin():
    askid = input("Enter your Id: ")
    if askid in admin:
        askpass = input("Enter Your Password: ")
        if askpass == admin['password']:
             adminlogin(askid)
        else:
            print("Incorrect Credentials.Pleas try again.\n")
            studentlogin()
    while askid not in students:
        askid = input("You Have entered invalid Student id.\nEnter Valid Student Id: ")
    askpass = input("Enter Your Password: ")
    while askpass != students[askid]['password']:
        askpass = input("Incorrect Password.\nEnter Your Password: ")
    studentdashboard(askid)
    
    
def studentdashboard(id):
    # Prompt user for input and validate it
    choice = int(input(
        f"Welcome{student[id]['givenname']}\n1) Check Test 1 results (10%).\n"
        "2) Check Mid results (20%).\n"
        "3) Check Test 2 results (10%).\n"
        "4) Check Activities results (15%).\n"
        "5) Check Final results (50%).\n"
        "6) Check Total results (100%).\n"
        "Please enter your choice: "
    ))
    
    # Loop until a valid choice is entered
    while choice not in [1, 2, 3, 4, 5, 6]:
        choice = int(input(
            "Invalid selection. Please select correctly\n"
            "1) Check Test 1 results (10%).\n"
            "2) Check Mid results (20%).\n"
            "3) Check Test 2 results (10%).\n"
            "4) Check Activities results (15%).\n"
            "5) Check Final results (50%).\n"
            "6) Check Total results (100%).\n"
            "Please enter your choice: "
        ))
    
            
            
studentlogin()
    