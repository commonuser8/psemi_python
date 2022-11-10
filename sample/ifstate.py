# if 文
a = 1

if a > 0:  # a > 0 を満たすとき
    print("a は 0 より大きい")
elif a < 0:  # 上の条件 (a > 0) を満たさず、a < 0 を満たすとき
    print("a は 0 より小さい")
else:  # それ以外（上の条件全てを満たさないとき）
    print("a は 0")


b = True
c = False

if b and c:  # and: かつ [両方が条件を満たす (True) なら True]
    print("True")
else:
    print("False")

if b or c:  # or: または [どちらかが条件を満たすなら True]
    print("True")
else:
    print("False")

if not b:  # not: ではない　[条件を満たさないなら True]
    print("True")
else:
    print("False")

# 1 を True, 0 を False としても扱える
if a == b:
    print("True")
else:
    print("False")
