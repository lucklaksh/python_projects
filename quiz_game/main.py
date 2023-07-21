from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_question = Question(question['text'], question['answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("you have completed the Quiz")
print(f"your final score is {quiz.score}/{quiz.question_number}")

# opentdb.com has many questions, use them to get fresh questions
#through json data put it in data.py model
# change 'text' and 'answer' correspondingly and match the key in dataset.