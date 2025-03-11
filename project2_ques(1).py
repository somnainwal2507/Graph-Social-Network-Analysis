import random
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

def random_walk(G):
    node=G.nodes() 
    coins={} #dictionary to store coins
    for i in node:
        coins[i]=0 
    n=random.choice(list(node)) #randomly choosing a node
    coins[n]+=1
    x=G.out_edges(n) #outgoing edges of node
    c=0
    while c<500000:
        if len(x)==0:
            m=random.choice(list(node))
        else:
            a=random.uniform(0,1)
            if a<0.85:
                n1=random.choice(list(x))
                m=n1[1]
            else:
                m=random.choice(list(node))

        coins[m]+=1 #incrementing coins of next node   
        x=G.out_edges(m) 
        c+=1 
    return coins 
sorted_by_values = sorted(random_walk(G).items(), key=lambda item: item[1]) #sorting coins dictionary
sorted_dict = {key: value for key, value in sorted_by_values} 
f=list(sorted_dict.keys())
g=list(sorted_dict.values())
def top_ten(sorted_dict): #function to print top 10 students according to pagerank
    for i in range(-1,-12,-1):
        if f[i]!='':
            print(f[i])
print("The top ten (most influential) students according to random walk algorithm are")
top_ten(sorted_dict)
print("The top leader according to random walk algorithm is : ", f[-2]) 