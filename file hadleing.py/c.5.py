file1=open(r'file hadleing.py/article.txt','r')
data=file1.read()
print(data)
count=0
for i in data:
    if i.islower():
        count+=1
print(count) 
