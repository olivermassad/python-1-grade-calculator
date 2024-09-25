#Asks user for the number of completed labs/quizzes 
num_labs_completed = int(input('Enter the numer of labs completed: '))
num_quizzes_completed = int(input('Enter the number of quizzes completed: '))

#Checks if the number of completed labs/quizzes is over 6 and fixes it
if num_labs_completed > 6:
    num_labs_completed = 6
    
if num_quizzes_completed > 6:
    num_quizzes_completed = 6

#Inputs all necessary grade variables our of 100%
assignement_1 = float(input('Enter grade for Assignment 1: '))
assignement_2 = float(input('Enter grade for Assignment 2: '))
assignement_3 = float(input('Enter grade for Assignment 3: '))
assignement_4 = float(input('Enter grade for Assignment 4: '))
midterm_1 = float(input('Enter grade for Midterm 1: '))
midterm_2 = float(input('Enter grade for Midterm 2: '))
final_exam = float(input("Enter grade for Final Exam: "))
preperations = float(input('Enter grade for Midterms and Final Preparation: '))

#Caculates the overall of each category to facilitate the last variable
labs_overall = (num_labs_completed/6*20)
quizzes_overall = (num_quizzes_completed/6*15)
assignements_overall = (assignement_1/100*4) + (assignement_2/100*4) + (assignement_3/100*4) + (assignement_4/100*4)
midterms_overall = (midterm_1/100*12.5) + (midterm_2/100*12.5)
final = (final_exam/100*18)
preperations = (preperations/100*6)

overall_grade = labs_overall + quizzes_overall + assignements_overall + midterms_overall + final + preperations

#prints the final result
print('Your overall grade is: ' + str(round(overall_grade, 2)) + '%')
