from stackwithlist import mystack


def dfa(node, adjlist,sourse_node):
    l = len(node)
    status = [1] * l
    nodestack = mystack()
    nodestack.push(sourse_node)
    nodelist=[]
    while not nodestack.isEmpty():
        N = nodestack.pop()
        nodelist.append(N)
        status[node[N]] = 3
        for j in adjlist[N]:
            if status[node[j]]==1:
                nodestack.push(j)
                status[node[j]]=2
    return nodelist

nodes = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6,'J':7, 'K':8}
adjlist={'A':'BCF', 'B':'CG', 'C':'F', 'D':'C', 'E':'CDJ', 'F':'D', 'G':'CE','J':'DK', 'K':'EG'}
print(dfa(nodes,adjlist,"J"))