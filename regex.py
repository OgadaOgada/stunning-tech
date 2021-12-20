from os import linesep
import re
myText = r"""we have a large database(csv) of legal case law,  we need to do some 
manipulations to it, we have tried to use Machine learning to extract 
citations but there is too much variance and fluctuations and are now 
opting for a regex methodology, following are some of the examples of 
the types of citations the regex needs to extract.

collince.com
PLD 1995 SC 406.
PLD 2010 Supreme Court 705
PLD 1987 SC 504
PLD 2007 Karachi 469
PLD 1966 Kar. 518
PLD 1977 Lah 71
PLJ 2010 1
1999 SCMR 2883
2010 SCMR 196
1995 SCMR 1748.
2019 CLC 1
1994 CLC 2214
2012 CLC 250 Lah.
2003 CLD 596
2003 CLD 1703
2021 PTD 281
2014 PTD 225
AIR 1943 PC 83
AIR 1987 SC 1109
AIR 1929 Lahore
1999 PLC (C.S.) 1539
2005 YLR 1968
2007 YLR 28__- last

123-123-123
345_367-589
345.567.234

800.567.234
900.567.234
 cat 
mat
bat
pat
"""
# . - any character except new line
# \d - digit (0-9)
# \D - not a digit 0-9
# \w word character a-z,A-Z,0-9,_
# \W not a word character
# \s whitespace
# \S not whitespace
# \b word boundary e.g \bword
# \B not a word boundary
# ^ begining of a string, the character search for has to be at the begining of the text ^start
# $ end of a string, text has to be at the end last$
# [] matches characters in bracket
# [^ ] matches characters NOT in bracket
# | either or
# 
# 


# myPattern = re.compile(r"AIR")
t = "\d\d\d"
# [] character set
# myPattern = re.compile(r"{}[-._]{}[-._]{}".format(t,t,t))
# myPattern = re.compile(r"[89]00[-._]{}[-._]{}".format(t,t)) #matches digits starting with 800 or 900
# myPattern = re.compile(r"[1-9]00") #match digits btwn 1 and 5 and has 00 and the end
# myPattern = re.compile(r"[^2-7]00") # carret in character set negates the match
# myPattern = re.compile(r"\b[^b]at\b") # carret in character set negates the match...will search for non lowercase a-z
# parttern = "\b\d\d\d\d[a-zA-Z0-9()-_+.\s]*"
# myPattern = re.compile(r"[0-9]{3}\s[a-zA-Z0-9()-_+.\s]") # matching some pattern and any other thing that follows
myPattern = re.compile(r"\b[0-9]{4}\s||\b[a-zA-Z]{3}\s") #  a grouping matching either 1+ whitespaces or end of string anchor (here, $ matches the end of string.)


# myPattern = re.compile(r"\.")
# matches = myPattern.finditer(myText)
matches = myPattern.findall(myText)
# print(matches)
for m in matches:
    print(m)





