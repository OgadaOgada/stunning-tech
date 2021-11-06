with open ("q:\Learning\Python\stunning-tech\copyPaste.txt","r") as file:
    data1 = file.read()
    data = data1.replace("\n","XX ")
    print(data1)
    print(data)
with open ("q:\Learning\Python\stunning-tech\copyPaste.txt","w") as file:
    # file.write(data)
    file.close()
with open ("q:\Learning\Python\stunning-tech\copyPaste.txt","r") as file:
    print(file.read())