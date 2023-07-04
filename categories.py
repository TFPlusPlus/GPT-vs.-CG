import json

num_of_generations = 10

category = ["Topic", "Bloom's Taxonomy", "Question Type", "Difficulty Level", "Input Type", "Output Type", "Reasoning", "Solution Process"]
options = [
    ["Geometry", "Graphics Introduction", "Color", "Illumination and Shading", "3D Modelling", "Texture Mapping", "Ray Tracing", "Parametric Curves and Surfaces"],
    ["Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create"],
    ["Multiple-Choice Question", "Written response", "Programming"],
    ["Easy", "Easy - Medium", "Medium", "Medium - Hard", "Hard"],
    ["Text", "Mathematical formula", "Image", "Code (OpenGL)"],
    ["Text", "Mathematical formula", "Image", "Code (OpenGL)"],
    ["Inductive", "Deductive", "Abductive"],
    ["Concept recall", "Calculation", "Geometry/Transformation", "Programming"]
]

for i in range(num_of_generations):
    category.append("Generation " + str(i+1))
    options.append(["Correct explanation", "Conceptual error", "Calculation error", "Logic error"])

categories = []
for i in range(len(category)):
    categories.append({"category": category[i], "options": options[i]})

json.dump(categories, open("categories.json", "w"), indent=4)