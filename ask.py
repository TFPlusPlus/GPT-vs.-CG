import openai

def ask(question, temperature = 1.0):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": question}
        ],
        temperature = temperature
    )
    return response.choices[0].message.content.strip()

# ans = ask("What is the dot product of the two vectors (0, 1, 2) and (1, 2, 3)?")
# print(ans)