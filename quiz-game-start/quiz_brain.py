class QuizBrain:
    def __init__(self, qlist):
        self.qNo = 0
        self.questionList = qlist
        self.score = 0

    def nextQuestion(self):
        self.questionText = self.questionList[self.qNo].qText
        self.correctAnswer = self.questionList[self.qNo].qAnswer
        self.userAnswer = input(f"Q.{self.qNo+1} {self.questionText}(true/false)? ").lower()
        self.qNo += 1
        self.checkAnswer(self.userAnswer, self.correctAnswer)

    def stillHasQuestions(self):
        # if self.qNo >= len(self.questionList):
        #     return False
        # return True
        return self.qNo < len(self.questionList)

    def checkAnswer(self, userAnswer, correctAnswer):
        if userAnswer.lower() == correctAnswer.lower():
            print("Thats correct...")
            self.score += 1
        else:
            print("Thats wrong!!!")
        print(f"Correct answer is {correctAnswer} ")
        print(f"Your score is: {self.score}/{self.qNo}")
        print("\n")


