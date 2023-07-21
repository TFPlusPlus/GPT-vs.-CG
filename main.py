from preprocess import preprocess
from ask import ask_json
from parse import parse
import codecs

# filename = "2023b"

# preprocess(filename, filename + "-1")

# file = codecs.open(filename + "-1", "r", "utf-8")
# text = file.read()
# file.close()
# l = text.split("\n")
# for i in range(len(l)-1, -1, -1):
#     if len(l[i].strip()) == 2 and l[i][1] == ".":
#         l[i] = l[i].strip() + " " + l[i+1]
#         l.pop(i+1)
# file = codecs.open(filename + "-1", "w", "utf-8")
# file.write("\n".join(l))
# file.write("\n")
# file.close()

# with codecs.open(filename + "-1", "r", "utf-8") as f, codecs.open(filename + "-2", "w", "utf-8") as g:
#     l = f.read().split("\n")
#     for i in range(len(l)):
#         if len(l[i]) > 4 and l[i].strip()[3] == "\\":
#             l[i] = l[i].strip()[0:3] + "$$" + l[i].strip()[3:] + "$$"
#         elif "\\" in l[i]:
#             l[i] = "$$" + l[i].strip() + "$$"
#     for i in range(len(l)):
#         g.write(l[i] + "\n")

# parse(filename + "-2", filename + ".json", num_of_generations=0)

# ask_json("Q.json", "Qs.json", num_of_generations = 10, test = False)