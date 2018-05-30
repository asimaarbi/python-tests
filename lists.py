


list = []


for i in range(3):
    n = input('Name :')
    list.append(str(n))
v = int(input('Enter member number to see'))
c = v
f = len(list)
if v > f:
    print(' you number low from list')
elif f <= 0:
    print(' your number ecxeeded from list ')
else:
 print(list[v -1])

#print(list[int(input('Enter member number to see'))-1])
