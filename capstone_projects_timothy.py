# PROJECT ONE: CBT

question_1 = """\n1. What is 2 + 2?
a) 3
b) 4
c) 5
d) 6
"""

question_2 = """\n2. What color is the sky on a clear day?
a) Red
b) Blue
c) Green
d) Yellow
"""

question_3 = """\n3. How many legs does a spider have?
a) 6
b) 7
c) 8
d) 9
"""

question_4 = """\n4. What sound does a cow make?
a) Meow
b) Bark
c) Moo
d) Quack
"""

question_5 = """\n5. What is the opposite of 'hot'?
a) Warm
b) Cold
c) Cool
d) Boiling
"""

questions_and_answers = {question_1: "b", question_2 :"b", question_3: "c", question_4: "c", question_5: "b"}

def test_questions():
    score_points = 0
    options = ("a", "b", "c", "d")
    for question, answers in questions_and_answers.items():
        print(question)

        while True:
            answer = input("Enter an option from a to d: ").lower()
            if answer not in options:
                print("You must choose from options a to d\n")
                continue
            if answer in options:
                if answer == answers:
                    score_points += 1
            break
    
    print(f"\nAt the end of the the CBT exam, you scored {score_points} points")

test_questions()



