import math
import sys
import time
from datetime import datetime

import pythonFunctions

# r = int(input("Radius: "))
now  = datetime.now()

print(pythonFunctions.addition(2,8))
# print(math.pi*r**2)
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

f = 34.666
print(math.floor(f))
