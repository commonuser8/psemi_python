# 演算子についてのサンプルコード

a = 10
b = 2

# 数値演算
c = a + b  # 足し算
d = a - b  # 引き算
e = a * b  # 掛け算
f = a / b  # 割り算
g = a // b  # 割り算の商
h = a % b  # 割り算の余り
i = a ** b  # べき乗（a の b 乗）

print(c, d, e, f, g, h, i)

# 比較演算
j = a == b  # a と b の値が等しければ True
k = a != b  # a と b の値が等しくなければ True
l = a > b  # a の値が b の値より大きければ True
m = a < b  # a の値が b の値より小さければ True
n = a >= b  # a の値が b の値以上であれば True
o = a <= b  # a の値が b の値以下であれば True

print(j, k, l, m, n, o)

p = [1, 5, 10]
q = a in p  # a の値が、リスト p に要素として含まれているなら True
r = b not in p  # bの値が、リスト p に要素として含まれていないなら True

print(q, r)


# 以下はおまけ
# オブジェクト比較
s = [1, 2, 3]
t = [1, 2, 3]
u = s

v = s is t  # オブジェクトが同一であれば True
w = s is not t  # オブジェクトが同一でなければ True
x = s is u

print(v, w, x)

# None は常に同一のオブジェクト
# 常に同一なオブジェクトについて、詳しく知りたい方は「シングルトン」について調べてください
y = None
z = None

print(y is z)
