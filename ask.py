import openai
import json

def ask(question, temperature = 0.75, num_of_generations = 10):
    responses = []
    for i in range(num_of_generations):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": question}
            ],
            temperature = temperature
        )
        responses.append(response.choices[0].message.content.strip().replace("\n\n", "\n"))
    return responses

def ask2(question, num_of_generations = 10):
    return ["Answer Text {}".format(i ** 2) for i in range(num_of_generations)]

def ask_txt(filename_input, filename_output, num_of_generations = 10, test = True):
    with open(filename_input, 'r') as file1, open(filename_output, 'w') as file2:
        while True:
            id = file1.readline()
            if id == "":
                break
            file1.readline()
            question = ""
            while True:
                line = file1.readline()
                if line == "\n" or line == "":
                    break
                question += line
            answer = ""
            while True:
                line = file1.readline()
                if line == "\n" or line == "":
                    break
                answer += line
            if test:
                generated = ask2(question, num_of_generations = num_of_generations)
            else:
                generated = ask(question, num_of_generations = num_of_generations)
            file2.write(id)
            file2.write("\n")
            file2.write(question)
            file2.write("\n")
            file2.write(answer)
            file2.write("\n")
            for generation in generated:
                file2.write(generation)
                file2.write("\n\n")


def ask_json(filename_input, filename_output, num_of_generations = 10, test = True):
    with open(filename_input, "r") as file:
        data = json.load(file)
        for i in range(len(data)):
            if test:
                generated = ask2(data[i]["question"], num_of_generations = num_of_generations)
            else:
                generated = ask(data[i]["question"], num_of_generations = num_of_generations)
            data[i]["generated"] = generated
    with open(filename_output, "w") as file:
        json.dump(data, file, indent = 4)
