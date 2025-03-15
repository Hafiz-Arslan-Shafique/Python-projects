def intgr(num):
    while num != 0:
        print(num % 10)
        num = int(num/10)

num = int(input('Enter the number'))
intgr(num)