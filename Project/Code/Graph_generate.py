import networkx as nx
from time import process_time 

f=open("Data/facebook_combined.txt", "r")
path = 'Generated_graph/'

G = nx.Graph()
line_number = 0

for i in range(0,4039):
    G.add_node(i)  

while(True):
    
    line = f.readline()
    if(line == ''):
        break
    line = line.split()
    G.add_edge(int(line[0]), int(line[1]))
    
    if(line_number % 10000 == 0):
        nx.write_gpickle(G, path + "graph_"+str(line_number)+".pickle")
    line_number += 1


nx.write_gpickle(G, path + "graph_"+str(line_number)+".pickle")
G.clear()
f.close()


