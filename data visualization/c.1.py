import matplotlib.pyplot as plt
import numpy as np
#rainfall
year=['jan',"feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
n=[140,130,130,190,160,200,150,170,190,170,150,120]
s=[160,200,130,200,200,170,110,160,130,140,170,200]
e=[140,180,150,170,190,140,170,180,190,150,140,170]
w=[180,150,200,120,180,140,110,130,150,190,110,140]
c=[110,160,130,110,120,170,130,200,150,160,170,130]
n=np.array(n)
y=np.arange(12)
s=np.array(s)
e=np.array(e)
w=np.array(w)
c=np.array(c)
## BAR-GRAPH
#plt.bar(y+0.00,n,width=0.15)
#plt.bar(y+0.15,s,width=0.15)
#plt.bar(y+0.30,e,width=0.15)
#plt.bar(y+0.45,w,width=0.15)
#plt.bar(y+0.60,c,width=0.15)
#plt.xticks(y,year)
#plt.xlabel('months')
#plt.ylabel('rainfall(in mm)')
#plt.show()
#
##PIE
#jan=[140,
#    160,
#    140,
#    180,
#    110]
#lb=['n','s','e','w','c']
#plt.pie(jan,labels=lb)
#plt.legend(loc='upper left')
#plt.show()
#
#line graph
plt.plot(year,n,label='north')
plt.plot(year,s,label='west')
plt.plot(year,e,label='east')
plt.plot(year,w,label='west')
plt.plot(year,c,label='central')
plt.legend(loc='upper left')
plt.xlabel('months')
plt.ylabel('rainfall(in mm)')
plt.show()
