from question_model import Question
from data import question_data, length
from quiz_brain import QuizBrain

Question_Bank = []

for i in range(0, length):
    new_q = Question(question_data[0]["results"][i]["question"], question_data[0]["results"][i]["correct_answer"],
                     question_data[0]["results"][i]["options"])
    Question_Bank.append(new_q)

quiz = QuizBrain(Question_Bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"You have completed the quiz. Your final score is {quiz.score}.")

