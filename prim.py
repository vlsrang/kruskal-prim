import sys
N=7
s=0
g=[None for x in range(N)]
g[0]=[(1,9),(2,10)]
g[1]=[(0,9),(3,10),(4,5),(6,3)]
g[2]=[(0,10),(3,9),(4,7),(5,2)]
g[3]=[(1,10),(2,9),(5,4),(6,8)]
g[4]=[(1,5),(2,7),(6,1)]
g[5]=[(2,2),(3,4),(6,6)]
g[6]=[(1,3),(3,8),(4,1),(5,6)]

visited=[False for x in range(N)]
dist=[sys.maxsize for x in range(N)]
dist[s]=0
previous=[None for x in range(N)]
previous[s]=s

for v in range(N):
    u=-1
    mindist=sys.maxsize
    for i in range(N):
        if not visited[i] and dist[i]<mindist:
            mindist=dist[i]
            u=i
    visited[u]=True
    for w,wt in g[u]:
        if not visited[w]:
            if wt<dist[w]:
                dist[w]=wt
                previous[w]=u

print('최소신장트리: ',end='')
mst_cost=0
for i in range(1,N):
    print('(%d,%d)'%(i,previous[i]),end='')
    mst_cost+=dist[i]
print('\n최소신장트리 가중치: ',mst_cost)
