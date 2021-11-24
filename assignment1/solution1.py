# 1. Using any of the conditional statement learnt to write a simple Python program that will 
# output the score and remark eg “Your score is 76 and this is Excellence” using the algorithm 
# below. Make sure that invalid score such value greater than 100 or less than 1 are detected 
# and reported 
#  0 – 34 = Fail 
#  35 – 44 = Pass 
#  45 – 49 = Fair 
#  50 – 59 = Good 
#  60 – 69 = Very good
#  70 – 100 = Excellence



print('Welcome to the grading system. I hope you have a good grade.')
print('    ')
score = input('Enter Your Score: ')

if score >= str(0) and score <= str(34):
    print(f'Your score is {score} and you failed.Try harder next time!!')

elif score >= str(35) and score <= str(44):
    print(f'Your score is {score} and you pass.')

elif score >= str(45) and score <= str(49):
    print(f'Your score is {score}, this is a fair score. Intensify your efforts.')

elif score >= str(50) and score <= str(59):
    print(f'Your score is {score} and this is good.')

elif score >= str(60) and score <= str(69):
    print(f'Your score is {score} and this is very good.')

elif score >= str(70) and score <= str(100) :
    print(f'Your score is {score} and this is excellent. Welldone')

# elif score < str(1):
#     print(f'Ooops!! Sorry but this is an invalid score. Please recheck.')

# elif score > str(100):
#     print(f'Please check well again. This score {score} is invalid')

else:
    print('This score is invalid')