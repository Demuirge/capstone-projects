#PROJECT TWO: EXAM WIZARD

question_1 = "\nExplain the process of photosynthesis."

keywords_1 = {"Photosynthesis": 2, "Light energy": 1, "Chemical energy": 1, "Chloroplasts": 2, "Chlorophyll": 1 , "Carbon dioxide": 1, "Water": 1 , "Glucose": 1, "Oxygen": 1, "ATP": 1}

question_and_keywords = {question_1: keywords_1}

def exam_wizard():
    points = 0
    question_scores = {}
    for question, keywords in question_and_keywords.items():
        print(question)
        answer = input("\nAnswer: ")

        for keyword, point in keywords.items():
            if keyword in answer or keyword.lower() in answer:
                points += point
        question_scores[question] = str(points) + " points"
        points = 0
    
    print(question_scores)

exam_wizard()
