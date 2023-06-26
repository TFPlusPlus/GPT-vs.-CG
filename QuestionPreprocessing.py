def preprocess(text):
    l = text.split("\n")
    for i in range(len(l)-1, -1, -1):
        if l[i].strip() == "":
            l.pop(i)
        if len(l[i]) == 2 and l[i][1] == ".":
            l[i] = l[i] + " " + l[i+1]
            l.pop(i+1)
    return "\n".join(l)

file = open("Question.txt", "r")
text = file.read()
file.close()
file = open("Question.txt", "w")
file.write(preprocess(text))
file.close()