from numpy.random import choice
import networkx as nx
import random
import numpy as np
import math
import matplotlib.pyplot as plt
from time import process_time
from decimal import Decimal

G = nx.read_gpickle("Test_Graph/graph_0.8_100000.pickle")
nt = G.number_of_nodes()
mt = G.number_of_edges()

print("Nodes: ", nt)
print("Edges: ", mt)
p = 0.8

degree_frequency = nx.degree_histogram(G)
expected_degree_value = []
x = []
max_degree = 42

####### Plot Predicted Line
temp = 0.0
x = list(range(1,max_degree+1))

for i in range(1,max_degree+1):
    temp = -1 - (2*p/((2*p)-1))
    temp = i**temp
    expected_degree_value.append(temp)


for i in range(max_degree - 2, -1, -1):
    expected_degree_value[i] = expected_degree_value[i] + expected_degree_value[i+1]


plt.figure()    
plt.plot(x, expected_degree_value, label = 'Predicted')
plt.xscale('log')
plt.yscale('log')


####### Plot Simulated Line


total = 0
for i in range(max_degree, 0, -1):
    total = total + degree_frequency[i]


temp = np.zeros(max_degree+1)
temp[max_degree] = degree_frequency[max_degree]
for i in range(max_degree - 1, 0, -1):

   temp[i] = degree_frequency[i]+ temp[i+1]


y = []  
for i in range(1, max_degree+1):
   
    y.append(temp[i] / total)
    

x = list(range(1,max_degree+1))
plt.scatter(x, y, color = 'red', marker = 's', label = 'Simulated')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('k')
plt.ylabel('P\'(k)')
plt.legend(loc='best')
plt.savefig('plots/degree_distribution.png')
plt.show()
    
    



