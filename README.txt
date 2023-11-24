# 3005-a4

Setup instructions:

How to run the application:
  Before running this program, make sure you have Postgre and Python installed. It is preferred if the Python is updated to version 3.11.
  The required packages to run this program are installed using pip by typing the following lines in the command terminal.
  ````````````````````
  pip install psycopg2
  pip install tabulate
  ````````````````````
  Once all the packages are installed, the program is prepared to be run. To run, first, make sure you are in the correct folder and run the following command.
  ```````````````
  python3 main.py
  ```````````````

Explanation of each function: (mix of assignment specs and my function implementations)
  getAllStudents(): Retrieves and displays all records from the Students table.
  addStudent(first_name, last_name, email, enrollment_date): Inserts a new student record into the Students table.
  updateStudentEmail(student_id, new_email): Updates the email address for a student with the specified student_id.
  deleteStudent(student_id): Deletes the record of the student with the specified student_id.
