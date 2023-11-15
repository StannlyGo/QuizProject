class QuizBrain:

    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        if self.still_has_questions() == False:
            pass
        else:
            self.question_number += 1
            user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
            self.user_answer = user_answer
            self.current_question = current_question


    def check_answer(self):
        if self.user_answer == self.current_question.answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer was: {self.current_question.answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")

