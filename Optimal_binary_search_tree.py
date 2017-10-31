p=[0,0.15,0.10,0.05,0.10,0.20] #关键字
q=[0.05,0.10,0.05,0.05,0.05,0.10] #伪关键字
n=len(p)
e=[[0 for i in range(n)] for j in range(n+1)]   #期望代价
w=[[0 for i in range(n)] for j in range(n+1)]
root=[[0 for i in range(n)] for j in range(n)]
for i in range(1,n+1):
    e[i][i-1]=q[i-1]
    w[i][i-1]=q[i-1]
for l in range(1,n+1):
    for i in range(1,n-l+1):
        j=i+l-1
        e[i][j]=1000
        w[i][j]= w[i][j-1]+p[j]+q[j]
        for r in range(i,j):
            t=e[i][r-1]+e[r+1][j]+w[i][j]
            if t<e[i][j]:
                e[i][j]=t
                root[i][j]=r
print(e)

