# import re

# text = "Agent Col gave money to agent Fin for both agents to work together"
# wordMatch = re.compile(r"agent \w+",re.I)
# wordMatch2 = re.compile(r"agent (\w)\w*",re.I)
# wordMatch3 = re.compile(r"agent \w+")

# mo1 = wordMatch.findall(text)
# # mo2 = wordMatch2.findall(text)
# mo3 = wordMatch.sub("Subbed",text)
# mo4 = wordMatch2.sub(r"Agent \1*****",text)

# print(mo1)
# # print(mo2)
# print(mo3)
# print(mo4)

import pyperclip


def format_number(num):
    print(format(num,","))
    return

num  = int(pyperclip.paste())
format_number(num)