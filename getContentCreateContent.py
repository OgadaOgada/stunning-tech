with open('preproinsulin-seq-clean.txt') as file: #opening the created preproinsulin text file
    mainFileContent = (file.read()).strip() #reading the contents of the preproinsulin text file and removes the leading spaces
    print(mainFileContent) #print the data read above
    dataLength = len(mainFileContent.replace(" ","")) #removes all the white spaces within the string for finding length
    print(dataLength)#printing the length from above
    
# creating a substring of data and writing it insulin text file
with open("lsinsulin-seq-clean.txt","w") as myFile: #creates the file lsinsulin-seq-clean.txt as myFile and sets the write function by w
    content = mainFileContent[0:24:1] #get the substring of mainFileContent got from above starting from 1 up to 24 incrementing by 1
    myFile.write(content) #writes the value of content to myFile which lsinsulin-seq-clean.txt
    print(content) #dispalys the written content
    print(len(content))

with open("lsinsulin-seq-clean.txt","r") as file:
    print("lsinsulin content: "+file.read())
    
# creating a substring of data and writing it binsulin-seq-clean.txt text file
with open("binsulin-seq-clean.txt","w") as file:
    content = mainFileContent[24:54:1]
    file.write(content)
    print("\n")
    print(content)
    print(len(content))

with open("binsulin-seq-clean.txt","r") as file:
    print("binsulin-seq-clean.txt content: "+file.read())
    
# creating a substring of data and writing it cinsulin-seq-clean.txt text file
with open("cinsulin-seq-clean.txt","w") as file:
    content = mainFileContent[54:89:1]
    file.write(content)
    print("\n")
    print(content)
    print(len(content))

with open("cinsulin-seq-clean.txt","r") as file:
    print("cinsulin-seq-clean.txt content: "+file.read())
    
# creating a substring of data and writing it ainsulin-seq-clean.txt text file
with open("ainsulin-seq-clean.txt","w") as file:
    content = mainFileContent[89:110:1]
    file.write(content)
    print("\n")
    print(content)
    print(len(content))

with open("ainsulin-seq-clean.txt","r") as file:
    print("ainsulin-seq-clean.txt content: "+file.read())