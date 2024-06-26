# checks if assigning a color to a node 
def is_safe(node, color, graph, colors):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True
# checks if all nodes in a graph have been colored
def color_graph(node, graph, colors, available_colors):
    if node == len(graph):
        return True
    
    for color in available_colors:
        if is_safe(node, color, graph, colors):
            colors[node] = color
            if color_graph(node+1, graph, colors, available_colors):
                return True
            colors[node] = None
    
    return False

#This function attempts to color a graph using the provided available colors
def map_coloring(graph, available_colors):
    num_nodes = len(graph)
    colors = [None] * num_nodes

    if color_graph(0, graph, colors, available_colors):
        print("The graph can be colored using the following colors:")
        for node, color in enumerate(colors):
            print("Node", node, ":", color)
    else:
        print("The graph cannot be colored using the provided colors.")

# Example graph represented as a dictionary of lists
graph = {
    0: [1, 2, 3],
    1: [0, 2],
    2: [0, 1, 3],
    3: [0, 2]
}

available_colors = ["Red", "Green", "pink", "Yellow"]

map_coloring(graph, available_colors)