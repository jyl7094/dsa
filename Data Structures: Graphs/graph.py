class Graph:
    def __init__(self):
        self.number_of_vertices = 0
        self.adjacent_list = {}
    
    def add_vertex(self, v):
        if v in self.adjacent_list:
            return False
        self.adjacent_list[v] = []
        self.number_of_vertices += 1
        return True
    
    def add_edge(self, v1, v2):
        if v1 not in self.adjacent_list or v2 not in self.adjacent_list:
            return False
        self.adjacent_list[v1].append(v2)
        self.adjacent_list[v2].append(v1)
        return True

    def show_connections(self):
        for key in self.adjacent_list:
            if self.adjacent_list[key]:
                print(f'{str(key)} --> {", ".join(map(str, self.adjacent_list[key]))}')
            else:
                print(f'{str(key)} --> None')
