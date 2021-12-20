from os import linesep
import re
myText = r"""
we have a large database(csv) of legal case law,  we need to do some 
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
2007 YLR 28

"""
# . - any character except new line
# \d - digit (0-9)
# \D - not a digit 0-9
# \w word character a-z,A-Z,0-9,_
# \W not a word character
# \s whitespace
# \S not whitespace
# \b word boundary

# myPattern = re.compile(r"AIR")
myPattern = re.compile(r".")
# myPattern = re.compile(r"\.")
matches = myPattern.finditer(myText)

for m in matches:
    print(m)
