import re

my_compile = re.compile(r"""
\d\d\d  #area code
-
\d\d\d  #first three digits
-
\d\d\d  #second three digits
-
\d\d\d  #last three digits
""",re.VERBOSE | re.IGNORECASE | re.DOTALL) #using the bitwise operator/pipe
