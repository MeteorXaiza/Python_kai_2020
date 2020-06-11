# coding:utf-8


from xaizalibs.CMOSanalyzerlib import *


# getArrFloatCsv
# np.argwhere
# numpyの値への参照方法
# continue
# list.append


# CSVファイルの読み込み
example_frame = getArrFloatCsv('example_frame.csv')
print(example_frame, '\n')


# Numpyの配列を作成
arr = np.arange(12).reshape((3, 4))
# 配列の中身を見てみる
print(arr, '\n')
# 特定の要素を参照する
print(arr[1, 2], '\n')
y = 2
x = 3
# 参照は変数を使っても良い
print(arr[y, x], '\n')


arr = np.arange(4).reshape((1, 4)) * (np.arange(3) + 1).reshape((3, 1))
print(arr, '\n')
# np.argwhereは要素が条件を満たすインデックスを返す
print(np.argwhere(arr < 4), '\n')


for x in range(10):
    # xを2で割ったあまりが1のとき
    if (x % 2) == 1:
        # continueでfor処理を一回だけ行わずにスキップする
        continue
    print(x)
print('\n')

alphabet_list = ['a', 'b', 'c']
print(alphabet_list)
# .appendで配列の末尾に要素を追加できる
alphabet_list.append('d')
print(alphabet_list)
alphabet_list.append('e')
print(alphabet_list)
print('\n')
