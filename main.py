import json
import psycopg2
from tabulate import tabulate
from contextlib import closing

# import the database configuration from config.json
with open('config.json', 'r') as config_file:
    parameters = json.load(config_file)

def getAllStudents():
    try:
        with closing(psycopg2.connect(**parameters)) as connection:
            with closing(connection.cursor()) as cursor:
                query_string = f'SELECT * FROM students'
                cursor.execute(query_string)
                students = cursor.fetchall()
                return students
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def addStudent(first_name, last_name, email, enrollment_date):
    try:
        with closing(psycopg2.connect(**parameters)) as connection:
            with closing(connection.cursor()) as cursor:
                query_string = """
                INSERT INTO students (first_name, last_name, email, enrollment_date)
                VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query_string, (first_name, last_name, email, enrollment_date))
                connection.commit()

                print("Student added successfully")

    except Exception as e:
        print(f"An error occurred: {e}")

def updateStudentEmail(student_id, new_email):
    try:
        with closing(psycopg2.connect(**parameters)) as connection:
            with closing(connection.cursor()) as cursor:
                query_string = """
                UPDATE students
                SET email = %s
                WHERE student_id = %s
                """
                cursor.execute(query_string, (new_email, student_id))
                connection.commit()

                print("Student email updated successfully")

    except Exception as e:
        print(f"An error occurred: {e}")

def deleteStudent(student_id):
    try:
        with closing(psycopg2.connect(**parameters)) as connection:
            with closing(connection.cursor()) as cursor:
                query_string = """
                DELETE FROM students
                WHERE student_id = %s
                """
                cursor.execute(query_string, (student_id,))
                connection.commit()

                print("Student deleted successfully")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # TESTING: getAllStudents()
    print(f'\nTESTING: getAllStudents():')
    headers = ["ID", "First Name", "Last Name", "Email", "Date"]
    print(tabulate(getAllStudents(), headers=headers, tablefmt="grid"))

    # TESTING: addStudent()
    print(f'\nTESTING: addStudent():')
    addStudent('Muntaha', 'Attef', 'muntahaattef@cmail.carleton.ca', '2023-11-23')
    print(tabulate(getAllStudents(), headers=headers, tablefmt="grid"))

    # TESTING: updateStudent()
    print(f'\nTESTING: updateStudentEmail():')
    updateStudentEmail('4', 'new_email@cmail.carleton.ca')
    print(tabulate(getAllStudents(), headers=headers, tablefmt="grid"))

    # TESTING: deleteStudent()
    print(f'\nTESTING: deleteStudent():')
    deleteStudent('4')
    print(tabulate(getAllStudents(), headers=headers, tablefmt="grid"))

main()