import networkx as nx
import random
import numpy as np
from time import process_time
import matplotlib.pyplot as plt

t1 = process_time()
probability = [0.1, 0.25, 0.4] #Instead of 0.9, 0.75, 0.6
x = [200, 400, 600, 800, 1000]
t = 1001

path = "Output_graph/"
node_to_be_added = 88234
markers = ['^', 's', 'd']
colors = ['magenta', 'red', 'blue']
sign_index = 0
birth = 0
death = 0


probability_j = 0.0
edge_probability_j = 0.0

for p in probability:
    print(p)
    G = nx.read_gpickle("Generated_graph/graph_88234.pickle")
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
            birth += 1
            node_to_be_added += 1
            node_list = np.arange(0, node_to_be_added, 1)
            probability_distribution = np.zeros(node_to_be_added)
            
            for j in range(0,node_to_be_added):
                if G.has_node(j):
                    probability_distribution[j] = G.degree(j) / (2*mt)

            node_to_add_edge = np.random.choice(a = node_list, p = probability_distribution)
        
            G.add_node(node_to_be_added)
            G.add_edge(node_to_be_added, node_to_add_edge)
            
        elif(rand > p):
            death += 1
            node_list = np.arange(0, node_to_be_added+1, 1)
            probability_distribution = np.zeros(node_to_be_added+1)
            for j in range(0,node_to_be_added+1):
                if G.has_node(j):
                    probability_distribution[j] = (nt - G.degree(j)) / ((nt**2)-(2*mt))

            node_to_delete = np.random.choice(a = node_list, p = probability_distribution)
          
            G.remove_node(node_to_delete)        

        if(i % 200 == 0):
            nx.write_gpickle(G, path + "graph_"+str(p)+"_"+str(i)+".pickle")
            total_node_list.append(G.number_of_nodes())
            total_edge_list.append(G.number_of_edges())
            run_time.append(process_time() - t1)
            
    G.clear()
    q = 1 - p

    ######### Plotting Nodes
    plt.figure(1)
    plt.scatter(x, total_node_list, marker = markers[sign_index], label = str(p))
    plt.plot(x, total_node_list)

    ######### Plotting Edges
    plt.figure(2)
    plt.scatter(x, total_edge_list, color = colors[sign_index], marker=markers[sign_index], label = str(p))
    plt.plot(x, total_edge_list, color = colors[sign_index])

    ######### Plotting Runtime
    plt.figure(3)
    plt.plot(x, run_time, color = colors[sign_index], label = str(p))

    sign_index += 1    
                 

plt.figure(1)
plt.xlabel('t')
plt.ylabel('E[$n_t$]')
plt.legend(loc='best')
plt.savefig('plots/nodes.png')

plt.figure(2)
plt.xlabel('t')
plt.ylabel('E[$m_t$]')
plt.legend(loc='best')
plt.savefig('plots/edges.png')

plt.figure(3)
plt.xlabel('t')
plt.ylabel('run-time')
plt.legend(loc='best')
plt.savefig('plots/runtime.png')

plt.show()


