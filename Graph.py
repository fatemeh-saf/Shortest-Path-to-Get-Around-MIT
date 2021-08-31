# class that represents weighted graph as a dictionary.
#Graph dict key is Node(src) and value is list of Edge obj with that src 
# Node(src):[Edge(src,dest1,wt,wi),Edge(src,dest2,wt,wi)] 

class Diagraph(object):
    def __init__(self):
        # graph={src1:[e1,e2...],src2:[e1,..],...}
        self.graph = {}
        # list of all edges exists in the graph
        self.edges = []

    def add_source(self, node):
        if node in self.graph:
            raise ValueError("duplicate key")            
        else:
            self.graph[node] = []    
    
    def get_node(self, node):
        for grNode in self.graph:
            if grNode==node:
                return grNode
        raise NameError       

    def node_in(self, node):
        for n in self.graph:
            if n==node:
                return True
        return False

    def add_edge(self,edge):
        src = edge.get_src()        
        if not (self.node_in(src)):
            raise KeyError("src not in graph")        
        self.graph[src].append(edge)
        self.edges.append(edge)        

    def get_edge_list(self, src):
        #returns list of edges for the src node
        for node in self.graph:
            if self.get_node(src):
                return self.graph[src]
    
    def get_edge(self,src,dest):
        for edge in self.edges:
            if edge.get_src()==src and edge.get_dest()==dest:
                return edge
        return ValueError

