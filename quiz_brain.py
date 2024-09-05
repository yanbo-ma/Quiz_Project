from question_model import Question
class Quiz_brain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.current_score =0

    def next_question(self):
        answer = input(f'Q {self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)')
        self.check_answer(answer)
        self.question_number += 1

    def end_quiz(self):
        print("You've completed the quiz")
        print(f"Your final score was {self.current_score}/{self.question_number}")

    def still_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self,answer):
        if answer == self.question_list[self.question_number].answer:
            print("You got it right!")
            print(f"The correct answer was: {self.question_list[self.question_number].answer}")
            self.current_score += 1
            print(f'Your current score is {self.current_score}/{self.question_number + 1}')
        else:
            print("That's wrong.")
            print(f"The correct answer was: {self.question_list[self.question_number].answer}")
            print(f'Your current score is {self.current_score}/{self.question_number + 1}')