from functools import reduce

#negative to positive

lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]
result = filter(lambda y : y>0, map(lambda x: x*-1, lst1))

print(list(result))

#reduce function multiplication
list1 = [1, 2, 3, 4, 5, 6]

mul = reduce(lambda a, b : b*a, list1)

print(mul)

#dictionary using zip and dict functions
lst1=["Netflix", "Hulu", "Sling", "Hbo"]
lst2=[198, 166, 237, 125]

dic1= dict(zip(lst1, lst2))
print(dic1)