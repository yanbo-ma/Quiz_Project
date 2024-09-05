from question_model import Question
from data import question_data
from quiz_brain import Quiz_brain


question_bank=[]
for i in question_data:
    question_bank.append(Question(i['text'],i['answer']))


quiz = Quiz_brain(question_bank)


while quiz.still_questions():
    quiz.next_question()

quiz.end_quiz()