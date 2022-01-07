s=str(input())
vowels="AEIOUaeiou"
for i in s:
    if i in v:
        s=s.replace(i,"")
print(s)

#OR

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for i in s:
    if i in vowels:
        s = s.replace(i, "")
print(s)
