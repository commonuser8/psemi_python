# 関数の定義
def rectangle(a, b):  # 縦と横の長さを渡すと四角形の面積を返す関数
    return a * b


def triangle(a, b):  # 底辺と高さを渡すと三角形の面積を返す関数
    return a * b / 2  # rectangle(a, b) / 2


a = 5
b = 10
print(rectangle(a, b), triangle(a, b))


def indexed_print(*args):  # 引数の中身を、先頭に番号をつけて順番に表示する関数（戻り値は None）
    i = 1
    for s in args:
        print(str(i) + ":" + s)
        i += 1


indexed_print("Java", "Python", "C++")
