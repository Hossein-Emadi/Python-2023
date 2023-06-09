a=input("please Enter a string:  ")
b=a.split()
c=0
for i in b:
    d=len(i)
    if d>c:
       c=d
       big_word=i
print("the longest word:",big_word,"alphabet count:",c)
