class MapColoring:
    def __init__(self, graph):
        self.graph = graph
        self.colors = {}

    def is_valid(self, node, color):
        for neighbor in self.graph[node]:
            if neighbor in self.colors and self.colors[neighbor] == color:
                return False
        return True

    def color_map(self, node, num_colors):
        if node not in self.graph:
            return True

        for color in range(num_colors):
            if self.is_valid(node, color):
                self.colors[node] = color
                if self.color_map(next(iter(set(self.graph.keys()) - set(self.colors.keys()))), num_colors):
                    return True
                del self.colors[node]

        return False

    def solve(self, num_colors):
        start_node = next(iter(self.graph))
        if self.color_map(start_node, num_colors):
            return self.colors
        return None


# Define the graph representing the map (regions and their adjacent regions)
graph = {
    'WA': {'NT', 'SA'},
    'NT': {'WA', 'SA', 'Q'},
    'SA': {'WA', 'NT', 'Q', 'NSW', 'V'},
    'Q': {'NT', 'SA', 'NSW'},
    'NSW': {'Q', 'SA', 'V'},
    'V': {'SA', 'NSW'}
}

# Initialize MapColoring with the graph
map_coloring = MapColoring(graph)

# Solve the map coloring problem with 3 colors
num_colors = 3
solution = map_coloring.solve(num_colors)

if solution:
    print("Map coloring solution:")
    for region, color in solution.items():
        print(f"{region}: Color {color}")
else:
    print("No solution found.")
