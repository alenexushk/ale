## Final project
## Student Grading Database

grades = {'Kitty':[90,78],
          'Alex':[79,75],
          'Javi':[98,87],
          'Dani':[95,83]}

def sgdb():
    print ("Welcome to SGDB")
    authentication()
    
def authentication():
    user = input ("Enter your username: ")
    print ("Welcome back,", user)
    pwd = input ("Enter your password: ")
    if pwd ==('loco'):
        print ("You are authorized")
        menu()
    else:
        print ("Wrong password")
        authentication()

def menu():
    print ("")
    print ("Welcome to Grade Central\n")
    print ("[1] - Enter Grades")
    print ("[2] - Remove Student")
    print ("[3] - Student Average Grades")
    print ("[4] - Exit")
    print ("")

    a = input ("Your choice?: ")

    if a == str(1):
        enterGrades()
    elif a == str(2):
        remove()
    elif a == str(3):
        avgGrades()
    elif a == str(4):
        print("Goodbye")
        exit
    else:
        print ("Sorry, incorrect selection. Try again")
        menu()

def enterGrades():
    print (grades)
    b = input("Student Name: ")
    if b not in grades:
        print("Sorry, cannot find that student")
        enterGrades()
    else:   # This 'else: pass' statement is optional
        pass
    c = int(input("Grade: "))
    print ("Adding Grade...")
    grades[b].append(c)
    print("Updated Grades: ", grades)
    menu()

def remove():
    print(grades)
    b = input("Student to remove: ")
    if b not in grades:
        print("Sorry, cannot find that student")
        remove()
    else:   # This 'else: pass' statement is optional
        pass
    print ("Removing Student...")
    del grades[b]
    print("Updated Grades: ", grades)
    menu()
    
def avgGrades():
    import statistics as stats
    print(grades)
    b = input("Average for what student?: ")
    if b not in grades:
        print("Sorry, cannot find that student")
        remove()
    else:   # This 'else: pass' statement is optional
        pass
    x = stats.mean(grades[b])
    print("The average for ", b, "is:", x)
    menu()
    
sgdb()
    


    


    




