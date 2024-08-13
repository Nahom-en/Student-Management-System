# storing credentials in 'ID' and 'password' form
import json
import random
#Emailing Modules
import smtplib as sl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


my_email = "Email"
password = "App Password:"


# Define email sending function
def send_grade_update_email(to_addrs, student_name, updated_category):
    connection = sl.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=password)

    # Prepare the notification email body with HTML formatting
    email_body = f"""
    <html>
    <body>
        <h2 style="color: #4CAF50;">Grade Update Notification</h2>
        <p>Hello {student_name},</p>
        <p>Your grades for the category "{updated_category}" have been updated. Please log in to check your new grades.</p>
        <p>Best regards,</p>
    </body>
    </html>
    """

    subject = "Your Grade Has Been Updated"
    msg = MIMEMultipart()
    msg['From'] = my_email
    msg['To'] = to_addrs
    msg['Subject'] = subject
    msg.attach(MIMEText(email_body, 'html'))

    # Send the email
    connection.send_message(msg)
    connection.quit()

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



def update_grade(category, max_mark):
    """Prompt user for grade input and validate it."""
    while True:
        try:
            mark = float(input(f"Enter {category} mark (max {max_mark}): "))
            if 0 <= mark <= max_mark:
                return mark
            else:
                print(f"Invalid mark. It should be between 0 and {max_mark}. Try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_totals():
    """Calculate and update total grades and averages."""
    print("Calculating totals...")
    for student_id, data in students.items():
        grades = data['Grades']
        
        # Check if all grades are provided
        all_grades_provided = True
        for category in ['test', 'mid', 'test2', 'Activity', 'Final']:
            for subject in grades[category]:
                if grades[category][subject] is None:
                    all_grades_provided = False
                    break
            if not all_grades_provided:
                break

        if not all_grades_provided:
            print(f"Cannot calculate totals for student {student_id} because not all grades are provided.")
            continue

        # Initialize total grades and grand total
        total_grades = {subject: 0 for subject in grades['test'].keys()}
        grand_total = 0
        
        # Calculate total marks for each subject
        for subject in total_grades.keys():
            total_grades[subject] = (
                grades['Activity'].get(subject, 0) +
                grades['Final'].get(subject, 0) +
                grades['mid'].get(subject, 0) +
                grades['test'].get(subject, 0) +
                grades['test2'].get(subject, 0)
            )
            grand_total += total_grades[subject]

        # Calculate average and round it
        average = round(grand_total / (len(total_grades)), 2)
        
        # Determine pass/fail based on the grand total
        status = "Pass" if average >= 50 else "Fail"

        # Update grades with totals and status
        grades['Total'].update({
            "English": total_grades['English'],
            "Amharic": total_grades['Amharic'],
            "Maths": total_grades['Maths'],
            "Physics": total_grades['Physics'],
            "Chemistry": total_grades['Chemistry'],
            "Geography": total_grades['Geography'],
            "Grand Total": grand_total,
            "Status": status,
            "Average": average
        })


subjects = ["English", "Amharic", "Maths", "Physics", "Chemistry", "Geography"]

def adminlogin(id):
    global subjects
    num = id
    print(f"Admin ID: {num}")  # Debug statement
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
        
        # Collecting student details
        print(f"Registering new student with ID {unique_id}...")
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
            "Total": {"English": None, "Amharic": None, "Maths": None, "Physics": None, "Chemistry": None, "Geography": None, "Grand Total": None, "Status": None, "Average": None}
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
        
        subjects = ["English", "Amharic", "Maths", "Physics", "Chemistry", "Geography"]
        if ask == 1:
            print("Inserting grades for Test 1")
            for subject in subjects:
                students[askid]['Grades']['test'][subject] = update_grade(f"Test 1 mark for {subject}", 10)
            # Calculate totals after inserting grades
            calculate_totals()
            with open('students.json', 'w') as file:
                json.dump(students, file, indent=4)
            # Send an email notification
            student_name = f"{students[askid]['givenname']} {students[askid]['lastname']}"
            send_grade_update_email(students[askid]['student_email'], student_name, "Test 1")
        
        elif ask == 2:
            print("Inserting grades for Mid")
            for subject in subjects:
                students[askid]['Grades']['mid'][subject] = update_grade(f"Mid mark for {subject}", 20)
            # Calculate totals after inserting grades
            calculate_totals()
            with open('students.json', 'w') as file:
                json.dump(students, file, indent=4)
            # Send an email notification
            student_name = f"{students[askid]['givenname']} {students[askid]['lastname']}"
            send_grade_update_email(students[askid]['student_email'], student_name, "Mid")

        elif ask == 3:
            print("Inserting grades for Test 2")
            for subject in subjects:
                students[askid]['Grades']['test2'][subject] = update_grade(f"Test 2 mark for {subject}", 10)
            # Calculate totals after inserting grades
            calculate_totals()
            with open('students.json', 'w') as file:
                json.dump(students, file, indent=4)
            # Send an email notification
            student_name = f"{students[askid]['givenname']} {students[askid]['lastname']}"
            send_grade_update_email(students[askid]['student_email'], student_name, "Test 2")

        elif ask == 4:
            print("Inserting grades for Activity")
            for subject in subjects:
                students[askid]['Grades']['Activity'][subject] = update_grade(f"Activity mark for {subject}", 10)
            # Calculate totals after inserting grades
            calculate_totals()
            with open('students.json', 'w') as file:
                json.dump(students, file, indent=4)
            # Send an email notification
            student_name = f"{students[askid]['givenname']} {students[askid]['lastname']}"
            send_grade_update_email(students[askid]['student_email'], student_name, "Activity")

        elif ask == 5:
            print("Inserting grades for Final Exam")
            for subject in subjects:
                students[askid]['Grades']['Final'][subject] = update_grade(f"Final Exam mark for {subject}", 40)
            # Calculate totals after inserting grades
            calculate_totals()
            with open('students.json', 'w') as file:
                json.dump(students, file, indent=4)
            # Send an email notification
            student_name = f"{students[askid]['givenname']} {students[askid]['lastname']}"
            send_grade_update_email(students[askid]['student_email'], student_name, "Final Exam")

        print("Grades inserted successfully!")

    elif choice == 5:
        askid = input("Enter Student Id: ")
        while askid not in students:
            askid = input("You Have entered invalid Student id.\nEnter Valid Student Id: ")

        print("\nWhich category of scores would you like to edit?")
        print("1) Test 1")
        print("2) Mid")
        print("3) Test 2")
        print("4) Activity")
        print("5) Final Exam")
        edit_choice = int(input("Please enter the number of your choice: "))

        if edit_choice not in [1, 2, 3, 4, 5]:
            print("Invalid choice. Please restart the editing process.")
            return

        categories = {1: 'test', 2: 'mid', 3: 'test2', 4: 'Activity', 5: 'Final'}
        category = categories[edit_choice]

        print(f"Editing grades for {category.capitalize()}")
        for subject in subjects:
            current_grade = students[askid]['Grades'][category].get(subject)
            new_grade = update_grade(f"{category.capitalize()} mark for {subject}", {"test": 10, "mid": 20, "test2": 10, "Activity": 10, "Final": 40}[category])
            if new_grade is not None:
                students[askid]['Grades'][category][subject] = new_grade
            else:
                print(f"No changes made for {subject}.")
        
        # Update Total and Average
        calculate_totals()

        with open('students.json', 'w') as file:
            json.dump(students, file, indent=4)
        print("Grades updated and total calculations are complete.")



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
        connection = sl.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=password)

    # Prepare the report body with HTML formatting
    report_body = """
    <html>
    <body>
        <h2 style="color: #4CAF50;">Results Status for Student ID: {id}</h2>
        <table border="1" style="border-collapse: collapse; width: 100%; max-width: 600px;">
            <thead>
                <tr style="background-color: #f2f2f2;">
                    <th style="padding: 8px; text-align: left;">Category</th>
                    <th style="padding: 8px; text-align: left;">Subject</th>
                    <th style="padding: 8px; text-align: left;">Grade</th>
                </tr>
            </thead>
            <tbody>
    """.format(id=id)

    for key, value in students[id]['Grades'].items():
        report_body += f"""
        <tr>
            <td colspan="3" style="background-color: #f9f9f9; font-weight: bold;">{key.upper()}</td>
        </tr>
        """
        for subject, grade in value.items():
            report_body += f"""
            <tr>
                <td></td>
                <td>{subject}</td>
                <td>{grade if grade is not None else 'No data'}</td>
            </tr>
            """
    
    report_body += """
            </tbody>
        </table>
        <p style="color: #555;">Please review your grades and contact us if you have any questions.</p>
    </body>
    </html>
    """

    # Email detailsstudents[id]['student_email']
    to_addrs = students[id]['student_email']
    subject = "Your Grade Report"
    msg = MIMEMultipart()
    msg['From'] = my_email
    msg['To'] = to_addrs
    msg['Subject'] = subject
    msg.attach(MIMEText(report_body, 'html'))

    # Send the email
    connection.send_message(msg)
    connection.quit()

    # Print the report to the console
    print(f"\nE*********RESULTS STATUS FOR STUDENT ID: {id}*********\n")
    for key, value in students[id]['Grades'].items():
        print(f"{key.upper()}:\n" + "\n".join([f"{subject}: {grade if grade is not None else 'No data'}" for subject, grade in value.items()]) + "\n")
    print("*********")

studentlogin()
