import json

num_of_generations = 10

category = ["Topic", "Bloom's Taxonomy", "Question Type", "Difficulty Level", "Input Type", "Output Type", "Reasoning", "Solution Process"]
options = [
    ["Geometry", "Graphics Introduction", "Color", "Illumination and Shading", "3D Modelling", "Texture Mapping", "Ray Tracing", "Parametric Curves and Surfaces", "Image Processing"],
    ["Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create"],
    ["Multiple-Choice Question", "Written response", "Programming"],
    ["Easy", "Easy - Medium", "Medium", "Medium - Hard", "Hard"],
    ["Text", "Mathematical formula", "Image description (novice)", "Image description (informed)", "Code"],
    ["Text", "Mathematical formula", "Image description (novice)", "Image description (informed)", "Code"],
    ["Deductive", "Inductive", "Abductive"],
    ["Concept recall", "Calculation", "Geometry/Transformation", "Programming"]
]

for i in range(num_of_generations):
    category.append("Generation " + str(i+1))
    options.append(["Correct answer", "Minor error", "Correct explanation", "Conceptual error", "Calculation error", "Logic error", "No explanation"])

categories = []
for i in range(len(category)):
    categories.append({"category": category[i], "options": options[i]})

json.dump(categories, open("categories.json", "w"), indent=4)