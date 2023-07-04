from preprocess import preprocess
from ask import ask, ask2
from parse import parse

with open("test1.txt", 'r') as file1, open("test2.txt", 'w') as file2:
    while True:
        id = file1.readline()
        if id == "":
            break
        file1.readline()
        question = ""
        while True:
            line = file1.readline()
            if line == "\n":
                break
            question += line
        answer = ""
        while True:
            line = file1.readline()
            if line == "\n" or line == "":
                break
            answer += line
        generated = ask2(question, num_of_generations = 10)
        print
        file2.write(id)
        file2.write("\n")
        file2.write(question)
        file2.write("\n")
        file2.write(answer)
        file2.write("\n")
        for generation in generated:
            file2.write(generation)
            file2.write("\n\n")