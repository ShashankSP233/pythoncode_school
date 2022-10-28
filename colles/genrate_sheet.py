import ast
def genrate_sheet(na):
    temp_sheet=open('tempcharsavefile.txt','r')
    char_data=temp_sheet.readline()
    # characterfilename=input('please enter the name of char')
    char_info = ast.literal_eval(char_data)
    charsheet = open((na+'.txt'), 'a')
    for  char_topic in char_info:
        char_content=char_info[char_topic]
        racestr=f'{char_topic} : {char_content} \n'
        charsheet.write(racestr)
     




