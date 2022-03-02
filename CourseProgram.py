"""
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students list using a For loop.
3) Print out the student name, course name, CRN and number of seats left for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
"""

from unicodedata import name
import CourseClass as cc


def main():

    name = "MIS 4322 - Advanced Python"
    crn = "250309"
    seats = 4
    status = "open"
    students = ["John", "James", "Jill", "Jack", "Joanne"]

    n = 0
    for s in students:
        if seats > 0:
            print("Student Name: ", students[n])
            print("CRN: ", crn)
            print("Course name: ", name)
            seats -= 1
            print("Seats left: ", seats)
            n += 1
            print()
            print()
        elif seats == 0 or seats < 0:
            print("Sorry", students[n], ", registration is closed for ", name)
            n += 1


main()
