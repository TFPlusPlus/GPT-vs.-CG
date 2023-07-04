import json
import math

def parse(path, num_of_generations = 10):
    with open(path, 'r') as file:
        questions = []
        while True:
            id = file.readline()
            if id == "":
                break
            file.readline()
            question = ""
            while True:
                line = file.readline()
                if line == "\n":
                    break
                question += line
            answer = ""
            while True:
                line = file.readline()
                if line == "\n":
                    break
                answer += line
            generated = []
            for i in range(num_of_generations):
                generation = ""
                while True:
                    line = file.readline()
                    if line == "\n" or line == "":
                        break
                    generation += line
                generated.append(generation.strip())
            question_dict = {
                "id": int(id),
                "question": question.strip(),
                "answer": answer.strip(),
                "generated": generated
            }
            questions.append(question_dict)
    with open(path[:-4] + ".json", 'w') as file:
        json.dump(questions, file, indent=4)

parse("Questions.txt")
