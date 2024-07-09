# Create class known as QuizBrain
class QuizBrain:

    # define the __init__function with parameter of question_list
    def __init__(self, question_list):
        # Assigning question number
        self.question_number = 0
        # Assigning the question_list as question_list
        self.question_list = question_list
        # Assigning the initial score
        self.score = 0

    # Define a function known as still_has_questions
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Define the function known as next question
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q. {self.question_number}: {current_question.text}(True / False): ").lower()
        self.check_answer(user_answer, current_question.answer)

    # Define the function known as check answer
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's incorrect!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}.")
        print("\n")