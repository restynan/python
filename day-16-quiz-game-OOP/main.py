from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_obj = Question(question["text"], question["answer"])
    question_bank.append(question_obj)

print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print("you have completed the Quiz")
print(f"your final score is {quiz.score}/{quiz.question_number}")
