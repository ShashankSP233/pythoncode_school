"""c.8.py"""
def displaywords():
    file1=open(r'file hadleing.py\story.txt','r')
    lisline= file1.readlines()
    for i in lisline:
        lisword=i.split()
        for l in lisword:
            if len(l)<5:
                print(l,end=',')
displaywords()                