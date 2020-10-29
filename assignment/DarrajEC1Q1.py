from fractions import Fraction


class DarrajEC1Q1:
    # function that will input sequence of grades
    def get_grades_seq(self):
        grades = input("Enter grades comma separated integer values: ")
        grades_seq = [int(e.strip()) for e in grades.split(",") if e and e.strip()]

        if not grades_seq:
            print("Grades sequence should not empty!")
            return

        return grades_seq

    def computes_information(self, grades_sequence):
        grade_letters = {
            'A': [], 'B': [], 'C': [], 'D': [], 'F': [],
        }

        for grade in grades_sequence:
            if 90 < grade < 101:
                grade_letters['A'].append(grade)
            elif 80 < grade < 91:
                grade_letters['B'].append(grade)
            elif 70 < grade < 81:
                grade_letters['C'].append(grade)
            elif 60 <= grade < 71:
                grade_letters['D'].append(grade)
            elif grade < 60:
                grade_letters['F'].append(grade)

        # computes and displays the number of passing and failing grades (passing grade >=60)
        passing_grades = grade_letters['A'] + grade_letters['B'] + grade_letters['C'] + grade_letters['D']
        passing_failing_grades = "Number of passing grades = {} and Number of failing grades = {}"
        print(passing_failing_grades.format(len(passing_grades), len(grade_letters['F'])))

        # computes and displays the average grade and finds the highest and lowest grade.
        all_grades = passing_grades + grade_letters['F']
        average = sum(all_grades) // len(all_grades)
        highest = max(all_grades)
        lowest = min(all_grades)
        print("Average grade = {}, Highest grade = {}, Lowest grade = {}".format(average, highest, lowest))

        # computes and displays the range of grades (range = highest grade – lowest grade).
        print("Range of grades (range = {} – {})".format(highest, lowest))

        # computes and displays the number and ratio of As, Bs, Cs, Ds, and Fs.
        print("Number of A Grades = {}".format(len(grade_letters['A'])))
        print("Number of B Grades = {}".format(len(grade_letters['B'])))
        print("Number of C Grades = {}".format(len(grade_letters['C'])))
        print("Number of D Grades = {}".format(len(grade_letters['D'])))
        print("Number of F Grades = {}".format(len(grade_letters['F'])))

        a_ratio = self.get_ratio(len(grade_letters['A']), len(all_grades))
        b_ratio = self.get_ratio(len(grade_letters['B']), len(all_grades))
        c_ratio = self.get_ratio(len(grade_letters['C']), len(all_grades))
        d_ratio = self.get_ratio(len(grade_letters['D']), len(all_grades))
        f_ratio = self.get_ratio(len(grade_letters['F']), len(all_grades))

        print("Ratio of A Grades = {}".format(a_ratio))
        print("Ratio of B Grades = {}".format(b_ratio))
        print("Ratio of C Grades = {}".format(c_ratio))
        print("Ratio of D Grades = {}".format(d_ratio))
        print("Ratio of F Grades = {}".format(f_ratio))

        # computes and displays the number grades entered
        print("Total grades entered = {}".format(len(all_grades)))

    def get_ratio(self, ratio_grades, total_grades):
        return str(Fraction(ratio_grades, total_grades))


if __name__ == "__main__":
    # Make class object
    darraj = DarrajEC1Q1()

    # Call function - sequence of grades obtained from the user.
    grades_sequence = darraj.get_grades_seq()

    # call function - computes information related to a sequence of grades
    darraj.computes_information(grades_sequence)
