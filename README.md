# Student-Management-System

This project is a console-based student management system that allows students to check and follow up on their grades. When teachers update scores, students receive notifications via email.

I started this project due to issues with our school’s grade portal, where students did not receive updates for new or corrected grades. This caused numerous inconveniences and the portal was frequently unreliable. This console-based system aims to resolve these issues by notifying students of grade updates and enabling admin functionalities such as registering new students and admins, checking student results, and determining pass/fail status.

## Usage

	1.	Initial Setup:
	•	The default admin ID and password are both 1234. Change these after your first login.
	2.	Email Configuration:
	•	To use the email functionality, you need an app-specific password instead of your actual email password. Follow the steps below to obtain one for Gmail and Outlook.

## Gmail

	1.	Enable Two-Factor Authentication:
	•	Go to your Google Account.
	•	Select “Security” from the menu.
	•	Under “Signing in to Google,” select “2-Step Verification” and follow the prompts to set it up if you haven’t already.
	2.	Generate an App Password:
	•	Go to your App passwords page (you may need to sign in).
	•	Select “Mail” as the app and “Windows Computer” as the device from the dropdown menus.
	•	Click “Generate” to create an app password.
	•	Copy the generated password and use it in the email configuration section of the system.

## Outlook

	1.	Enable Two-Factor Authentication:
	•	Go to your Microsoft Account Security page.
	•	Under “Two-step verification,” select “Set up” and follow the prompts to enable two-step verification if you haven’t already.
	2.	Generate an App Password:
	•	Go to the Microsoft Account App passwords page (you may need to sign in).
	•	Select “Create a new app password.”
	•	Copy the generated password and use it in the email configuration section of the system.
	3.	Configuration:
	•	Update the email and password fields with your app-specific email credentials.

## It Includes

	•	Student JSON database to store student information.
	•	Admin JSON database to store admin information.
	•	JSON library for data handling.
	•	smtplib for sending emails.
	•	random library for generating random numbers.

## Future Enhancements

	•	Transition from a function-based to an object-oriented programming (OOP) approach.
	•	Upgrade from a console-based system to a web-based system using frameworks.




