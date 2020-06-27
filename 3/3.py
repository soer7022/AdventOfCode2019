
with open("input3.txt", "r") as file:
    cable1 = file.readline()
    cable2 = file.readline()

cable1_visited = {}
cable2_visited = {}


at = (0, 0)
steps = 0
for instruction in cable1.split(","):
    moves = int(instruction[1:])
    if instruction[0] is "R":
        for i in range(moves):
            at = (at[0] + 1, at[1])
            steps += 1
            cable1_visited[at] = steps
    elif instruction[0] is "D":
        for i in range(moves):
            at = (at[0], at[1] - 1)
            steps += 1
            cable1_visited[at] = steps
    elif instruction[0] is "L":
        for i in range(moves):
            at = (at[0] - 1, at[1])
            steps += 1
            cable1_visited[at] = steps
    elif instruction[0] is "U":
        for i in range(moves):
            at = (at[0], at[1] + 1)
            steps += 1
            cable1_visited[at] = steps

at = (0, 0)
steps = 0
for instruction in cable2.split(","):
    moves = int(instruction[1:])
    if instruction[0] is "R":
        for i in range(moves):
            at = (at[0] + 1, at[1])
            steps += 1
            cable2_visited[at] = steps
    elif instruction[0] is "D":
        for i in range(moves):
            at = (at[0], at[1] - 1)
            steps += 1
            cable2_visited[at] = steps
    elif instruction[0] is "L":
        for i in range(moves):
            at = (at[0] - 1, at[1])
            steps += 1
            cable2_visited[at] = steps
    elif instruction[0] is "U":
        for i in range(moves):
            at = (at[0], at[1] + 1)
            steps += 1
            cable2_visited[at] = steps
shortest_distance = 99999999999
for x in cable1_visited.keys():
    if x in cable2_visited.keys():
        distance = cable1_visited[x] + cable2_visited[x]
        if distance < shortest_distance:
            shortest_distance = distance

print(shortest_distance)

