#import json
import psycopg2
from tabulate import tabulate
from contextlib import closing
'''
# import the database configuration from config.json
with open('config.json', 'r') as config_file:
    parameters = json.load(config_file)
'''
conn = psycopg2.connect(database = "postgres", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "student",
                        port = 5432)

cur = conn.cursor()
'''
Retrieves and displays all tuples from the students table.
params: none
returns: a tabular display of all the students in the database
'''
def getAllStudents():
    cur = conn.cursor() 
    cur.execute("SELECT * FROM students") #sql way of choosing all data in the students table
    rows = cur.fetchall() #fetch the data to be printed (all data)
    conn.commit() #commit to the changes 
    cur.close() #close teh cursor and shut down the connection
    conn.close()
    for row in rows:    #loop through to print the data
        print(row)
    '''
    try:
        with closing(psycopg2.connect(**parameters)) as connection:
            with closing(connection.cursor()) as cursor:
                query_string = f'SELECT * FROM students'
                cursor.execute(query_string)
                students = cursor.fetchall()
                return students
    #in the case of an error, display the error and return an empty table of no students
    except Exception as e: 
        print(f"An error occurred: {e}")
        return []
        '''

'''
Adds a student into the student table
params: first name, last name, email, enrollment date of the student to populate the tuple
returns: a message to display if it was successfully added or not 
'''
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

'''
Updates an existing students' email
params: the id of th student to update and the new email to update the old email from
returns: a message to display if it was successfully updated or not 
'''
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
    #would be executed if the student does not exist or email to be updated is not unique (email already exists to another student)
    except Exception as e:
        print(f"An error occurred: {e}")

'''
deletes an existing student's data
params: the id of th student to delete
returns: a message to display if it was successfully deleted or not 
'''
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
    #unprompted testing
    # TESTING: getAllStudents()
    print(f'\nTESTING: getAllStudents():')
    headers = ["ID", "First Name", "Last Name", "Email", "Date"] #param to display columns
    print(tabulate(getAllStudents(), headers=headers, tablefmt="grid"))#displays updated table
    '''
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

    #prompted testing
    '''

main()
