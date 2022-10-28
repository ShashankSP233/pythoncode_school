""" this contain convertion in length 
1)kg to tonne -->kgtotone()
2)tone to kg -->tonetokg()
3)kg to pound-->kgtopound()
4)pound to kg-->poundtokg()
for futher info refer help()
 """


#functions

def kgtotonne(kg):
    """it takes value of kg in int and convert into tonne"""
    value=kg/1000
    return value


def tonnetokg(tonne):
    """it takes value of tonne in int and convert into kg """
    value=tonne*1000
    return value


def kgtopound(kg):
    """it takes value of kg in int and convert into pound """
    value=kg*2.20462
    return value


def poundtokg(pound):
    """it takes value of pound in int and convert into kg """
    value=pound/2.20462
    return value

#constant values
kg_in_tonne=0.001
tonne_in_kg=1000
kg_in_pound=2.20462
pound_in_kg=0.45359290943564


#help
def help():
    print('kgtotonne(kg):\n \t it takes value of kg in int and convert into tonne \n \t formula:tone=kg/1000')
    print('tonnetokg(tonne):\n \t it takes value of tonne in int and convert into kg \n \tformula:kg=tone*1000')
    print('kgtopound(kg):\n \t it takes value of kg in int and convert into pound \n\t formula:pound=kg*2.20462')
    print('poundtokg(pound):\n \t it takes value of pound in int and convert into kg \n\t formula:kg=pound/2.20462')
