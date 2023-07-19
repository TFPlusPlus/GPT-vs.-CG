import json

def prepare(filename_input, filename_output):
    file = open(filename_input, "r")
    text = file.read().strip()
    file.close()
    l = text.split("\n")
    for i in range(len(l)-1, -1, -1):
        if l[i].strip() == "":
            l.pop(i)
        elif len(l[i]) == 2 and l[i][1] == ".":
            l[i] = l[i] + " " + l[i+1]
            l.pop(i+1)
    k = 1
    l = ["{}{:02d}\n".format(filename_input, k)] + l
    for i in range(1, len(l)):
        if i == len(l) - 1:
            if l[i] == "~~~":
                l[i] = "\nNULL".format(filename_input)
        else:
            if l[i] == "~~~":
                k += 1
                l[i] = "\nNULL\n\n{}{:02d}\n".format(filename_input, k)
            if l[i] == "~~":
                k += 1
                l[i] = "\n{}{:02d}\n".format(filename_input, k)
    file = open(filename_output, "w")
    file.write("\n".join(l))
    file.write("\n")
    file.close()
    with open(filename_output, 'r') as file:
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
            question_dict = {
                "id": id.strip(),
                "question": question.strip(),
                "answer": answer.strip(),
                "generated": []
            }
            questions.append(question_dict)
    with open(filename_output, 'w') as file:
        json.dump(questions, file, indent=4)