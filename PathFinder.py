''' reads the data from mit_map.txt file and finds the shortest route from 
    one building to another (start to destination) on the MIT campus
    given the user input  constrains on the total distance and outdoor distance
    
'''

import os
import sys
from Edge import Node,Edge
from Graph import Diagraph

def load_data(filename):   
    #returns a list of line-splited data from the text file
    #each line in text file includes:
    # [src_name,des_name,total_length,outdoor_length](e.g.[32 36 70 0])
    with open(os.path.join(sys.path[0],filename), mode='r') as file:    
        mit_map = []
        for line in file:
            mit_map.append(line.split())
        file.close()    
    return mit_map


def generate_graph(filename, graph_class):
    #returns graph class obj generated using text file data 
    map_data = load_data(filename)
    map_graph = graph_class()  

    for data in map_data:        
        src_name, dest_name = data[0], data[1]
        src,dest=Node(src_name),Node(dest_name)
        edge=Edge(src,dest,int(data[2]),int(data[3]))        
        if not map_graph.node_in(src):
            map_graph.add_source(src)
        map_graph.add_edge(edge)

    return map_graph

def path_len_finder(graph, path, length=0):
    #returns total length of a given path (which is a list of Node class obj)
    if len(path) <= 1:
        return length
    else:        
        edge=graph.get_edge(path[0],path[1])
        length=length+edge.get_total_len()
        return path_len_finder(graph, path[1:], length)


def weightedDFS(graph,start,destination,total,outdoor,path=[],shortest=None):
    #returns the shortest path between start and end node
    # that meets the total and max_outdoor length if exists 
    #it applies deapth-first search algorithm
    path=path+[start]    
    if start==destination:
        return path    
    for edge in graph.get_edge_list(start):
        node=edge.get_dest()        
        if node not in path: # to avoid loop
            #check if the total length and outdoor length for given path are valid 
            availTotal,availOutdoor=total-edge.get_total_len(),\
                                    outdoor-edge.get_outdoor_len()            
            if availTotal>=0 and availOutdoor>=0:                
                newPath=weightedDFS(graph,node,destination,availTotal
                ,availOutdoor,path,shortest)
                #update the shortest path, if found any
                if shortest==None or path_len_finder(graph,newPath)<path_len_finder(graph,shortest):
                    shortest=newPath                  
                    if shortest!=None:
                        nodeList=[n.get_name() for n in shortest]
                        #print(nodeList)                  
    return shortest


def print_graph(graph):
    graphDict={}
    for k in graph.graph:
        graphDict[k.get_name()]=[]
        for edge in graph.graph[k]:
            graphDict[k.get_name()].append(edge.get_dest().get_name())
        print(k,graphDict[k.get_name()])


if (__name__)=="__main__":
    graph=generate_graph("mit_map.txt",Diagraph)

    print("all available building connections: ")
    print_graph(graph)
    print("------------------------------------------")
    print("to see available building number please refer to the data above")

    print()
    start_name=input("please enter the strat building No: ")
    dest_name=input("please enter the destination building No:")
    max_distance=int(input("please enter max distance (m): "))
    max_outdoor=int(input("please enter max outdoor distance (m): "))
    print()

    start=Node(start_name)
    dest=Node(dest_name)
    print("------Calculating the shortest path------")    
    shortest=weightedDFS(graph,start,dest,max_distance,max_outdoor)
    result=""
    if shortest!=None:
        for node in shortest:
            result+=node.get_name()+"->"
        print(f"shortest path from {start_name} to {dest_name}: ",result[:-2])
    else:
        print("no path found")