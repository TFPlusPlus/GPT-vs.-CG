import openai

def ask(question, temperature = 1.0, num_of_generations = 10):
    responses = []
    for i in range(num_of_generations):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": question}
            ],
            temperature = temperature
        )
        responses.append(response.choices[0].message.content.strip())
    return responses

def ask2(question, num_of_generations = 10):
    return ["Answer Text {}".format(i) for i in range(num_of_generations)]

def ask_file(filename_input, filename_output, num_of_generations = 10, test = True):
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

# ans = ask("How will the weather be tomorrow in Auckland?", num_of_generations = 2)
# print(ans)
