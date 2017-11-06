p=[0,15,10,5,10,20] #关键字
q=[5,10,5,5,5,10] #伪关键字

n=len(p)
e=[[0 for i in range(n)] for j in range(n+1)]   #期望代价
w=[[0 for i in range(n)] for j in range(n+1)]
root=[[0 for i in range(n)] for j in range(n)]

for i in range(1,n+1):
    e[i][i-1]=q[i-1]
    w[i][i-1]=q[i-1]

for k in range(1,n+1):

    for i in range(1,n-k+1):

        j=i+k-1

        e[i][j]=10000

        w[i][j]= p[j]+q[j]+w[i][j-1]
        for r in range(i,j+1):
            t=e[i][r-1]+e[r+1][j]+w[i][j]

            if t<e[i][j]:

                e[i][j]=t

                root[i][j]=r
print(e)
print(w)
print(root)


