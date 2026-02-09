def avg(num):
    list1=list(num)
    sum=0
    for x in list1:
        sum=sum+x
    return sum 

n=(12,34,87,56,98,78,59,82)
l=len(n)
print("tuple is",n)
print("average are",avg(n)/l)