# data = """
# X,AA,B,C,D,D,D
# a,0,0,1,0,0,1
# b,0,1,1,1,1,1
# c,1,0,1,0,0,0
# d,0,0,0,0,0,0
# """
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

def P(var, conditions = [], collective = False):    # The conditions are joined with AND operators
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
        return "{:.2f}%".format(sum(results) / len(var_array) / len(results) * 100)
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

# print(P("D", conditions=["A", "B"], collective=False))
# print(P("Correct answer"))
# print(P("Correct answer", collective=True))
# print(P("Correct answer", conditions=["Question Type: Multiple-Choice Question"], collective=True))
# print(P("Correct answer", conditions=["Question Type: Programming"], collective=True))
# l = P("Correct answer", conditions=["Question Type: Programming"], collective=False)
# print(sum([1 for i in l.values() if i > 0]) / len(l))
print(P("Correct answer", conditions=["Input Type: Image description (novice)"], collective=True))
print(P("Correct answer", conditions=["Input Type: Image description (informed)"], collective=True))