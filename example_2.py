# coding:utf-8


from xaizalibs.nplib import *

# example_frame.fitsを読み込む
example_frame = getArrFloatCsv('example_frame.csv')
# event_thを設定
event_th = 84.5
# split_thを設定
split_th = 82.5

# 「イベントの中心となる候補のピクセル」＝「PHがevent_thよりも大きいピクセル」を特定
large_PH_pixel = np.argwhere(example_frame > event_th)
# イベントの中心となるピクセルを格納するためのlist
event_center_pixel = []
# イベントの中心のピクセルを特定する
for pixel in large_PH_pixel:
    # フレームの端はイベントの中心にならないので処理をしない
    if pixel[0] == 0 or pixel[0] == 9 or pixel[1] == 0 or pixel[1] == 9:
        continue
    PH0 = example_frame[pixel[0], pixel[1]]
    # イベントの中心でなかったとき0になるフラグ変数
    flg = 1
    # a=0,1,2 でループ
    for a in range(3):
        # 候補のピクセルの左右を確認するための変数
        x = a - 1
        # b=0,1,2 でループ
        for b in range(3):
            # 候補のピクセルの上下を確認するための変数
            y = b - 1
            # 候補のピクセルを確認する必要はないので処理しない
            if x == 0 and y == 0:
                continue
            # 「候補のピクセルの近くのPH」が「候補のピクセルのPH」以上ならば
            # フラグ変数を0にする
            if example_frame[pixel[0]+y, pixel[1]+x] >= PH0:
                flg = 0
    # フラグ変数が1のままならばlistにピクセルを追加する
    if flg == 1:
        event_center_pixel.append(pixel)

# シングルイベントのPHasumを格納するためのlist
single_PHasum = []
# シングルイベントか調べてシングルイベントならばPHasumをlistに追加する
for pixel in event_center_pixel:
    # イベントの中心のPH
    PH0 = example_frame[pixel[0], pixel[1]]
    # シングルイベントでなかったとき0になるフラグ変数
    flg = 1
    for a in range(3):
        x = a - 1
        for b in range(3):
            y = b - 1
            if x == 0 and y == 0:
                continue
            # イベントの中心の周りのPHがsplit_th以上ならばフラグ変数を0にする
            if example_frame[pixel[0]+y, pixel[1]+x] >= split_th:
                flg = 0
    # フラグ変数が1のままならばlistにPHasum=PH[0]を追加する
    if flg == 1:
        single_PHasum.append(example_frame[pixel[0], pixel[1]])

# シングルイベントのPHasumのlistを表示する
print(single_PHasum)
