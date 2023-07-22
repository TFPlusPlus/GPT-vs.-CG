data = """
X,A,B,C,D,D,D
a,0,0,1,0,0,1
b,0,1,1,1,1,1
c,1,0,1,0,0,0
d,0,0,0,0,0,0
"""
file = open("data.csv", "r")
data = file.read()

data = [row.split(',') for row in data.strip().split('\n')]
headers = data[0]
data = data[1:]
for i in range(len(data)-1, -1, -1):
    delete = True
    for j in range(1, len(data[0])):
        data[i][j] = int(data[i][j])
    if sum(data[i][1:]) == 0:
        data.pop(i)

def P(var, conditions = [], collective = False):    # The conditions are joined with AND operators
    var_array = []
    cond_array = []
    for i in range(len(headers)):
        if headers[i] == var:
            var_array.append(i)
        if headers[i] in conditions:
            cond_array.append(i)
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
        results = []
        for row in data:
            valid = True
            for cond in cond_array:
                if not row[cond]:
                    valid = False
                    break
            if valid:
                results.append("{},{:.2f}%".format(row[0], sum([row[i] for i in var_array]) / len(var_array) * 100))
        if len(results) == 0:
            return "N/A"
        return "\n".join(results)

# print(P("", conditions=["A", "B"], collective=False))
print(P("Correct answer"))
print(P("Correct answer", collective=True))
