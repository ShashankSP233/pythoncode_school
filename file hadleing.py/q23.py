file1 = open(r'E:\py code\file hadleing.py\Poem.txt','r')
file2 = open(r'E:\py code\file hadleing.py\poen2.txt','w')

line = file1.readlines()

print(line[-1])
