class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = current_question.answer
        user_answer = input(
            f"Q.{self.question_number + 1}:  {current_question.text} (options: {current_question.options}) : ")
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            print("Yay!!! That's Right.")
            self.score += 1
        else:
            print("Oops! That's incorrect.")

        print(f"The correct answer is {answer}.")
        print(f"Yore score is {self.score}/{self.question_number}\n")
