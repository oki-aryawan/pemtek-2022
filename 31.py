a = int(input("Enter Lower Range: "))
b = int(input("Enter Upper Range: "))

def bilanganPrima (upper, lower):
    hasil = []
    for num in range(upper, lower):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                hasil.append(num)
    return hasil

print(bilanganPrima(a+1,b))

