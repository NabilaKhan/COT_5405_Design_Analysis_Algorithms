from numpy.random import choice
import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
from time import process_time


realizations = 1000
count_size = 1000
G = nx.read_gpickle("Test_Graph/graph_0.8_40000.pickle")
nt = G.number_of_nodes()
mt = G.number_of_edges()
print("Nodes: ", nt)
print("Edges: ", mt)

dt = float(2 * mt)/ nt
degree_frequency = nx.degree_histogram(G)
expected_degree_value = []
max_degree = 18

for i in range(1,max_degree):
    temp = i * degree_frequency[i]
    temp = float(temp) / (nt - dt)
    temp = temp * (1 - float(2 * dt) / nt)
    expected_degree_value.append(temp)


####### Plot Predicted Line

plt.figure()    

x = list(range(1,len(expected_degree_value)+1))
plt.plot(x, expected_degree_value, label= 'Predicted')

count = np.zeros(count_size)
nodes = list(G.nodes)
last_node_added = nodes[len(nodes)-1] + 1


#############Count degree frequency for 1000 realizations
for r in range(0, realizations):

    if(r % 100 == 0):
        print("realization: ", r)
  
    node_list = np.arange(0, last_node_added, 1)
    probability_distribution = np.zeros(last_node_added)
    for j in range(0,last_node_added):
        if G.has_node(j):
            probability_distribution[j] = (nt - G.degree(j)) / ((nt**2)-(2*mt))

    node_to_delete = np.random.choice(a = node_list, p = probability_distribution)
    adjacent_nodes = G[node_to_delete]

    for key in adjacent_nodes:
        
        degree = G.degree(key) - 1
        if(degree >= 0):
                        
            count[degree] = count[degree] + 1 
    
total = 0
x = []
y = []
for i in range(1, max_degree+1):
    total = total + count[i]
for i in range(1, max_degree):
    x.append(i)
    y.append(count[i-1]/total)


plt.scatter(x, y, marker = 's', color = 'red', label= 'Simulated')

plt.xlabel('k')
plt.ylabel('E[$N_{k,t}^{(1)}$]')
plt.legend(loc='best')
plt.savefig('plots/degree_neighbor.png')
plt.show()





