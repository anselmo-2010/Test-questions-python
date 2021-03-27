question_prompts = [
    "Capital of Kyrgyzstan ?\n(a) Bishkek\n(b) Osh\n(c) Batken\n\n",
    "Capital of Turkey ?\n(a) Ankara\n(b) Stambul\n(c) Bursa\n\n",
    "Capital of USA ?\n(a) Indiana\n(b) New-York\n(c) Washington\n\n"
]

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + " / " + str(len(questions)) + " correct")

run_test(questions)

