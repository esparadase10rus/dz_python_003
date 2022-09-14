x = ""
n = int(input("Введите число для преобразовывания :\n"))
while n != 0:
    x = str(n%2) + x
    n //=2
print(x)