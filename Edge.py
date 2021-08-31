# Node and Edge class used to generate Graph
class Node(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def __eq__(self, other):
        return other !=None and self.name==other.get_name()

    def __hash__(self): 
        return self.name.__hash__()
    
    def __str__(self):
        return self.name


class Edge(object):
    #each edge (==connection between building A and building B) has two lengths: 
    #total length=indoor length+outdoor length
    #outdoor length=length outside the building
    def __init__(self, source, destination, total_length=None,outdoor_length=None):
        self.src = source
        self.dest = destination        
        self.wt = total_length
        self.wo = outdoor_length

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest

    def get_total_len(self):
        return self.wt

    def get_outdoor_len(self):
        return self.wo
        
    def __eq__(self,other):
        #assumes there's only one edge between src and dest:
        if other !=None and self.src==other.get_src() and\
            self.dest==other.get_dest()  :          
            return True
        return False

    def __hash__(self):
        return hash(self.src,self.dest)    
    
    def __str__(self):
        return 'Source: '+str(self.get_src()) +\
            ', Destination: '+str(self.get_dest())