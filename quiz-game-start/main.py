from question_model import Question
from data import question_data
from quiz_brain import QuizBrain # from file import class

questionBank = []
for question in question_data:
    questionBank.append(Question(qText=question["text"], qAnswer=question["answer"]))

quiz = QuizBrain(questionBank)

while quiz.stillHasQuestions():
    quiz.nextQuestion()

print("Quiz completed")
print(f"your FINAL SCORE is {quiz.score}/{quiz.qNo}")