import json

def P(var, cond_and = [], cond_not = [], cond_or1 = [], cond_or2 = [], cond_or3 = [], filter = "", collective = True):
    var_array = []
    and_array = []
    not_array = []
    or1_array = []
    or2_array = []
    or3_array = []
    for i in range(len(headers)):
        if var in headers[i]:
            var_array.append(i)
        for cond in cond_and:
            # if cond == headers[i]:
            if cond in headers[i]:
                and_array.append(i)
        for cond in cond_not:
            if cond in headers[i]:
                not_array.append(i)
        for cond in cond_or1:
            if cond in headers[i]:
                or1_array.append(i)
        for cond in cond_or2:
            if cond in headers[i]:
                or2_array.append(i)
        for cond in cond_or3:
            if cond in headers[i]:
                or3_array.append(i)
    results = {}
    numerator = {}
    denominator = {}
    for row in data:
        if filter != "" and filter not in row[0]:
            continue
        valid = True
        # AND
        for cond in and_array:
            if not row[cond]:
                valid = False
                break
        if not valid:
            continue
        # NOT
        for cond in not_array:
            if row[cond]:
                valid = False
                break
        if not valid:
            continue
        # OR1
        valid = or1_array == []
        for cond in or1_array:
            if row[cond]:
                valid = True
                break
        if not valid:
            continue
        # OR2
        valid = or2_array == []
        for cond in or2_array:
            if row[cond]:
                valid = True
                break
        if not valid:
            continue
        # OR3
        valid = or3_array == []
        for cond in or3_array:
            if row[cond]:
                valid = True
                break
        if not valid:
            continue
        results[row[0]] = sum([row[i] for i in var_array]) / len(var_array)
        numerator[row[0]] = sum([row[i] for i in var_array])
        denominator[row[0]] = len(var_array)
    if len(results) == 0:
        return "N/A"
    if collective:
        return "{:.2f}% ({} / {})".format(sum(numerator.values()) / sum(denominator.values()) * 100, sum(numerator.values()), sum(denominator.values()))
    return results

def search(terms = []):
    terms_indices = {}
    results = {}
    for term in terms:
        terms_indices[term] = []
    for i in range(len(headers)):
        for term in terms:
            if term in headers[i]:
                terms_indices[term].append(i)
    for row in data:
        valid = [False] * len(terms)
        valid_indices = [[] for i in range(len(terms))]
        for i in range(len(terms)):
            for index in terms_indices[terms[i]]:
                if row[index]:
                    valid[i] = True
                    valid_indices[i].append(index)
        if all(valid):
            results[row[0]] = []
            for indices in valid_indices:
                results[row[0]] += [headers[index] for index in indices]
    return results

# data = """
# X,AA,B,C,D,D,D
# a,0,0,1,0,0,1
# b,0,1,1,1,1,1
# c,1,0,1,0,0,0
# d,0,0,0,0,0,0
# """
# data = [row.split(',') for row in data.strip().split('\n')]
# headers = data[0]
# data = data[1:]
# for i in range(len(data)-1, -1, -1):
#     for j in range(1, len(data[0])):
#         data[i][j] = int(data[i][j])
# print(P("D", cond_not=["C"], collective=False))

file = open("data.csv", "r")
data = file.read()
data = [row.split(',') for row in data.strip().split('\n')]
headers = data[0]
data = data[1:]
for i in range(len(data)-1, -1, -1):
    for j in range(1, len(data[0])):
        data[i][j] = int(data[i][j])
    if sum(data[i][1:]) == 0:
        data.pop(i)
marks = json.load(open("marks.json", "r"))

""" General Statistics """
# print(P("Correct answer"))
# print(P("Minor error"))
# print(P("Correct answer", cond_and=["Question Type: Multiple-Choice Question"]))
# print(P("Correct answer", cond_and=["Question Type: Programming"]))
# l = P("Correct answer", cond_and=["Question Type: Programming"], collective=False)
# print("{:.2f}%".format(sum([1 for i in l.values() if i > 0]) / len(l) * 100))
# print(P("Correct answer", cond_or1=["Input Type: Image description"]))
# print(P("Correct answer", cond_and=["Input Type: Image description (novice)"]))
# print(P("Correct answer", cond_and=["Input Type: Image description (informed)"]))

""" Novice vs Informed"""
# novice = P("Correct answer", cond_and=["Input Type: Image description (novice)"], collective=False)
# informed = P("Correct answer", cond_and=["Input Type: Image description (informed)"], collective=False)
# for i in novice:
#     print(novice[i])
#     # print(novice[i] * marks[i[:7]])
# print()
# for i in informed:
#     print(informed[i])
#     # print(informed[i] * marks[i[:7]])

""" Inductive vs Deductive """
print(P("Correct answer", cond_and=["Reasoning: Deductive"]))
print(P("Correct answer", cond_and=["Reasoning: Inductive"]))

""" Input Type """
# print(P("Correct answer", cond_and=["Input Type: Text"], cond_not=["Input Type: Mathematical formula", "Input Type: Image description (novice)", "Input Type: Image description (informed)", "Input Type: Code"]))
# print(P("Correct answer", cond_and=["Input Type: Text", "Input Type: Mathematical formula"], cond_not=["Input Type: Image description (novice)", "Input Type: Image description (informed)", "Input Type: Code"]))
# print(P("Correct answer", cond_and=["Input Type: Text", "Input Type: Code"], cond_not=["Input Type: Mathematical formula", "Input Type: Image description (novice)", "Input Type: Image description (informed)"]))
# print(P("Correct answer", cond_and=["Input Type: Text", "Input Type: Image description (novice)"], cond_not=["Input Type: Mathematical formula", "Input Type: Image description (informed)", "Input Type: Code"]))
# print(P("Correct answer", cond_and=["Input Type: Text", "Input Type: Image description (informed)"], cond_not=["Input Type: Mathematical formula", "Input Type: Image description (novice)", "Input Type: Code"]))
# print(P("Correct answer", cond_not=["Input Type: Text"]))
# print(P("Correct answer", cond_or1=["Image"]))
# print(P("Correct answer", cond_not=["Image"]))
# print(P("Correct answer", cond_or1=["Programming"]))
# print(P("Minor error", cond_or1=["Programming"]))

""" Output Type """
# print(P("Correct answer", cond_and=["Output Type: Text"]))
# print(P("Correct answer", cond_and=["Output Type: Mathematical formula"]))
# print(P("Correct answer", cond_and=["Output Type: Code"]))

""" Input/Output Type """
# print(P("Correct answer", cond_not=["Math", "Image", "Code"]))
# print(P("Correct answer", cond_or1=["Math"], cond_not=["Image", "Code"]))
# print(P("Correct answer", cond_or1=["Image"]))

""" Topic """
# print(P("Correct answer", cond_and=["Topic: Geometry"]))
# print(P("Correct answer", cond_and=["Topic: Graphics Introduction"]))
# print(P("Correct answer", cond_and=["Topic: Color"]))
# print(P("Correct answer", cond_and=["Topic: Illumination and Shading"]))
# print(P("Correct answer", cond_and=["Topic: 3D Modelling"]))
# print(P("Correct answer", cond_and=["Topic: Texture Mapping"]))
# print(P("Correct answer", cond_and=["Topic: Ray Tracing"]))
# print(P("Correct answer", cond_and=["Topic: Parametric Curves and Surfaces"]))
# print(P("Correct answer", cond_and=["Topic: Image Processing"]))

""" Search """
# print(search(["Color", "Correct answer"]))

""" Marks (old) """
# codes = ["2022a", "2022b", "2023a", "2023b"]
# versions = ["a", "b"]
# for code in codes:
#     for version in versions:
#         print(code, version)
#         for i in range(10):
#             # d = P("Generation {}: Correct answer".format(i + 1), cond_not=["Topic: Image Processing"], filter=code, collective=False)
#             d = P("Generation {}: Correct answer".format(i + 1), filter=code, collective=False)
#             score = 0
#             total = 0
#             for key in d:
#                 if len(key) == 7 or key[-1] == version:
#                     score += d[key] * marks[key[:7]]
#                     total += marks[key[:7]]
#             print("{} {:.2f} ({} / {})".format(i, score / total * 100, score, total))
#             # print("{:.4f}".format(score / total))

""" Bloom's Taxonomy (not categorized well?) """
# print(P("Correct answer", cond_and=["Bloom's Taxonomy: Remember"], collective=False))
# print(P("Correct answer", cond_and=["Bloom's Taxonomy: Understand"]))
# print(P("Correct answer", cond_and=["Bloom's Taxonomy: Apply"]))
# print(P("Correct answer", cond_and=["Bloom's Taxonomy: Analyze"]))
# print(P("Correct answer", cond_and=["Bloom's Taxonomy: Evaluate"]))
# print(P("Correct answer", cond_and=["Bloom's Taxonomy: Create"]))

""" Difficulty Level """
# print(P("Correct answer", cond_and=["Difficulty Level: Easy"])) # CHANGE COND_AND TO MATCH EXACTLY
# print(P("Correct answer", cond_and=["Difficulty Level: Easy - Medium"]))
# print(P("Correct answer", cond_and=["Difficulty Level: Medium"])) # CHANGE COND_AND TO MATCH EXACTLY
# print(P("Correct answer", cond_and=["Difficulty Level: Medium - Hard"]))
# print(P("Correct answer", cond_and=["Difficulty Level: Hard"]))

""" Marks (new) """
# codes = ["2022a", "2022b", "2023a", "2023b"]
# versions = ["a", "b"]
# mcq = P("Correct answer", cond_not=["Programming"], collective=False)
# pro = P("Correct answer", cond_or1=["Programming"], collective=False)
# for code in codes:
#     for version in versions:
#         print(code, version)
#         score = 0
#         total = 0
#         for q in mcq:
#             if code in q and (len(q) == 7 or q[-1] == version):
#                 score += mcq[q] * marks[q[:7]]
#                 total += marks[q[:7]]
#         for q in pro:
#             if code in q and (len(q) == 7 or q[-1] == version):
#                 score += (pro[q] > 0) * marks[q[:7]]
#                 total += marks[q[:7]]
#         print("{:.2f}% ({} / {})".format(score / total * 100, score, total))

""" Miscellaneous """
# d = P("Input Type: Mathematical formula")