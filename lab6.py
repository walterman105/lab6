import pickle

class Course_grade():
    def __init__(self):
        self.course_name = ""
        self.student_id = []
        self.student_grades = []
    
    def create(self):
        self.course_name = input("Enter the course name: ")
        students = int(input("Enter the amount of students to add: "))
        
        for x in range(0, students):
            self.student_id.append(int(input("Enter Student ID: ")))
            self.student_grades.append(int(input("Enter Student Grade: ")))
        
def display_courses():
    data_file = open("courses.dat", "rb")
    while 1:
        try:
            data = pickle.load(data_file)
            print(f"\nCourse Name: {data.course_name}")
            print("Student ID   Student Grade")
            print("--------------------------")
            for student_id, student_grade in zip(data.student_id, data.student_grades):
                print(f"{student_id} {student_grade}")
            print()
        except (EOFError):
            break
    data_file.close()
    


while 1:
    print("1. Create Course")
    print("2. Display Courses")
    print("3. Erase All Courses")
    print("0. Exit")
    
    user_input = int(input("Enter option: "))
    
    if user_input == 1:
        c = Course_grade()
        c.create()
        data_file = open("courses.dat", "ab")
        pickle.dump(c, data_file)
        data_file.close()

    elif user_input == 2:
        display_courses()
        
    elif user_input == 3:
        data_file = open("courses.dat", "wb")
        data_file.close()
        
    elif user_input == 0:
        break
    else:
        print("Invalid Option")