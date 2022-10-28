# def nthRoot(a,n):
#     return (a**(1/n))
# x=int(input('enter the number'))
# y=int(input("enter the root" ))
# # print(nthRoot(x,y))
s='abcde _ f  1 _ 3'
d=''
count=0
lis=[]

for i in range(0,len(s)):
    e=s[i]
    if e==' ':
        if s[i+1]=='_' and s[i+2]==' ':
            # print(d)
            # lis+=d
            # d='' 
            # print(d)
            d+='\n'
        else:
            if s[i-1]=='_' and s[i-2]==' ':
                # print(d)
                # lis+=str(d)
                # d=''
                d+='\n'
            else:
                d+=e
    elif e=='_':
        if s[i-1]==' ' and s[i+1]==' ':
            # lis+=d
            # d=''
            d+='\n'
        else:
            d+=e
    else:
        d+=e
print(d)
    


