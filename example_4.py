# coding:utf-8


from xaizalibs.nplib import *

# example_frame.fitsを読み込む
example_frame = getArrFloatCsv('example_frame.csv')
print(example_frame, '\n')
# event_thを設定
event_th = 84.5
# split_thを設定
split_th = 82.5

# フレームのサイズ
frame_shape = example_frame.shape

# イベントの中心ならばTrue、そうでなければFalseとなる配列
is_event_center = example_frame > event_th
# フレームの端はイベントの中心にならないのでFalseにする
is_event_center[0, :] = False
is_event_center[frame_shape[0]-1, :] = False
is_event_center[:, 0] = False
is_event_center[:, frame_shape[1]-1] = False

PH0 = example_frame[1:frame_shape[0]-1, 1:frame_shape[1]-1]
print(PH0, '\n')
for x in [-1,0,1]:
    for y in [-1,0,1]:
        if x == 0 and y == 0:
            continue
        PH = example_frame[1+y:frame_shape[0]-1+y, 1+x:frame_shape[1]-1+x]
        print(PH, '\n')
        is_event_center[1:frame_shape[0]-1, 1:frame_shape[1]-1] *= PH0 > PH

event_center_pixel = np.argwhere(is_event_center)

single_PHasum_list = []
for pixel in event_center_pixel:
    event_PH = example_frame[pixel[0]-1:pixel[0]+2, pixel[1]-1:pixel[1]+2]
    print(event_PH)
    if (event_PH >= split_th).sum() == 1:
        single_PHasum_list.append(event_PH[1,1])

print(is_event_center)
print(single_PHasum_list)
