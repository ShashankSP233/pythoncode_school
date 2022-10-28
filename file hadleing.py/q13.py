file1 = open(r"file hadleing.py\image2.png", "wb")
file2 = open("‪file hadleing.py\\934011.jpg", "rb") 
while True:
    byte = f.read(1)
    if not byte:
        break
    file1.write(byte[0])