import random
import numpy as np
import csv
import networkx as nx

obj=csv.reader(open('data.csv','r'))
l=[] #nodelist
e=[] #edgelist
next(obj) 
G=nx.DiGraph() #directed graph
for row in obj:
    b=row[1][0:11].upper() 
    l.append(b) #appending nodes to nodelist
    for i in row[2:]:
        e.append((b,i[-11:].upper())) #appending edges to edgelist
G.add_nodes_from(l) #adding nodes to graph
G.add_edges_from(e) #adding edges to graph

adj_matrix=nx.to_numpy_array(G,nodelist=sorted(G.nodes())) #adjacency matrix
L=list(G.nodes()) #list of nodes
w=len(L) #number of nodes
missing_links=[]
def change_values(G,adj_matrix):
    for i in range(w):
        for j in range(w):
            if adj_matrix[i][j]==0:
                adj_matrix_copy=adj_matrix.copy()
                f = adj_matrix_copy[:,j]
                f = np.delete(f,i,axis=0) #delete the ith element of f
                adj_matrix_copy=np.delete(adj_matrix_copy,j,axis=1) #delete the jth column of the adjacency matrix
                b=[] #list to store values of the ith row of the adjacency matrix except the jth column
                for k in range(w-1):
                    b.append(adj_matrix_copy[i][k])
                adj_matrix_copy=np.delete(adj_matrix_copy,i,axis=0) #delete the ith row of the adjacency matrix
                adj_matrix_copy_t=adj_matrix_copy.transpose()
                b_t=np.array(b).transpose()
                x_t, residuals, rank, singular_values = np.linalg.lstsq(adj_matrix_copy_t, b_t, rcond=None)
                x=x_t.transpose()
                if abs(np.matmul(x,f))>1:
                    missing_links.append((L[i],L[j]))
                    G.add_edge(L[i],L[j])
                    adj_matrix[i][j]=1
    print("The missing links added to the network are: ",missing_links)
    return G    
change_values(G,adj_matrix)
network_density=len(e)/(w*(w-1)) # network_density=0.194
changed_network_density=(len(e)+len(missing_links))/(w*(w-1)) # changed_network_density=0.263
print("Number of missing links added to the network: ",len(missing_links))
print(network_density,changed_network_density)

