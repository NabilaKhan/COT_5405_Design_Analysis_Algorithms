from numpy.random import choice
import networkx as nx
import random
import numpy as np
import math
import matplotlib.pyplot as plt
from time import process_time
from decimal import Decimal

size = 100000
break_point = 30000
degree_bound = 500
G = nx.read_gpickle("Data/graph_0.9_100000.pickle")
nt = G.number_of_nodes()
mt = G.number_of_edges()

print("Nodes: ", nt)
print("Edges: ", mt)
p = 0.8

degree_frequency = nx.degree_histogram(G)
expected_degree_value = []
x = []
max_degree = 42

node_count = 0
last_old_node = 0
old_node_frequency = np.zeros(degree_bound)
for old_node in range(0,size):
    if G.has_node(old_node):
       node_count += 1
       old_node_frequency[G.degree(old_node)] += 1
    if node_count == break_point:
        last_old_node = old_node
        break

new_node_frequency = np.zeros(degree_bound)
for new_node in range(last_old_node+1,size):
    if G.has_node(new_node):
       node_count += 1
       new_node_frequency[G.degree(new_node)] += 1
    if node_count == nt:
        break

####### Plot Predicted Line
temp = 0.0
x = list(range(1,max_degree+1))

for i in range(1,max_degree+1):
    temp = -1 - (1.15*p/((2*p)-1))
    temp = i**temp
    expected_degree_value.append(temp)


for i in range(max_degree - 2, -1, -1):
    expected_degree_value[i] = expected_degree_value[i] + expected_degree_value[i+1]


plt.figure(1)    
plt.plot(x, expected_degree_value, label = 'Predicted')
plt.xscale('log')
plt.yscale('log')


####### Plot Simulated Line for Old Nodes


total = 0
for i in range(max_degree, 0, -1):
    total = total + old_node_frequency[i]


temp = np.zeros(max_degree+1)
temp[max_degree] = old_node_frequency[max_degree]
for i in range(max_degree - 1, 0, -1):

   temp[i] = old_node_frequency[i]+ temp[i+1]


y = []  
for i in range(1, max_degree+1):
   
    y.append(temp[i] / total)
    

x = list(range(1,max_degree+1))
plt.scatter(x, y, color = 'red', marker = 's', label = 'Old Nodes')


####### Plot Simulated Line for New Nodes

total = 0
for i in range(max_degree, 0, -1):
    total = total + new_node_frequency[i]


temp = np.zeros(max_degree+1)
temp[max_degree] = new_node_frequency[max_degree]
for i in range(max_degree - 1, 0, -1):

   temp[i] = old_node_frequency[i]+ temp[i+1]


y = []  
for i in range(1, max_degree+1):
   
    y.append(temp[i] / total)
    

x = list(range(1,max_degree+1))
plt.scatter(x, y, color = 'green', marker = 's', label = 'New Nodes')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('k')
plt.ylabel('P\'(k)')
plt.legend(loc='best')
plt.savefig('plots/degree_distribution1.png')



####### Plot Simulated Cumulative Probability Comparison

for i in range(0,degree_bound):
    new_node_frequency[i] = new_node_frequency[i] / nt
    old_node_frequency[i] = old_node_frequency[i] / nt

for i in range(degree_bound-2,-1, -1):
    new_node_frequency[i] = new_node_frequency[i] + new_node_frequency[i+1]
    old_node_frequency[i] = old_node_frequency[i] + old_node_frequency[i+1]

x = list(range(1,max_degree+1))
y1 = []
y2 = []
for i in range(1, max_degree+1):   
    y1.append(old_node_frequency[i])
    y2.append(new_node_frequency[i])

plt.figure(2)    
plt.scatter(x, y1, color = 'red', marker = 's', label = 'Old Nodes')
plt.plot(x, y1, color = 'red', marker = 's')
plt.scatter(x, y2, color = 'green', marker = 's', label = 'New Nodes')
plt.plot(x, y2, color = 'green', marker = 's')
plt.xlabel('k')
plt.ylabel('P\'(k)')
plt.legend(loc='best')
plt.savefig('plots/degree_distribution2.png')
plt.show()
    
    



