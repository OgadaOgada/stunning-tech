#format number

numbers = 3237823434.3434355
number2dp = format(numbers, "0.2f")# up to 2 decimal places
print(number2dp)
number = format(numbers, '>20.2f')# reserves ten spaces for the number, infront
print(number)
number = format(numbers,"<20.2f")# reservrs 20 spaces for the number behind
print(number)
number = format(numbers,"^20.2f")# reserves 20 but with number centered
print(number)
number = format(float(number2dp),",")# reserves 20 but with number centered
print(number)