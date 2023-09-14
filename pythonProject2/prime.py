num = int(input("请输入一个整数："))
for i in range(2, num):
    if i % 2 == 1 and i > 1:
        prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            print(i)