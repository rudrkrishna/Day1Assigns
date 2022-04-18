#decorator

def dec_twice(fun):
    def inner(a,b):
        print(a*b)
        return fun(a,b)
        #return fun(a*b, a*b)
    return inner

@dec_twice
def mul(a,b):
    print(a*b)

mul(3,5)


#generator

def fib(val):
   n1,n2=0,1
   k= 1
   n1 = n1 + n2
   yield 0
   while k<val:
       yield n1
       n1, n2 = n2, n2+n1
       k = k + 1

values= fib(int(input("Enter a number: ")))
for i in values:
    print(i, end=" ")