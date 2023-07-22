data = """
X,A,B,C,D,D,D
a,0,0,1,0,0,1
b,0,1,1,1,1,1
c,1,0,1,0,0,0
d,0,0,0,0,0,0
"""

data = [row.split(',') for row in data.strip().split('\n')]
headers = data[0]
data = data[1:]
for i in range(len(data)-1, -1, -1):
    delete = True
    for j in range(1, len(data[0])):
        data[i][j] = int(data[i][j])
        if data[i][j] != 0:
            delete = False
    if delete:
        data.pop(i)

def P(variables, conditions = [], collective = False):
    pass