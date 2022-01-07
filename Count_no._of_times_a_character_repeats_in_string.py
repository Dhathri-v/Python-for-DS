s=str(input())
ch=str(input())
count=0
for i in s:
    if ch.lower()==i.lower():
        count=count+1
        
print(count)
