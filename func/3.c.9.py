def equdis(a,b):
    
    c=1
    d=a
    e=b
    for i in range ((b-a)//2):
        d+=1
        e-=1
    
        if d-a==e-d and b-e==d-a:
           c==1
           print(a,d,e,b)
      
           
a=int(input('enter start numb'))
b=int(input('enter last numb'))          
equdis(a,b)
