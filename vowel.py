#vowel repetation problem
s=input()
v="aeiou"
mx=-999
d={}
for i in s:
    if i in v:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
        if d[i]>mx:
            mx=d[i]
            ans=i
print(d)
print(ans)
