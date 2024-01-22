class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def display(self):
        print(self.text)
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")
        print()

    def check_answer(self, user_answer):
        return user_answer == self.correct_option


class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start_game(self):
        print("Welcome to the Quiz Game!")
        for question in self.questions:
            question.display()
            user_answer = int(input("Enter the number of your answer: "))
            if question.check_answer(user_answer):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {question.correct_option}: {question.options[question.correct_option - 1]}\n")

        print(f"Game Over! Your final score is: {self.score}/{len(self.questions)}")


# Sample questions
question1 = Question("What is the capital of France?", ["Paris", "Berlin", "Madrid", "Rome"], 1)
question2 = Question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], 2)
question3 = Question("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], 2)

# Create a list of questions
questions_list = [question1, question2, question3]

# Create a QuizGame instance with the list of questions
quiz_game = QuizGame(questions_list)

# Start the game
quiz_game.start_game()
