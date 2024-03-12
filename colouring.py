V = 4
graph = [[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]]

def is_valid(v, color, c):
    for i in range(V):
        if graph[v][i] == 1 and c == color[i]:
            return False
    return True

def m_coloring(colors, color, vertex):
    if vertex == V:
        return True
    for col in range(1, colors + 1):
        if is_valid(vertex, color, col):
            color[vertex] = col
            if m_coloring(colors, color, vertex + 1):
                return True
            color[vertex] = 0
    return False

colors = 3
color = [0] * V

if not m_coloring(colors, color, 0):
    print("Solution does not exist.")
else:
    print("Assigned Colors are:")
    for i in range(V):
        print(color[i], end=" ")
