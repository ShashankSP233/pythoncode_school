fil1=open(r"file hadleing.py\1.txt","r+")
fil2=open(r"file hadleing.py\2.txt","w+")
rl = fil1.read()
rl= rl.split()
a=''
for i in rl:
    a=a+i
    a=a+' '

fil2.write(a)
fil2.close()
fil1.close()



