def solution(n, costs):
    costs.sort(key = lambda x : x[2])
    
    mst = []
    p = [0]
    tree_edges = 0
    mst_c = 0 
    
    def find(u):
        if u != p[u]:
            p[u] = find(p[u])
        return p[u]
    def union(u,v):
        root1 = find(u)
        root2 = find(v)
        p[root2] = root1
    
    for i in range(1,n+1):
        p.append(i)
        
    while True:
        if tree_edges == n-1:
            break
        u,v,wt = costs.pop(0)
        if find(u) != find(v):
            union(u,v)
            mst.append((u,v))
            mst_c += wt
            tree_edges += 1
    return mst_c
