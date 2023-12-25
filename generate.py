import os
from openai import OpenAI
import json

client = OpenAI(api_key=os.environ['OPENAI_KEY'])

def generate_answers(instructions, gpt_model="gpt-4-1106-preview"):
    data = []
    for prompt in instructions:
        response = client.chat.completions.create(messages=[{
                                                        "role": "user",
                                                        "content": prompt
                                                    }],
                                                    model=gpt_model)
        data.append(response.choices[0].message.content)
    return data

def extract_questions_from_file(file_path):
    questions = []
    current_question = ""
    with open(file_path, "r") as file:
        for line in file:
            if line.strip().lower().startswith("question"):
                if current_question != "":
                    questions.append(current_question.strip())
                    current_question = ""
            else:
                current_question += line
        if current_question != "":
            questions.append(current_question.strip())

    return questions

if __name__ == "__main__":
    for i in range(1, 27):
        file_path = f"principles/principle_{i}.txt"
        questions = []
        answers = []
        q = extract_questions_from_file(file_path)
        for _ in range(10):
            a = generate_answers(q)
            questions.extend(q)
            answers.extend(a)
        qa_pairs = [{"instruction": q, "output": a} for q, a in zip(questions, answers)]
        json_data = json.dumps(qa_pairs, indent=4)
        filename = f'principle_{i}.json'
        folder_path = 'gpt4'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        f_path = os.path.join(folder_path, filename)
        with open(f_path, 'w') as file:
            file.write(json_data)