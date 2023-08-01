def P_AND(var, conditions = [], collective = False):
    var_array = []
    cond_array = []
    for i in range(len(headers)):
        if var in headers[i]:
            var_array.append(i)
        for cond in conditions:
            if cond in headers[i]:
                cond_array.append(i)
                break
    if collective:
        results = []
        for row in data:
            valid = True
            for cond in cond_array:
                if not row[cond]:
                    valid = False
                    break
            if valid:
                results.append(sum([row[i] for i in var_array]))
        if len(results) == 0:
            return "N/A"
        return "{:.2f}% ({} / {})".format(sum(results) / len(var_array) / len(results) * 100, sum(results), len(var_array) * len(results))
    else:
        results = {}
        for row in data:
            valid = True
            for cond in cond_array:
                if not row[cond]:
                    valid = False
                    break
            if valid:
                results[row[0]] = sum([row[i] for i in var_array]) / len(var_array) * 100
                # results.append("{},{:.2f}%".format(row[0], sum([row[i] for i in var_array]) / len(var_array) * 100))
        if len(results) == 0:
            return "N/A"
        return results

def P_OR(var, conditions = [], collective = False):
    var_array = []
    cond_array = []
    for i in range(len(headers)):
        if var in headers[i]:
            var_array.append(i)
        for cond in conditions:
            if cond in headers[i]:
                cond_array.append(i)
                break
    if collective:
        results = []
        for row in data:
            valid = False
            for cond in cond_array:
                if row[cond]:
                    valid = True
                    break
            if valid:
                results.append(sum([row[i] for i in var_array]))
        if len(results) == 0:
            return "N/A"
        return "{:.2f}% ({} / {})".format(sum(results) / len(var_array) / len(results) * 100, sum(results), len(var_array) * len(results))
    else:
        results = {}
        for row in data:
            valid = False
            for cond in cond_array:
                if row[cond]:
                    valid = True
                    break
            if valid:
                results[row[0]] = sum([row[i] for i in var_array]) / len(var_array) * 100
                # results.append("{},{:.2f}%".format(row[0], sum([row[i] for i in var_array]) / len(var_array) * 100))
        if len(results) == 0:
            return "N/A"
        return results
    
# data = """
# X,AA,B,C,D,D,D
# a,0,0,1,0,0,1
# b,0,1,1,1,1,1
# c,1,0,1,0,0,0
# d,0,0,0,0,0,0
# """
# print(P_AND("D", conditions=["A", "B"], collective=False))

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

""" General Statistics """
print(P_AND("Correct answer", collective=True))
print(P_AND("Minor error", collective=True))
# print(P_AND("Correct answer", conditions=["Question Type: Multiple-Choice Question"], collective=True))
# print(P_AND("Correct answer", conditions=["Question Type: Programming"], collective=True))
# l = P_AND("Correct answer", conditions=["Question Type: Programming"], collective=False)
# print("{:.2f}%".format(sum([1 for i in l.values() if i > 0]) / len(l) * 100))
# print(P_AND("Correct answer", conditions=["Input Type: Image description (novice)"], collective=True))
# print(P_AND("Correct answer", conditions=["Input Type: Image description (informed)"], collective=True))

""" Novice vs Informed"""
# novice = P_AND("Correct answer", conditions=["Input Type: Image description (novice)"], collective=False).values()
# informed = P_AND("Correct answer", conditions=["Input Type: Image description (informed)"], collective=False).values()
# for i in novice:
#     print(i)
# print()
# for i in informed:
#     print(i)

""" Inductive vs Deductive """
# print(P_AND("Correct answer", conditions=["Reasoning: Deductive"], collective=True))
# print(P_AND("Correct answer", conditions=["Reasoning: Inductive"], collective=True))

""" Topic """
# print(P_AND("Correct answer", conditions=["Topic: Geometry"], collective=True))
# print(P_AND("Correct answer", conditions=["Topic: Graphics Introduction"], collective=True))
# print(P_AND("Correct answer", conditions=["Topic: Color"], collective=True))
# print(P_AND("Correct answer", conditions=["Topic: Illumination and Shading"], collective=True))
# print(P_AND("Correct answer", conditions=["Topic: 3D Modelling"], collective=True))
# print(P_AND("Correct answer", conditions=["Topic: Texture Mapping"], collective=True))
# print(P_AND("Correct answer", conditions=["Topic: Ray Tracing"], collective=True))
# print(P_AND("Correct answer", conditions=["Topic: Parametric Curves and Surfaces"], collective=True))
# print(P_AND("Correct answer", conditions=["Topic: Image Processing"], collective=True))