import json
import math

def parse(filename_input, filename_output, num_of_generations = 10):
    with open(filename_input, 'r') as file:
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
                if line == "\n" or line == "":
                    break
                answer += line
            if num_of_generations == 0:
                generated = ["EMPTY {}".format(i + 1) for i in range(10)]
            else:
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
                "id": id.strip(),
                "question": question.strip(),
                "answer": answer.strip(),
                "generated": generated
            }
            questions.append(question_dict)
    with open(filename_output, 'w') as file:
        json.dump(questions, file, indent=4)

# parse("Questions.txt")
