
def remove_letter(sentence,letter):
        a=sentence.split(letter)
        sentence=''
        for  i in a:
            sentence=sentence+i
        print(sentence)
#remove_letter('how do you do ','o')
def cap_words1(a):
        b=a.split()
        c=''
        for i in b:
            i=i.capitalize()
            c+=i+' '
        return c
#print(cap_words1('hello how are you fella \n hope you are fine\t as am i'))

