from preprocess import preprocess
from ask import ask_json
from parse import parse
import codecs

filename = "2023a"

# preprocess(filename, filename + "-1")

# with codecs.open(filename + "-1", "r", "utf-8") as f, codecs.open(filename + "-2", "w", "utf-8") as g:
#     l = f.read().split("\n")
#     for i in range(len(l)):
#         if len(l[i]) > 4 and l[i].strip()[3] == "\\":
#             l[i] = l[i].strip()[0:3] + "$$" + l[i].strip()[3:] + "$$"
#         elif "\\" in l[i]:
#             l[i] = "$$" + l[i].strip() + "$$"
#     for i in range(len(l)):
#         g.write(l[i] + "\n")

parse(filename + "-2", filename + ".json", num_of_generations=0)

# ask_json(filename + "-q.json", filename + "-a.json", num_of_generations = 10, test = True)

# parse(filename + "-2", filename + ".json", num_of_generations = 10)
