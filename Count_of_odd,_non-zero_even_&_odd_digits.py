a=intput()
count=0
counto=0
count0=0
for i in str(a):
    if int(i)>0:
        if int(i)%2==0:
            count+=1
        else:
            counto+=1
    elif int(i)==0:
        count0+=1
print("Number of odd digits:",counto)
print("Number of non-zero even digits:",count)
print("Number of zeros:",count0)
