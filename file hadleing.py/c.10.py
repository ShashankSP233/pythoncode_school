def a_sort(dirt):
    file1=open(r'{}'.format(dirt),'r')
    count=0
    relines=file1.readlines()
    for i in relines:
        if i[0]=='A':
            count+=1
    print(count)
a_sort("file hadleing.py\LINES.txt")
    