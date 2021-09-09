
data = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0]
]

node = ["(0)", "(1)", "(2)", "(3)", "(4)"]

for y in range(5):
    for x in range(y, 5):
        if data[y][x] == 1 and data[x][y] == 1:
            print(node[y], "<->", node[x])


directed_graph_data = [
    [0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 1, 1, 0]
]

arrow = ["", "-->", "<--", "<->"]

print("\n---Directed Graph---")

for y in range(5):
    for x in range(y, 5):
        edge_1 = directed_graph_data[y][x]
        edge_2 = directed_graph_data[x][y]
        arrow_num  = edge_1 + edge_2 * 2

        if arrow_num > 0:
            print(node[y], arrow[arrow_num], node[x])