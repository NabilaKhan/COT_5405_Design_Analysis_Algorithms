import networkx as nx
import random
import numpy as np
from time import process_time
import matplotlib.pyplot as plt

node_probability = 0.8
edge_probability = 0.8
probability = 0.8

x = [2000, 4000, 6000, 8000, 10000]
t = 10001

path = "Output_graph/"

G = nx.Graph()
G.add_node(0)
G.add_node(1)
G.add_edge(0, 1)

node_to_be_added = 1
markers = ['^', 's', 'd']
colors = ['magenta', 'red', 'blue']
sign_index = 0

probability_j = 0.0
edge_probability_j = 0.0

total_node_list = []
total_edge_list = []

for iteration in range(1,t):
    
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

    rand = random.uniform(0, 1) #Selects if it will handle node or edge in the current iteration

    if(rand <= probability): #Will handle node 
        
        rand2 = random.uniform(0, 1)
        
        if(rand2 <= node_probability): #Birth of node
                 
            node_to_be_added += 1
            node_list = np.arange(0, node_to_be_added, 1)
            probability_distribution = np.zeros(node_to_be_added)

            for j in range(0,node_to_be_added):
                if G.has_node(j):
                    probability_distribution[j] = G.degree(j) / (2*mt)

            node_to_add_edge = np.random.choice(a = node_list, p = probability_distribution)
            G.add_node(node_to_be_added)
            G.add_edge(node_to_be_added, node_to_add_edge)


        elif(rand2 > node_probability): #Death of node
          
            node_list = np.arange(0, node_to_be_added+1, 1)
            probability_distribution = np.zeros(node_to_be_added+1)
            for j in range(0,node_to_be_added+1):
                if G.has_node(j):
                    probability_distribution[j] = (nt - G.degree(j)) / ((nt**2)-(2*mt))

            node_to_delete = np.random.choice(a = node_list, p = probability_distribution)
            G.remove_node(node_to_delete)        

            
    elif(rand > probability):  #Will handle edge
        
        rand3 = random.uniform(0, 1)
        nodes = list(G.nodes)
        random_node = random.choice(nodes)
        adjacent_nodes = G[random_node]
        nodes.remove(random_node)
        
        
        if(rand3 <= edge_probability): #Birth of Edge
           
            adjacent_count = np.zeros(node_to_be_added+1)
            node_list = np.arange(0, node_to_be_added+1, 1)

            for key in adjacent_nodes:
                secondary_adjacent_nodes = G[key]

                for key2 in secondary_adjacent_nodes:
                    if key2 not in adjacent_nodes and key2 != random_node:
                        adjacent_count[key2] += 1
                
            total_count = sum(adjacent_count)

            if(total_count != 0):
                for i in range(0,node_to_be_added+1):
                    adjacent_count[i] = adjacent_count[i] / total_count
            
            if(sum(adjacent_count) == 1):
                node_to_add_edge = np.random.choice(a = node_list, p = adjacent_count)
                
            else:
                node_to_add_edge = random.choice(nodes)
                
            G.add_edge(random_node,node_to_add_edge)
            
            
        elif(rand3 > edge_probability): #Death of Edge

            adjacent_count = []
            node_list = []
            for key in adjacent_nodes:

                common_adjacent_nodes = sorted(nx.common_neighbors(G, random_node, key))
                if key in common_adjacent_nodes:
                    common_adjacent_nodes.remove(key)
                if random_node in common_adjacent_nodes:
                    common_adjacent_nodes.remove(random_node)

                node_list.append(key)
                adjacent_count.append(nt - len(common_adjacent_nodes))

            total_count = sum(adjacent_count)

            if(total_count != 0):
                for k in range(0, len(adjacent_count)):
                    adjacent_count[k] = adjacent_count[k] / total_count
                node_to_delete_edge = np.random.choice(a = node_list, p = adjacent_count)
                G.remove_edge(random_node, node_to_delete_edge)


    if(iteration % 2000 == 0):
        print(iteration)
        total_node_list.append(G.number_of_nodes())
        total_edge_list.append(G.number_of_edges())
        
G.clear()

q_node_probability = 1 - node_probability
q_edge_probability = 1 - edge_probability
q_probability = 1 - probability

######### Plotting Nodes
plt.figure(1)
plt.scatter(x, total_node_list, marker = markers[sign_index], color = 'orange', label = "Simulated Line")
expected_val_node = []
expected_val_node2 = []
for val in x:
    expected_val_node.append((node_probability - q_node_probability)*val + 2 * q_node_probability)
    expected_val_node2.append(probability * (q_probability+1) * (node_probability/2) * ((edge_probability - q_edge_probability)+(node_probability - q_node_probability)) * val + 1 * (q_node_probability))
plt.plot(x, expected_val_node, color = 'green', label = "Previously Predicted")
plt.plot(x, expected_val_node2, color = 'orange', label = "Updated Predicted")

######### Plotting Edges
plt.figure(2)
plt.scatter(x, total_edge_list, marker=markers[sign_index], color = 'orange', label = "Simulated Line")
expected_val_edge = []
expected_val_edge2 = []
for val in x:
    #expected_val_edge.append(q_probability * (edge_probability) * (edge_probability - q_edge_probability) * val)
    expected_val_edge2.append(probability * (q_probability+1) * (edge_probability) * 0.5 *((node_probability - q_node_probability)+(edge_probability - q_edge_probability)) * val)
    #expected_val_edge.append(probability * (q_probability+1) * (node_probability+edge_probability) *(edge_probability - q_edge_probability) * val)
    #expected_val_edge.append(17 * q_probability * (edge_probability) * (edge_probability - q_edge_probability) * val)
    expected_val_edge.append(node_probability * (node_probability - q_node_probability) * val)
plt.plot(x, expected_val_edge, color = 'green', label = "Previously Predicted")
plt.plot(x, expected_val_edge2, color = 'orange', label = "Updated Predicted")

sign_index += 1    
                 
plt.figure(1)
plt.xlabel('t')
plt.ylabel('E[$n_t$]')
plt.legend(loc='best')
plt.savefig('plots/Preferential_nodes.png')

plt.figure(2)
plt.xlabel('t')
plt.ylabel('E[$m_t$]')
plt.legend(loc='best')
plt.savefig('plots/Preferential_edges.png')

plt.show()

