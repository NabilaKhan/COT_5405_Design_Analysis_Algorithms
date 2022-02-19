import networkx as nx
import random
import numpy as np
from time import process_time
import matplotlib.pyplot as plt


t1 = process_time()
probability = [0.75]
x = [100, 200, 300, 400, 500]
t = 501

G = nx.Graph()
G.add_node(0)
G.add_node(1)
G.add_edge(0, 1)

node_to_be_added = 1
markers = ['^', 's', 'd']
colors = ['magenta', 'red', 'blue']
sign_index = 0

highest_possible_degree = 150

probability_j = 0.0
edge_probability_j = 0.0

for p in probability:
    print(p)
    total_node_list = []
    total_edge_list = []
    run_time = []
    for i in range(1,t):

        nt = G.number_of_nodes()
        mt = G.number_of_edges()

        ###Case Handling 1: When all nodes get deleted, again create the graph
        if(nt == 0):
            G.add_node(0)
            G.add_node(1)
            G.add_edge(0, 1)
            nt = 2
            mt = 1
            
        ###Case Handling 2: When all edges get deleted, create an edge between first two nodes of the graph
        elif(mt == 0):
            if(nt == 1):     #If graph contains only one node, create another node
                node_to_be_added += 1
                G.add_node(node_to_be_added)
                nt = 2
            nd = list(G.nodes)
            G.add_edge(nd[0], nd[1])
            mt = 1

        rand = random.uniform(0, 1)
        
        if(rand <= p):
        
            node_to_be_added += 1
            node_list = np.arange(0, node_to_be_added, 1)
            probability_distribution = np.zeros(node_to_be_added)

            for j in range(0,node_to_be_added):
                if G.has_node(j):
                    probability_distribution[j] = (G.degree(j)) / (2*mt)

            node_to_add_edge = np.random.choice(a = node_list, p = probability_distribution)
        
            G.add_node(node_to_be_added)
            G.add_edge(node_to_be_added, node_to_add_edge)
            
        elif(rand > p):

            node_list = np.arange(0, node_to_be_added+1, 1)
            probability_distribution = np.zeros(node_to_be_added+1)
            for j in range(0,node_to_be_added+1):
                if G.has_node(j):
                    #probability_distribution[j] = (nt - G.degree(j)) / ((nt**2)-(2*mt))  #####Equation 2 (Used in the paper)
                    probability_distribution[j] = (highest_possible_degree - G.degree(j)) / ((highest_possible_degree * nt) - (2 * mt)) #Equation 5 (Proposed Equation)
           
            node_to_delete = np.random.choice(a = node_list, p = probability_distribution)
          
            G.remove_node(node_to_delete)        

        if(i % 100 == 0):
            total_node_list.append(G.number_of_nodes())
            total_edge_list.append(G.number_of_edges())
            
    G.clear()
    q = 1 - p

    ######### Plotting Nodes
    plt.subplot(2,1,1)
    plt.scatter(x, total_node_list, marker = markers[sign_index], label ="Simulated")
    expected_val_node = []
    for val in x:
        expected_val_node.append((p - q)*val + 2 * q)
    plt.plot(x, expected_val_node, label ="Predicted")
    plt.legend(loc='best')
    plt.ylabel('E[$n_t$]')
    
    ######### Plotting Edges
    plt.subplot(2,1,2)
    plt.scatter(x, total_edge_list, color = colors[sign_index], marker=markers[sign_index], label ="Simulated")
    expected_val_edge = []
    for val in x:
        expected_val_edge.append(p * (p - q) * val)
    plt.plot(x, expected_val_edge, color = colors[sign_index], label ="Predicted")
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.ylabel('E[$m_t$]')
   
                 
plt.xlabel('t')
plt.ylabel('E[$n_t$]')
plt.legend(loc='best')
plt.savefig('plots/model.subplot2.png')


plt.show()


