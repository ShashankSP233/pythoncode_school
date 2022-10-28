file1=open(r'file hadleing.py/Poem.txt','r')
ary= (file1.read()).split()
to_count=0
the_count=0
for i in ary:
    if i.lower() == 'to':
        to_count+=1
    if i.lower() == 'the':
        the_count+=1
print('no of to are:',to_count)
print('no of the are:',the_count)