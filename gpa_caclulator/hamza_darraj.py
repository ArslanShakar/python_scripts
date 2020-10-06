# Author Hamza Darraj
# GPA calculator made in tool python 3


class HamzaDarraj:
    # function that will get the input of student courses list
    def get_courses_list_input(self):
        no_of_courses = int(input("Enter number of courses: "))
        course_input_count = 1
        courses_list = []

        if no_of_courses < 1:
            print("Number of courses should be greater than 0")
            return

        while course_input_count <= no_of_courses:
            print("for course number {}".format(course_input_count))
            course_credits = input("Enter number of credits: ")

            if course_credits not in ['1', '2', '3']:
                print("Invalid number of credits.\nA course can have between 1 and 3 credits. Try again")
                continue

            course_letter_grade = input("Enter course letter grade: ")

            if course_letter_grade == 'A':
                points = 4
            elif course_letter_grade == 'B':
                points = 3
            elif course_letter_grade == 'C':
                points = 2
            elif course_letter_grade == 'D':
                points = 1
            elif course_letter_grade == 'F':
                points = 0
            else:
                print("Invalid letter grade."
                      "\nPlease make sure letter grade should be one of them 'A', 'B', 'C', 'D', 'F'")
                continue

            course = {
                int(course_credits): points
            }

            courses_list.append(course)
            course_input_count += 1

        return courses_list

    # function calculate the courses gpa
    def calculate_gpa(self, courses_list):
        total_no_of_credits = 0
        gpa_sum = 0

        for course_dict in courses_list:
            course_credits, points = course_dict.popitem()

            total_no_of_credits += course_credits
            gpa_sum += course_credits * points

        gpa = gpa_sum / total_no_of_credits
        return gpa

    # user defined function display calculated gpa
    def show_gpa(self, gpa):
        print("Your GPA is: {}".format(gpa))


if __name__ == "__main__":
    # Make class object
    hamza_obj = HamzaDarraj()

    # call function that get user courses input
    courses_list = hamza_obj.get_courses_list_input()

    # call function that calculate gpa
    gpa = hamza_obj.calculate_gpa(courses_list)

    # call function show_gpa
    hamza_obj.show_gpa(gpa)
