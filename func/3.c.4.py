def func(a,b):
    import random
    c=random.randrange(a,b)
    print(c)

a=int(input('first'))
b=int(input('second'))
for i in range (3): 
    func(a,b)  

