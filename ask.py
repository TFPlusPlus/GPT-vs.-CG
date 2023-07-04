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

# ans = ask("How will the weather be tomorrow in Auckland?", num_of_generations = 2)
# print(ans)
