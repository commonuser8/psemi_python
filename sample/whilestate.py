# while 文
num = 0
while num <= 5:
    print(num)
    num += 1

# else 節
num = 0
while num <= 5:
    num += 1
    print(num)
else:
    print("while 文が正常に終了すると、else 節の処理が実行される")

# break
num = 0
while True:
    num += 1
    if num == 2:
        break
    print(num)

# continue
num = 0
while num < 5:
    num += 1
    if num == 2:
        continue
    print(num)
