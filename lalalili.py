l_range = int(input("Enter Lower Range: "))
u_range = int(input("Enter Upper Range: "))
print("Prime numbers between", l_range, "and", u_range, "are:")
prima= []
for num in range(l_range, u_range + 1):
# all prime numbers are greater than 1
    for i in range(2, num):

        if (num % i) == 0:
            break
        else:
                #print(num)
            prima.append(num)
print(prima)