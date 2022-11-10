set_a = {0, 1, 2}
list_b = [2, 3, 4]
tuple_c = (2, 4, 6)
set_b = set(list_b)
set_c = set(tuple_c)

# 和集合
union_a = set_a | set_b | set_c  # 集合同士の和集合
print(union_a)

union_b = set_a.union(list_b, tuple_c)  # 集合以外でも和集合を作れる
print(union_b)

# 差集合
difference_a = set_a - set_b - set_c
print(difference_a)

difference_b = set_a.difference(list_b, tuple_c)  # 集合以外でも差集合を作れる
print(difference_b)

# 積集合
intersection_a = set_a & set_b & set_c
print(intersection_a)

intersection_b = set_a.intersection(list_b, tuple_c)  # 集合以外でも積集合を作れる
print(intersection_b)

# 対称差集合
symmetric_diff_a = set_a ^ set_b ^ set_c
print(symmetric_diff_a)

symmetric_diff_b = set_a.symmetric_difference(list_b)  # 引数が一つしか取れない
symmetric_diff_b = symmetric_diff_b.symmetric_difference(tuple_c)
print(symmetric_diff_b)


s1 = {1, 2, 3}
s2 = {3, 2, 1}
s3 = {4, 5, 6}
s4 = {1, 2, 3, 4, 5, 6}

# 完全一致
print(s1 == s2)  # s1 と s2 の集合の要素が同数で全て同じなら True

# 完全不一致
print(s1.isdisjoint(s3))  # s1 と s2 に同じ要素が一つもなければ True

# 部分集合
print(s1.issubset(s4))  # s1 が s4 の要素だけを持つ集合なら True (s1 <= s4)

# 上位集合
print(s4.issuperset(s1))  # s4 が s1 の要素全てを持つ集合なら True (s4 >= s1)
