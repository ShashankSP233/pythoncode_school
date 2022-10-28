def ath_sort(f1,f2):
    lis=f1.readlines()
    for i in lis:
        if 'Atheletics' in i:
            f2.write(i)


file1=open(r'file hadleing.py\sporys.dat','r')
file2=open(r'file hadleing.py\athl.dat','w')
ath_sort(file1,file2)