from prepare import prepare
from ask import ask_json

filename = "2019ab"

prepare(filename, filename + ".json")

# ask_json(filename + ".json", filename + "-a.json", num_of_generations = 10, test = True)
