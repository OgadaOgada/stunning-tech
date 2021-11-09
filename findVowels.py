import re
# caret ^ means match must start with a given character
# $ means match must end with a given character
# ^$ (both) means entire text must match with a given text

largeText = "All my large Text should appear here. Well, I'll find all the vowels in this large text"

vowelsLower = re.compile(r"[aeiou]")
vowelsAll = re.compile(r"[aeiou]",re.IGNORECASE)
vowelsAllCase = re.compile(r"[aeiou]",re.I) #same as above, ignore case

lowerMo = vowelsLower.findall(largeText)
allMo = vowelsAll.findall(largeText)
allCaseMo = vowelsAllCase.findall(largeText)

print(lowerMo)
print(allMo)
print(allCaseMo)