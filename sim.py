n=int(input())
a=[]
for _ in range(n):
    a.append(input())
ans=[]
for i in a:
    p=i.split('-')
    temp="-".join(p[::-1])
    ans.append(temp)
ans.sort()
for i in ans:
    p=i.split('-')
    temp="-".join(p[::-1])
    print(temp)
