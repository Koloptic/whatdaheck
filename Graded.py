""" Exam Grade Calculator
Name of Exam
Max. Pos Score
Score Received
Show % Score and Grade
"""

print("Hi, Welcome to my Grading Evaluation Calculator")
print()
examName = input("What class would you like to evaluate?:")
print()
examMScore = int(input("What is the maximum scoring points for this exam?:"))
print()
examScore = int(input("What score did you receive:"))
print()
scorePct = round(examScore/examMScore*100,2)
def get_grade(grade): #Starts to define get_grade and allows for an input into grade via another variable
    if grade > 100 or grade < 0:
        print("Please enter a valid score, extra credit is not calculated")
        return None # Returns Null to get_grade(grade)
    grades = {
        (90,100): "A",
        (80,89): "B",
        (70,79): "C",
        (60,69): "D",
        (0,59): "F"
    }
    for (gradeL,gradeM), scoring in grades.items():  #scoring refers to 3rd variable of grades items
        if gradeL <= grade <= gradeM:
            return scoring # Returns Letter Grade to get_grade to be called later
    return None
finalGrade = get_grade(scorePct) # Using a variable to input into get_grade(grade)
if finalGrade == "A":
    print(f"You did an \033[42m Excellent \033[0m job")
elif finalGrade =="F":
    print(f"\033[31m Please review the course material and try again!\033[0m")
print()
if finalGrade is not None:
    print(f"Your {examName} was graded a {scorePct}% which is a {get_grade(scorePct)}")