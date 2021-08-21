import random

r = random.randint(1, 100)
count = 0
while True:
    count += 1 # count = count + 1
    num = input('请猜数字')
    num = int(num)
    if num == r:
        print('你猜对了')
        print('这是', count, '次')
        break
    elif num > r:
        print('比答案大')
    elif num < r:
        print('比答案小')
    print('这是', count, '次')