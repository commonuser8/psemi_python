# for 文
langs = ["Python", "Java", "C#"]
for s in langs:  # for (String s: langs)
    print(s)

# range 関数
for i in range(0, 5, 1):  # for (int i = 0; i < 5; i = i + 1)
    print(i)

# range 関数の引数は場合によっては省略できる
# for i in range(0, 5):  # 一つ減らすと三つ目の引数として 1 が補間される
# for i in range(5):  # さらに一つ減らすと一つ目の引数に 0 が補間される


# break
a = []
for i in range(5):
    if i == 2:
        break
    a.append(i)

print(a)

# continue
b = []
for i in range(5):
    if i == 2:
        continue
    b.append(i)

print(b)
