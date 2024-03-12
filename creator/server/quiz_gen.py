import os
import re
import random
import json

def generate_quiz(text, num_questions=5):
    sentences = re.split(r'(?<=[.!?]) +', text.strip())
    questions = random.sample(sentences, min(num_questions, len(sentences)))
    options = [sentence.split()[:-1] for sentence in sentences]
    quiz_data = []
    for i, question in enumerate(questions):
        question_data = {
            "id": i+1,
            "question": question.strip(),
            "options": []
        }
        correct_answer = question.split(' ')[-1]
        options_list = [correct_answer] + random.sample(options[i], min(3, len(options[i])))
        random.shuffle(options_list)
        for j, option in enumerate(options_list):
            option_text = ''.join(option)
            if "." in option_text:
                option_text = option_text.replace(".", "")
            option_data = {
                "op": chr(97+j),
                "text": option_text,
                "correct": option == correct_answer
            }
            question_data["options"].append(option_data)
        quiz_data.append(question_data)

    output_folder = "OutputFiles"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    with open(os.path.join(output_folder, "Quiz.json"), "w") as json_file:
        json.dump(quiz_data, json_file, indent=2)
    
