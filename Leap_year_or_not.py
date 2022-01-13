def is_leap(year):
    leap = False
    if 1900<=year<=(10**5):
        if year%4==0 and year%100!=0:
            leap = True
        if year%100==0 and year%400==0:
            leap = True
    return leap

year = int(input())
print(is_leap(year))

(OR)
# In case of returning the output as a boolean value, we need not use the if-else function & can be a little dry with the function as below(we can just return the condition
# since it will always return in boolean.

year=int(input())
def is_leap(year):
    return year%4==0 and (year%400==0 or year%100!=0)
print(is_leap(year))
