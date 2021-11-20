print('Welcome to the grading system. I hope you have a good grade.')
print('    ')
score = input('Enter Your Score: ')

if score <= str(34):
    print(f'Your score is {score} and you failed.Try harder next time!!')

elif score <= str(44):
    print(f'Your score is {score} and you pass.')

elif score <= str(49):
    print(f'Your score is {score}, this is a fair score. Intensify your efforts.')

elif score <= str(59):
    print(f'Your score is {score} and this is good.')

elif score <= str(69):
    print(f'Your score is {score} and this is very good.')

elif score <= str(100):
    print(f'Your score is {score} and this is excellent. Welldone')

elif score < str(1):
    print(f'Ooops!! Sorry but this is an invalid score. Please recheck.')

elif score > str(100):
    print(f'Please check well again. This score {score} is invalid')

else:
    print('Assignment not done properly')