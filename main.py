# storing credentials in 'ID' and 'password' form
import json
import random

# RANDOM NUMBER GENERATOR FOR STUDENTS WHEN ADMIN ADD NEW STUDENT TO REGISTER
def generate_unique_id():
    return random.randint(1000, 9999)

#CREATION OF ADMIN AND STUDENT JSON BASED DATABASE
with open('admin.json', 'r') as file:
    admin = json.load(file)

with open('students.json', 'r') as file:
    students = json.load(file)

def regadmin():
    unique_id = generate_unique_id()
    # auto-generate again if unique id is given for admin 
    while str(unique_id) in admin:
        unique_id = generate_unique_id()
        
    ask1 = input(f"{unique_id} assigned for Admin.\nEnter Admin's Given name: ").title()
    while not ask1.isalpha():
        ask1 = input("Invalid Characters used. Please enter Admin's given name: ").title()
    admin[str(unique_id)] = {'givenname': ask1}

    ask2 = input("Enter Admin's Last name: ").title()
    while not ask2.isalpha():
        ask2 = input("Invalid Characters used. Please enter Admin's Last name: ").title()
    admin[str(unique_id)]['lastname'] = ask2
    
    ask3 = input("Enter Admin's position: ").title()
    while not ask3.isalpha():
        ask3 = input("Invalid Characters used. Please enter Admin's position: ").title()
    admin[str(unique_id)]['position'] = ask3
    admin[str(unique_id)]['password'] = input("Enter Admin's Password: ")
    with open('admin.json', 'w') as file:
        json.dump(admin, file, indent=4)
    print( "New Admin has been Registered Successfully!")

def adminlogin(id):
    num = id
    choice = int(input(f"\n****Welcome {admin[num]['givenname']}****\n1) Register new student.\n2) Register new admin.\n3) Check students result.\n4) Insert student grade.\n5) Edit Student grade.\nPlease enter your choice: "))
    while choice not in [1, 2, 3, 4, 5]:
        choice = int(input(
        "Please Enter Correct choice\n1) Register new student.\n"
        "2) Register new admin.\n"
        "3) Check students result.\n"
        "4) Insert student grade.\n"
        "5) Edit Student grade.\n"
        "Please enter your choice: "
    ))
    if choice == 1:
        unique_id = generate_unique_id()
        while str(unique_id) in students:
            unique_id = generate_unique_id()
        students[str(unique_id)] = {}

        ask1 = input(f"{unique_id} assigned for student.\nEnter student Given name: ").title()
        while not ask1.isalpha():
            ask1 = input("Invalid Characters used. Please enter student given name: ").title()
        students[str(unique_id)]['givenname'] = ask1

        ask2 = input("Enter student last name: ").title()
        while not ask2.isalpha():
            ask2 = input("Invalid Characters used. Please enter student last name: ").title()
        students[str(unique_id)]['lastname'] = ask2

        ask3 = input("Enter student email (Enter to skip): ").title()
        students[str(unique_id)]['student_email'] = ask3

        ask4 = input("Enter student Phone number: ")
        while not ask4.isdigit():
            ask4 = input("Invalid Characters used. Please enter student Phone number: ")
        students[str(unique_id)]['student_tel'] = ask4

        ask5 = input("Enter parent Given name: ").title()
        while not ask5.isalpha():
            ask5 = input("Invalid Characters used. Please enter parent given name: ").title()
        students[str(unique_id)]['parent_givenname'] = ask5

        ask6 = input("Enter parent last name: ").title()
        while not ask6.isalpha():
            ask6 = input("Invalid Characters used. Please enter parent last name: ").title()
        students[str(unique_id)]['parent_lastname'] = ask6

        ask7 = input("Enter parent email (Enter to skip): ").title()
        students[str(unique_id)]['parent_email'] = ask7

        ask8 = input("Enter parent Phone number: ")
        while not ask8.isdigit():
            ask8 = input("Invalid Characters used. Please enter parent Phone number: ")
        students[str(unique_id)]['parent_tel'] = ask8

        # Initialize grades dictionary for the student
        students[str(unique_id)]['Grades'] = {
            "test": {"English": None, "Amharic": None, "Maths": None, "Physics": None, "Chemistry": None, "Geography": None},
            "mid": {"English": None, "Amharic": None, "Maths": None, "Physics": None, "Chemistry": None, "Geography": None},
            "test2": {"English": None, "Amharic": None, "Maths": None, "Physics": None, "Chemistry": None, "Geography": None},
            "Activity": {"English": None, "Amharic": None, "Maths": None, "Physics": None, "Chemistry": None, "Geography": None},
            "Final": {"English": None, "Amharic": None, "Maths": None, "Physics": None, "Chemistry": None, "Geography": None},
            "Total": {"English": None, "Amharic": None, "Maths": None, "Physics": None, "Chemistry": None, "Geography": None}
        }

        # Add password for student
        students[str(unique_id)]['password'] = input("Enter Student's Password: ")

        with open('students.json', 'w') as file:
            json.dump(students, file, indent=4)
        print("Student Successfully Registered!")
        
    elif choice == 2:
        regadmin()
    elif choice == 3:
        askid = input("Enter Student Id: ")
        while askid not in students:
            askid = input("You Have entered invalid Student id.\nEnter Valid Student Id: ")
        print(f"\n*********RESULTS STATUS FOR STUDENT ID: {askid}*********\n")
        for key, value in students[askid]['Grades'].items():
            print(f"{key.upper()}:\n" + "\n".join([f"{subject}: {grade if grade is not None else 'No data'}" for subject, grade in value.items()]) + "\n")
        print("*********")

    elif choice == 4:
        askid = input("Enter Student Id: ")
        while askid not in students:
            askid = input("You Have entered invalid Student id.\nEnter Valid Student Id: ")

        ask = int(input(f"\nStudent Id:{askid}\nStudent Full Name: {students[askid]['givenname']} {students[askid]['lastname']}\n1)To insert test 1\n2)To insert mid\n3)To insert test 2\n4)To insert Activity\n5)To insert Final.\n"))
        con = True
        if ask == 1:
            while con:
                ask = float(input("Test 10% Mark\n\nEnter English mark:"))
                students[askid]['Grades']['test']['English'] = ask
                if ask <= 10:
                    con = False
            con = True

            while con:    
                ask = float(input("Enter Amharic mark:"))
                students[askid]['Grades']['test']['Amharic'] = ask
                if ask <= 10:
                    con = False
            con = True

            while con:
                ask = float(input("Enter Maths mark:"))
                students[askid]['Grades']['test']['Maths'] = ask
                if ask <= 10:
                    con = False
            con = True

            while con:
                ask = float(input("Enter Physics mark:"))
                students[askid]['Grades']['test']['Physics'] = ask
                if ask <= 10:
                    con = False
            con = True

            while con:
                ask = float(input("Enter Chemistry mark:"))
                students[askid]['Grades']['test']['Chemistry'] = ask
                if ask <= 10:
                    con = False
            con = True

            while con:
                ask = float(input("Enter Geography mark:"))
                students[askid]['Grades']['test']['Geography'] = ask
                if ask <= 10:
                    con = False
            with open('students.json', 'w') as file:
                json.dump(students, file, indent=4)
        elif ask == 2:
            while con:
                ask = float(input("Mid 20% Mark\n\nEnter English mark:"))
                students[askid]['Grades']['mid']['English'] = ask
                if ask <= 20:
                    con = False
            con = True

            while con:    
                ask = float(input("Enter Amharic mark:"))
                students[askid]['Grades']['mid']['Amharic'] = ask
                if ask <= 20:
                    con = False
            con = True

            while con:
                ask = float(input("Enter Maths mark:"))
                students[askid]['Grades']['mid']['Maths'] = ask
                if ask <= 20:
                    con = False
            con = True

            while con:
                ask = float(input("Enter Physics mark:"))
                students[askid]['Grades']['mid']['Physics'] = ask
                if ask <= 20:
                    con = False
            con = True

            while con:
                ask = float(input("Enter Chemistry mark:"))
                students[askid]['Grades']['mid']['Chemistry'] = ask
                if ask <= 20:
                    con = False
            con = True

            while con:
                ask = float(input("Enter Geography mark:"))
                students[askid]['Grades']['mid']['Geography'] = ask
                if ask <= 20:
                    con = False
            with open('students.json', 'w') as file:
                json.dump(students, file, indent=4)
        elif ask == 3:
            while con:
                ask = float(input("Test 2 10% Mark\n\nEnter English mark:"))
                students[askid]['Grades']['test2']['English'] = ask
                if ask <= 10:
                    con = False
            con = True

            while con:    
                ask = float(input("Enter Amharic mark:"))
                students[askid]['Grades']['test2']['Amharic'] = ask
                if ask <= 10:
                    con = False
            con = True

            while con:
                ask = float(input("Enter Maths mark:"))
                students[askid]['Grades']['test2']['Maths'] = ask
                if ask <= 10:
                    con = False
            con = True

            while con:
                ask = float(input("Enter Physics mark:"))
                students[askid]['Grades']['test2']['Physics'] = ask
                if ask <= 10:
                    con = False
            con = True

            while con:
                ask = float(input("Enter Chemistry mark:"))
                students[askid]['Grades']['test2']['Chemistry'] = ask
                if ask <= 10:
                    con = False
            con = True

            while con:
                ask = float(input("Enter Geography mark:"))
                students[askid]['Grades']['test2']['Geography'] = ask
                if ask <= 10:
                    con = False
            with open('students.json', 'w') as file:
                json.dump(students, file, indent=4)
        elif ask == 4:
            while con:
                ask = float(input("Activity 10% Mark\n\nEnter English mark:"))
                students[askid]['Grades']['Activity']['English'] = ask
                if ask <= 10:
                    con = False
            con = True

            while con:    
                ask = float(input("Enter Amharic mark:"))
                students[askid]['Grades']['Activity']['Amharic'] = ask
                if ask <= 10:
                    con = False
            con = True

            while con:
                ask = float(input("Enter Maths mark:"))
                students[askid]['Grades']['Activity']['Maths'] = ask
                if ask <= 10:
                    con = False
            con = True

            while con:
                ask = float(input("Enter Physics mark:"))
                students[askid]['Grades']['Activity']['Physics'] = ask
                if ask <= 10:
                    con = False
            con = True

            while con:
                ask = float(input("Enter Chemistry mark:"))
                students[askid]['Grades']['Activity']['Chemistry'] = ask
                if ask <= 10:
                    con = False
            con = True

            while con:
                ask = float(input("Enter Geography mark:"))
                students[askid]['Grades']['Activity']['Geography'] = ask
                if ask <= 10:
                    con = False
            with open('students.json', 'w') as file:
                json.dump(students, file, indent=4)
        elif ask == 5:
            while con:
                ask = float(input("Final Exam 40% Mark\n\nEnter English mark:"))
                students[askid]['Grades']['Final']['English'] = ask
                if ask <= 40:
                    con = False
            con = True

            while con:    
                ask = float(input("Enter Amharic mark:"))
                students[askid]['Grades']['Final']['Amharic'] = ask
                if ask <= 40:
                    con = False
            con = True

            while con:
                ask = float(input("Enter Maths mark:"))
                students[askid]['Grades']['Final']['Maths'] = ask
                if ask <= 40:
                    con = False
            con = True

            while con:
                ask = float(input("Enter Physics mark:"))
                students[askid]['Grades']['Final']['Physics'] = ask
                if ask <= 40:
                    con = False
            con = True

            while con:
                ask = float(input("Enter Chemistry mark:"))
                students[askid]['Grades']['Final']['Chemistry'] = ask
                if ask <= 40:
                    con = False
            con = True

            while con:
                ask = float(input("Enter Geography mark:"))
                students[askid]['Grades']['Final']['Geography'] = ask
                if ask <= 40:
                    con = False
            with open('students.json', 'w') as file:
                json.dump(students, file, indent=4)

    elif choice == 5:
        askid = input("Enter Student Id: ")
        while askid not in students:
            askid = input("You Have entered invalid Student id.\nEnter Valid Student Id: ")

        ask = int(input(f"\nStudent Id:{askid}\nStudent Full Name: {students[askid]['givenname']} {students[askid]['lastname']}\n1)To Edit Test 1 Marks\n2)To Edit Mid Marks\n3)To Edit Test 2 Marks\n4)To Edit Activity Marks\n5)To Edit Final Marks\n\nPlease Choose: "))
        if ask == 1:
            edit_subject = input("Enter Subject Name (English, Amharic, Maths, Physics, Chemistry, Geography): ").capitalize()
            if edit_subject in students[askid]['Grades']['test']:
                new_grade = float(input(f"Enter new mark for {edit_subject}: "))
                students[askid]['Grades']['test'][edit_subject] = new_grade
                with open('students.json', 'w') as file:
                    json.dump(students, file, indent=4)
                print("Test 1 marks updated successfully!")
            else:
                print("Invalid Subject Name")

        elif ask == 2:
            edit_subject = input("Enter Subject Name (English, Amharic, Maths, Physics, Chemistry, Geography): ").capitalize()
            if edit_subject in students[askid]['Grades']['mid']:
                new_grade = float(input(f"Enter new mark for {edit_subject}: "))
                students[askid]['Grades']['mid'][edit_subject] = new_grade
                with open('students.json', 'w') as file:
                    json.dump(students, file, indent=4)
                print("Mid marks updated successfully!")
            else:
                print("Invalid Subject Name")

        elif ask == 3:
            edit_subject = input("Enter Subject Name (English, Amharic, Maths, Physics, Chemistry, Geography): ").capitalize()
            if edit_subject in students[askid]['Grades']['test2']:
                new_grade = float(input(f"Enter new mark for {edit_subject}: "))
                students[askid]['Grades']['test2'][edit_subject] = new_grade
                with open('students.json', 'w') as file:
                    json.dump(students, file, indent=4)
                print("Test 2 marks updated successfully!")
            else:
                print("Invalid Subject Name")

        elif ask == 4:
            edit_subject = input("Enter Subject Name (English, Amharic, Maths, Physics, Chemistry, Geography): ").capitalize()
            if edit_subject in students[askid]['Grades']['Activity']:
                new_grade = float(input(f"Enter new mark for {edit_subject}: "))
                students[askid]['Grades']['Activity'][edit_subject] = new_grade
                with open('students.json', 'w') as file:
                    json.dump(students, file, indent=4)
                print("Activity marks updated successfully!")
            else:
                print("Invalid Subject Name")

        elif ask == 5:
            edit_subject = input("Enter Subject Name (English, Amharic, Maths, Physics, Chemistry, Geography): ").capitalize()
            if edit_subject in students[askid]['Grades']['Final']:
                new_grade = float(input(f"Enter new mark for {edit_subject}: "))
                students[askid]['Grades']['Final'][edit_subject] = new_grade
                with open('students.json', 'w') as file:
                    json.dump(students, file, indent=4)
                print("Final marks updated successfully!")
            else:
                print("Invalid Subject Name")
        adminlogin(num)
    

def studentlogin():
    askid = input("Enter your Id: ")
    if askid in admin:
        askpass = input("Enter Your Password: ")
        if askpass == admin[askid]['password']:
            adminlogin(id=askid)
        else:
            print("Incorrect Credentials. Please try again.\n")
            studentlogin()
    elif askid in students:
        askpass = input("Enter Your Password: ")
        while askpass != students[askid].get('password', ''):
            askpass = input("Incorrect Password.\nEnter Your Password: ")
        studentdashboard(askid)
    else:
        print("Invalid ID.")
        studentlogin()
    
def studentdashboard(id):
    # Prompt user for input and validate it
    choice = int(input(
        f"Welcome {students[id]['givenname']}\n"
        "1) Check Your Results.\n"
            "Please enter your choice: "
    ))
    
    # Loop until a valid choice is entered
    while choice not in [1, 2, 3, 4, 5, 6]:
        choice = int(input(
            "Invalid selection. Please select correctly\n"
            "1) Check Your Results.\n"
            "Please enter your choice: "
        ))

    # Display the results 
    if choice == 1:
        print(f"\n*********RESULTS STATUS FOR STUDENT ID: {id}*********\n")
        for key, value in students[id]['Grades'].items():
            print(f"{key.upper()}:\n" + "\n".join([f"{subject}: {grade if grade is not None else 'No data'}" for subject, grade in value.items()]) + "\n")
        print("*********")

studentlogin()
