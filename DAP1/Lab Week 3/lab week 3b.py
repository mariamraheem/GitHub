# Names: Mariam Raheem, Xerac Akhtar, Anoosha Imran

#fix the problems with each of these classes (1-3)
#(run them to see the traceback)

#1
class MyClass():
    def __init__(self, a, b):
        self.a = 10
        self.b = 20
        self.x = a + b
my_instance = MyClass(40, 30)
my_instance.x

#2
class MyClass():
    def __init__(self, a, b):
        self.a = 10
        self.b = 20
        self.x = a + b
my_instance = MyClass(50, 20)
my_instance.x

#3
class MyClass():
    def __init__(self, a, b):
        self.x = a + b
my_instance = MyClass(10, 20)
my_instance.x

#4 Create a class to hold all of the courses a student at Harris is enrolled in.
#  - The instance should take two arguments when created; student name, 
#    and student year
#  - At startup, each instance should have an empty list as an attribute 
#    named "enrolled_courses"
#  - Create a method named "enroll" that takes some arguments that describe
#    a course, e.g. name, course number, days, times
#  - When called, make the "enroll" method add a course to the "enrolled_courses"
#    list
#  - Finally, think about what other methods you could add. One to drop a course?
#    One to display the enrolled courses?  Or could you modify "enroll" to make
#    sure times don't overlap, or there aren't too many courses in the list?
#    Work on these if you would like an extra challenge.

class MyCourses:
    def __init__(self, student_name, student_year):
        self.student_name = student_name
        self.student_year = student_year
        self.enrolled_courses = []

    def enroll(self, course_name, course_number, course_days, course_times):
        my_courses = (course_name, 
                      course_number, 
                      course_days, 
                      course_times)
        self.enrolled_courses.append(my_courses)

# NOTE: Used hints from ChatGPT and StackOverflow to arrive at the following
    def drop_course(self, course_name):
        for course in self.enrolled_courses:
            if course[0] == course_name:
                self.enrolled_courses.remove(course)
                print(f"Dropped {course_name}.")
                return
        print(f"Not enrolled in {course_name}.")

    def list_enrollment(self):
        print(f"Enrolled courses for {self.student_name}:")
        for course in self.enrolled_courses:
            print(course)

# Enrollment details for Quarter 2:
quarter_2 = MyCourses("Mariam Raheem", "First Year")

quarter_2.enroll("Analytical Politics", "PPHA 31610", "Tue/Thu", "11:00AM-12:20PM")
quarter_2.enroll("Stats for Data Analysis", "PPHA 31102", "Tue/Thu", "09:30AM-10:50AM")
quarter_2.enroll("Principles of Microeconomics & Public Policy", "PPHA 32400", "Mon/Wed", "03:00PM-04:20PM")

quarter_2.list_enrollment()

quarter_2.drop_course("Analytical Politics")
quarter_2.list_enrollment()
