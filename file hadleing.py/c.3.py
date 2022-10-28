print("Name            |       Phone no. ")
file = open(r'file hadleing.py\pone.txt', "r")
lst = file.readlines()
for i in lst :
    data = i.split()
    if len(data[0])<7:    
        print( data[0] ,end = "\t\t" )
        print("|" , end = "\t")
        print ( data[1] )
    elif len(data[0])>7:
        l=8-len(data[0])
        print( data[0] ,end = (' '*l)+"\t" )
        print("|" , end = "\t")
        print ( data[1] )
file.close()
