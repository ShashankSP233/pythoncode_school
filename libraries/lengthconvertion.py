""" this contain convertion in length 
1)mile to km -->miletokm()
2)km to mile -->kmtomile()
3)feet to inch-->feettoinch()
4)inch to feet-->inchtofeet()
for futher info refer help()
 """


#functions

def miletokm(miles):
    """it takes value of miles in int and convert into km """
    value=miles*1.60934
    return value


def kmtomils(km):
    """it takes value of km in int and convert into miles """
    value=km/1.60934
    return value


def feettoinch(feet):
    """it takes value of feet in int and convert into inch """
    value=feet*12
    return value


def inchtofeet(inch):
    """it takes value of inch in int and convert into feet """
    value=inch/12
    return value

#constant values
mile_in_km=1.609344
km_in_miles=0.621371192237334
feet_in_inch=12
inch_in_feet=0.08333

#help
def help():
    print('miletokm(miles):\n \t it takes value of miles in int and convert into km \n \t formula:km=miles*1.609344')
    print('kmtomile(km):\n \t it takes value of km in int and convert into mile \n \tformula:mile=km/1.609344')
    print('feettoich(feet):\n \t it takes value of feet in int and convert into inch \n\t formula:feet=inch*12')
    print('inchtofeet(inch):\n \t it takes value of inch in int and convert into feet \n\t formula:km=miles/12')
