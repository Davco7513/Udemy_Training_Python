from Project_day17_question_model import Question
from Project_day17_data import question_data
from Project_day17_quizz_brain import QuizzBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quizz = QuizzBrain(question_bank)

while quizz.still_has_questions():
    quizz.next_question()

print("You've completed the quizz")
print(f"Your final score was: {quizz.score}/{quizz.question_number}")
