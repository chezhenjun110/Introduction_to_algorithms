p=[0,0.15,0.10,0.05,0.10,0.20] #关键字
q=[0.05,0.10,0.05,0.05,0.05,0.10] #伪关键字
e=[]
w=[]
root=[]
n=len(p)
for i in range(1,n+1):
    for j in range(n):
        e[i][j]=0
        w[i][j]=0
print(len(e))
# for i in range(1,n+1):

    # e[i][i-1]=q[i-1]
    # w[i][i-1]=q[i-1]
