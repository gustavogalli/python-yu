class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f'Q. {self.question_number}: {current_question.text} (True/False): ')
        self.check_answer(current_question.answer, user_answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, correct_answer, answer):
        if correct_answer.lower() == answer.lower():
            print('\nYou got it right!')
            self.score += 1
        else:
            print('\nThat\'s wrong.')
        print(f'The correct answer was: {correct_answer.upper()}.')
        print(f'Your current score is: {self.score}/{self.question_number}\n\n')
