import itertools

my_counter = 0

#REPEAT
sz = list(itertools.repeat("I love my lady",5))
for i in sz:
    my_counter += 1
    print(my_counter,i)

print()
#COUNT
my_number = itertools.count(1,step=1)
for i in my_number:
    print(i)
    if i == 20:
        break
for i in itertools.count(0.1, 1.5):
    print(i)
    if i > 3:
        break


