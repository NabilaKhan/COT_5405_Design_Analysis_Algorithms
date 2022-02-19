import networkx as nx
import random
import numpy as np
from time import process_time
import matplotlib.pyplot as plt


probability = [0.6, 0.75, 0.9]
x = [20000, 40000, 60000, 80000, 100000]
t = 100001
total_runtime = [189.42080845400002, 757.219362833, 1765.648732376, 3230.996875098, 4983.554779142, 436.87102721, 1783.002776774, 3839.50269522, 7005.673817082, 10918.518818543,
            602.728871668, 2422.6160247459998, 5610.313284701, 9986.255446638, 15602.248412972]


markers = ['^', 's', 'd']
colors = ['magenta', 'green', 'blue']
sign_index = 0
start_runtime_index = 0

for p in probability:

    total_node_list = []
    total_edge_list = []
    run_time = []

    for t in x:

        print(p," of ", t)

        G = nx.read_gpickle("Test_Graph/graph_"+str(p)+"_"+str(t)+".pickle")
        total_node_list.append(G.number_of_nodes())
        total_edge_list.append(G.number_of_edges())
        run_time.append(total_runtime[start_runtime_index]/60)
        start_runtime_index += 1

            
    G.clear()
    q = 1 - p

    ######### Plotting Nodes
    plt.figure(1)
    plt.scatter(x, total_node_list, marker = markers[sign_index], label= str(p))
    expected_val_node = []
    for val in x:
        expected_val_node.append((p - q)*val + 2 * q)
    plt.plot(x, expected_val_node)

    ######### Plotting Edges
    plt.figure(2)
    plt.scatter(x, total_edge_list, color = colors[sign_index], marker=markers[sign_index], label= str(p))
    expected_val_edge = []
    for val in x:
        expected_val_edge.append(p * (p - q) * val)
    plt.plot(x, expected_val_edge, color = colors[sign_index])

    ######### Plotting Runtime
    plt.figure(3)
    plt.plot(x, run_time, color = colors[sign_index],label= str(p))

    sign_index += 1    
                 
n = G.number_of_nodes()
m = G.number_of_edges()

print("Nodes: ", n)
print("Edges: ", m)

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
plt.ylabel('run-time in minutes')
plt.legend(loc='best')
plt.savefig('plots/runtime.png')


plt.show()


