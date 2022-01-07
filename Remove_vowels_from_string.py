s=str(input())
v="AEIOUaeiou"
for i in s:
    if i in v:
        s=s.replace(i,"")
print(s)
