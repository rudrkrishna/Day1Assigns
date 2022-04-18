#Lambda fun

eqn = lambda a, b, c, x: print(a*x*x+b*x+c)

eqn(1, 2, 3, 4)

#count of occurance of Letters
lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
liCount=[]

letterCount = lambda stri, c: str(stri.count(c))
def counterFun(li):
    return "A -> "+letterCount(li, 'A')+" | "+"a -> "+letterCount(li, 'a')

countLi=list(map(counterFun, lst1))

print(countLi)