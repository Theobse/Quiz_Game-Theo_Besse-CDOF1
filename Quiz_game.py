import json

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

    def get_user_answer(self):
        while True:
            try:
                user_answer = int(input("Enter the number of your answer: "))
                if 1 <= user_answer <= len(self.questions.options):
                    return user_answer
                else:
                    print("Please enter a valid number.")
            except ValueError:
                print("Please enter a valid number.")

    def start_game(self):
        print("Welcome to the Quiz Game!")

        for question in self.questions:
            question.display()
            
            user_answer = self.get_user_answer()

            if question.check_answer(user_answer):
                print("Correct!\n")
                self.score += 1
            else:
                correct_option = question.correct_option
                correct_answer = question.options[correct_option - 1]
                print(f"Wrong! The correct answer was {correct_option}: {correct_answer}\n")

        print(f"Game Over! Your final score is: {self.score}/{len(self.questions)}")


def load_questions_from_file(filename):
    with open(filename, "r") as file:
        questions_data = json.load(file)

    questions = []
    for data in questions_data:
        question = Question(data["text"], data["options"], data["correct_option"])
        questions.append(question)

    return questions


# Sample questions (replace with loading questions from a file)
questions_list = load_questions_from_file("questions.json")

# Create a QuizGame instance with the list of questions
quiz_game = QuizGame(questions_list)

# Start the game
quiz_game.start_game()
