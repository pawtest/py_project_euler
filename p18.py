triangle = []
# problem 18 and 67 are essentially the same problem
# with open("18_input.txt", "r") as input:
with open("67_input.txt", "r") as input:
    for line in input:
        triangle.append([int(x) for x in line.split()])

#print(triangle)

for row in triangle[1:]:
    i = len(row) -1
    for j in range(len(row)):
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        elif j == i:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])
            
print(max(triangle.pop()))