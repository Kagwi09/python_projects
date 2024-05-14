from data_base import quiz_questions
from data_base import options

score = 0


def game(user_guess, correct_answer):
    if user_guess == correct_answer:
        return True
    else:
        return False


for question_num in range(len(quiz_questions)):
    print('****************************************************')
    print(quiz_questions[question_num]['Question'])
    for answer in options[question_num]:
        print(answer)

    guess = input('Enter your answer (A,B,C,D) : ').upper()
    is_correct = game(guess, quiz_questions[question_num]['answer'])
    if is_correct:
        score += 1
        print(f'Correct. Your score is {score} / {score}')
    else:
        print('Wrong answer')
print(f'You have given {score} correct answers')
print(f'Your current score is {(score / len(quiz_questions)) * 100} %')