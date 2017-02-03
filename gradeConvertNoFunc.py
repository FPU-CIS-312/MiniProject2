# gradeConvert
# prompts user for a numerical grade and converts to a letter grade
# Specifically leaves out functions


grade = eval(input("Enter the numerical grade value: "))
letterGrade = "I"
print(int(grade))
if grade >= 90:
    letterGrade = "A"
elif grade < 90 and grade >= 80:
    letterGrade = "B"
elif grade < 80 and grade >= 70:
    letterGrade = "C"
elif grade <70 and grade >= 60:
    letterGrade = "D"
else:
    letterGrade = "F"
    
print("A score of", grade, "equates to a letter grade of",letterGrade)
