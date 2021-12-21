#!/usr/bin/env python3
import re
myText = r"""we have a large database(csv) of legal case law,  we need to do some 
manipulations to it, we have tried to use Machine learning to extract 
citations but there is too much variance and fluctuations and are now 
opting for a regex methodology, following are some of the examples of 
the types TES of citations the regex needs to extract.
TESTHERE
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
1923
1994 CLC 2214
2012 CLC 250 Lah.
2003 CLD 596
2003 CLD 1703
2021 PTD 281
2014 PTD 225
AIR 1943 PC 83
AIR 1987 SC 1109
AIR 1929 Lahore
LK
1999 PLC (C.S.) 1539
2005 YLR 1968
2007 YLR 28
_
_- last

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
myText2 = """
http://www.wikipedia.org
http://www.qq.com
http://www.google.co.in
https://www.google.co.id
https://youku.com
http://www.rakuten.co.jp
http://www.craigslist.org
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
# * 0 or more (optional)
# + 1 or more
# ? 0 or one optinal too
# {3} exact number
# {3,4} range of numbers (minimum, maximum)


# myPattern = re.compile(r"AIR")
t = "\d\d\d"
# [] character set
# myPattern = re.compile(r"{}[-._]{}[-._]{}".format(t,t,t))
# myPattern = re.compile(r"[89]00[-._]{}[-._]{}".format(t,t)) #matches digits starting with 800 or 900
# myPattern = re.compile(r"[1-9]00") #match digits btwn 1 and 5 and has 00 and the end
# myPattern = re.compile(r"[^2-7]00") # carret in character set negates the match
# myPattern = re.compile(r"\b[^b]at\b") # carret in character set negates the match...will search for non lowercase a-z
# myPattern = re.compile(r"\d{3}.\d{3}.\d{3}")
# pattern = "[A-Z0-9()-+_.]+"
# myPattern = re.compile(r"{}\s{}\s{}.*".format(pattern,pattern,pattern)) #regex for the challenge

# myPattern = re.compile(r"(https?://)(www\.)?([a-zA-Z0-9-_]+)(\.[a-zA-Z0-9-_]+)(\.[a-zA-Z0-9-_]+)?")
myPattern = re.compile(r"https?://(www\.)?([a-zA-Z0-9-_]+)(\.[a-zA-Z0-9-_]+)(\.[a-zA-Z0-9-_]+)?") 
#above, matching urls with the s in https being optional(can appear once or not), a groups www being optional, a first group of characters, 
# a dot and a group of characters, and an optional last dot and group of characters

# myPattern = "\b\d{4}[a-zA-Z0-9()-_+.\s]*"
# myPattern = "\b\d\d\d\d[a-zA-Z0-9()-_+.\s]*"

# myPattern = re.compile(r"\b\d\d\d\d\s\w*\s\w*") #  a grouping matching either 1+ whitespaces or end of string anchor (here, $ matches the end of string.)


# myPattern = re.compile(r"\.")
# re.match only matches once from the start of the sentence, not iterable...matches just like a carret
# matches = myPattern.findall(myText)
# matches = myPattern.finditer(myText)
# print(matches)
# for m in matches:
    # print(m)
    # print(m.group(0))
    # print(m.group(1))
    # print(m.group(2))
    # print(m.group(3))
    # if m.group(4) != None:
    #     print(m.group(2),m.group(3),m.group(4))
    # else:
    #     print(m.group(2),m.group(3))

# working with subs, replacing the urls with matched groups 2,3 and 4
subbed_urls = myPattern.sub(r"\2\3\4",myText2)
# print(subbed_urls)
    

# learn regex withing 5 mins

# emailRegex = re.compile(r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|edu|net)")
# useremail = input("Email: ")
# if(re.search(emailRegex,useremail)):
#     print("Valid email")
# else:
#     print("Invalid email")


# using the multiline flag

mtext = ''''
one sentence endone
two sentence endtwo
three sentence endthree
'''
# partt = re.compile(r"endtwo$",re.MULTILINE)
# mo = partt.findall(mtext)
# print(mo)

# printing pattern
# txt1 = '*'
# txt = '*'
# lng = 10
# for i in range(1,lng+1):
#     print(txt*i)
# for i in range(lng,0,-1):
#     print(txt1*i)

# function with default value
def func(greeting='Hi',name='You'):
    return '{}, {}'.format(greeting,name)

print(func(name="Collince"))

# *args (tuple) and **kwargs (dictionary)
def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
# student_info("Math","Eng","Kis",Name="Collince",Form="Three",Stream="B")
subjects = ['Math', 'Eng', 'Kis']
info = {'Name': 'Collince', 'Form': 'Three', 'Stream': 'B'}
# student_info(subjects,info)
student_info(*subjects,**info)

# number of days per month, first value placeholder for indexing purposes
month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    #return true for leap years and False otherwise
    return year % 4 == 0 and (year % 100 !=0 or year % 400 == 0)

def days_in_month(year,month):
    #return number of days in that month in the year
    if not 1 <= month <= 12:
        return "Invalid Month"
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print(days_in_month(2020,2))