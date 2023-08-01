file = open("data.csv", "r")
data = file.read()
file.close()

data = [row.split(',') for row in data.strip().split('\n')]
headers = data[0]
data = data[1:]
for i in range(len(data)-1, -1, -1):
    for j in range(1, len(data[0])):
        data[i][j] = int(data[i][j])

# end = headers.index("Generation 1: Correct answer")
# novice = headers.index("Input Type: Image description (novice)")
# informed = headers.index("Input Type: Image description (informed)")
# for i in range(len(data)-1):
#     if data[i][0][-1] == "a" and data[i+1][0][-1] == "b":
#         data[i+1][1:end] = data[i][1:end]
#         data[i][novice] = 1
#         data[i][informed] = 0
#         data[i+1][novice] = 0
#         data[i+1][informed] = 1

category_indices = [1]
category = headers[1][:headers[1].find(":")]
for i in range(2, len(headers)):
    current_category = headers[i][:headers[i].find(":")]
    if current_category != category:
        category = current_category
        category_indices.append(i)
category_indices.append(len(headers))
# print(category_indices)

for i in range(len(data)):
    for j in range(len(category_indices)-1):
        if sum(data[i][category_indices[j]:category_indices[j+1]]) == 0:
            print(data[i][0], headers[category_indices[j]])

file = open("data.csv", "w")
file.write(",".join(headers) + "\n")
for row in data:
    file.write(",".join([str(i) for i in row]) + "\n")
file.close()