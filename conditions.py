
i, j, k = 8, 2, 6

one = i * j + k
two = k * i + j
three = j * k + i

if(one > two):
    if(one > three):
        print("One is better")
    
    else: print("One is not the better")
    
elif(two > one):
    if(two > three):
        print("Two is better")
    
    else: print("Two is not better")

elif(three > one and three > two):
    print("Three is better")

# Two is better, confirmation
if(two > one and two > three):
    print("Two is very better")