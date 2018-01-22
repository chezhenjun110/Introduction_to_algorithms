weight=[3,4,5]
price= [4,5,6]
totalweight=10
n=len(weight)
def printMax(a, b):
    if a > b:
        return a
    else:
        return  b
# f=[[0 for i in range(totalweight+1)] for j in range(n)]             #空间和时间都是O(N*V)
# for i in range(0,n):
#     for j in range(1,totalweight+1):
#         if weight[i]<totalweight:
#             f[i][j]=printMax(f[i-1][j],f[i-1][j-weight[i]]+price[i])
#         else:
#             f[i][j]=f[i-1][j]




f=[0 for i in range(totalweight+1)]                   #空间为O(V)
for  i in range(n):
    for j in range(totalweight+1):
        v=totalweight-j
        if weight[i]<v:
            f[v]=printMax(f[v],f[v-weight[i]]+price[i])

print(f)