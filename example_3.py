# coding:utf-8


from xaizalibs.nplib import *


example_frame = getArrFloatCsv('example_frame.csv')
print(example_frame, '\n')
# .shapeで配列の形状を調べられる
print(example_frame.shape, '\n')
# 変数に格納することもできる
s = example_frame.shape
print(s, '\n')

# 「:」を使うことで配列を切り取ることができる（スライシング）
print(example_frame[1:4, 2:6], '\n')
# スライシングによって配列の一部を書き換えることもできる
example_frame[1:3, 2:5] = 12.0
print(example_frame, '\n')

arr_a = ((np.arange(4).reshape((1, 4)) % 2) == 0) * np.ones((4,4), dtype=bool)
arr_b = (np.arange(4).reshape((4, 1)) < 2) * np.ones((4,4), dtype=bool)
# numpyの配列は数値だけでなくbool（TrueとFalse）を入れることもできる
print(arr_a, '\n')
print(arr_b, '\n')
# 「or」は「+」で演算する
arr_or = arr_a + arr_b
print(arr_or, '\n')
# 「and」は「*」で演算する。
arr_and = arr_a * arr_b
print(arr_and, '\n')

arr = np.arange(100) + 1
print(arr)
# .sum()は配列の要素の合計を返す（数値の配列）
print(arr.sum())
# 要素がboolならばTrueの個数を返す
print(arr_or.sum())
