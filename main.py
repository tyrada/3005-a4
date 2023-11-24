import psycopg2
from tabulate import tabulate

'''
establish a connection between database and the program
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
    try:
        toExecute = "SELECT * FROM students" #sql way of choosing all data in the students table
        cur.execute(toExecute) #execute command
        rows = cur.fetchall() #fetch the all the data to be printed
        conn.commit() #commit to the changes 
        return rows    #return all the data to be formatted by tabulate
    except Exception as e:
        print(f"An error occurred: {e}")


    
'''
Adds a student into the student table
params: first name, last name, email, enrollment date of the student to populate the tuple
returns: a message to display if it was successfully added or not 
'''
def addStudent(first_name, last_name, email, enrollment_date):
    try:
        toExecute = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)" #sql way of adding data to the students table
        cur.execute(toExecute, (first_name, last_name,email, enrollment_date)) #execute command with the given parameters
        conn.commit() #commit to the changes 
        print("Student added successfully")#display message to user
        
    except Exception as e:
        print(f"An error occurred: {e}")

   
'''
Updates an existing students' email
params: the id of th student to update and the new email to update the old email from
returns: a message to display if it was successfully updated or not 
'''
def updateStudentEmail(student_id, new_email):
    try:
        toExecute = "UPDATE students SET email = %s WHERE student_id = %s" #sql way of updating an existing student in the students table
        cur.execute(toExecute, (new_email, student_id)) #execute command with the given parameters
        conn.commit() #commit to the changes 
        print("Student email updated successfully")#display message to user

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
        toExecute = """DELETE FROM students WHERE student_id = %s """ #sql way of deleting a specified student in the students table
        cur.execute(toExecute, student_id) #execute command with the given param
        conn.commit() #commit to the changes 
        print("Student deleted successfully")#display message to user

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    
    print("BEGINNING WITH UNPROMPTED TESTING")   
    #unprompted testing
    # TESTING: getAllStudents()
    print("TESTING: getAllStudents():")
    headers = ["ID", "First Name", "Last Name", "Email", "Date"] #param to display columns
    print(tabulate(getAllStudents(), headers=headers, tablefmt="grid"))#displays updated table
    
    # TESTING: addStudent()
    print("TESTING: addStudent():")
    addStudent('Muntaha', 'Attef', 'muntahaattef@cmail.carleton.ca', '2023-11-23')
    print(tabulate(getAllStudents(), headers=headers, tablefmt="grid"))
    
    # TESTING: updateStudent()
    print("TESTING: updateStudentEmail():")
    updateStudentEmail('4', 'new_email@cmail.carleton.ca')
    print(tabulate(getAllStudents(), headers=headers, tablefmt="grid"))

    # TESTING: deleteStudent()
    print("TESTING: deleteStudent():")
    deleteStudent('4')
    print(tabulate(getAllStudents(), headers=headers, tablefmt="grid")) 

    #prompted testing
    print("CONTINUING WITH PROMPTED TESTING")   

    while(1): #infinite loop to keep asking for user input
        #prompt and prompt formatting
        prompt = input("What command would you like to run? (please type update, delete, add, display, or quit to exit the program): ")
        userInput = prompt.upper() #make user input into uppercase for consistency
        headers = ["ID", "First Name", "Last Name", "Email", "Date"] #param to display columns

        # EXECUTING: updateStudent()
        if userInput == "UPDATE":
            print("EXECUTING: updateStudent()")
            id = input("enter the student ID of the student you wish to update the email of: ")
            nEmail = input("enter the updated email address: ")
            updateStudentEmail(id, nEmail) 
            continue
        
        # EXECUTING: deleteStudent()
        if userInput == "DELETE":
            print("EXECUTING: deleteStudent()")
            id = input("enter the student ID of the student you would like to delete: ")
            deleteStudent(id)
            continue
        
        # EXECUTING: addStudent()
        if userInput == "ADD":
            print("EXECUTING: addStudent()")
            f = input("enter the first name of the new student: ")
            l = input("enter the last name of the new student: ")
            e = input("enter the email of the new student: ")
            en = input("enter the enrollment date of the new student: ")
            addStudent(first_name=f, last_name=l, email=e, enrollment_date=en)
            continue
        
        # EXECUTING: getAllStudents()
        if userInput == "DISPLAY":
            print("EXECUTING: getAllStudents()")
            print(tabulate(getAllStudents(), headers=headers, tablefmt="grid"))#displays table in formatted from using tabulate
            continue
        
        #quit the program
        if userInput == "QUIT": 
            print("goodbye. ")
            quit()
        
        #ERROR HANDLING for invalid entry
        else:
            print("I did not understand your input, please try again")
            continue   
    

main()
