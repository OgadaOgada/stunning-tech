import re
import os

os.system("cls") #clear the screen just before displaying output
# caret ^ means match must start with a given character
# $ means match must end with a given character
# ^$ (both) means entire text must match with a given text

largeText = "All my large Text should appear here. Well, I'll find all the vowels in this long text, both lower and Upper"

vowelsLower = re.compile(r"[aeiou]")
vowelsAll = re.compile(r"[aeiou]",re.IGNORECASE)
# vowelsAllCase = re.compile(r"[aeiou]",re.I) #same as above, ignore case
vowelsAllUpperCase = re.compile(r"[AEIOU]") #UPPERCASE VOWELS

lowerMo = vowelsLower.findall(largeText)
allMo = vowelsAll.findall(largeText)
allCaseMo = vowelsAllUpperCase.findall(largeText)

print("Lowercase",lowerMo)
print("Both cases",allMo)
print("Upper case",allCaseMo)