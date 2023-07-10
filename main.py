from preprocess import preprocess
from ask import ask_json
from parse import parse

filename = "2023a"

preprocess(filename, filename + "-1")

# parse(filename + "-1", filename + ".json", num_of_generations=0)

# ask_json(filename + "-q.json", filename + "-a.json", num_of_generations = 10, test = True)

# parse(filename + "-2", filename + ".json", num_of_generations = 10)

# s = """

# """

# print(s.replace("\n\n", "\n"))