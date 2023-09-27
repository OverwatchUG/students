# empty list to be used to store student's data
students = []

# Recording each student's biography from the user
for i in range(10):
    print(f"Enter student {i + 1} details")
    name = str(input("First name: "))
    reg_no = input("Registration number: ")
    age = int(input("Age: "))
    mobile_no = input("Mobile number: ")
    email = input("Email address: ")
    nationality = input("Nationality: ")
    course = input("Course: ")
    program = input("Program: ")
    year_of_study = int(input("Year of study: "))
    graduation_date = input("Expected date of graduation: ")

    # dictionary for storing each student's data
    student = {
        "name": name,
        "reg_no": reg_no,
        "age": age,
        "mobile_no": mobile_no,
        "email": email,
        "nationality": nationality,
        "course": course,
        "program": program,
        "year_of_study": year_of_study,
        "graduation_date": graduation_date
    }

    # adding each student's data to the empty list
    students.append(student)

# printing each student's biography to the console
print(students)

# Printing each student's biography to the console
# for i in range(10):
#     print(f"ENTER STUDENT {i + 1} BIOGRAPH\n")
#     print(f" Name : {student_name}\n Reg-no: {reg_no}\n Age: {student_age}\n Mobile number: {mobile_no}\n "
#           f"Email: {email}\n Nationality: {nationality}\n Course: {course}\n Program: {program}\n "
#           f"Year of study: {year_of_study}\n Graduation date: {graduation_date}")
#     print("--------------------------")
