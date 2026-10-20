#変数の宣言
x = object()
y = object()

#リストの宣言＋リスト内容の乗算
x_list = [x] * 10
y_list = [y] * 10

#リストの結合
big_list = x_list + y_list

#リスト内オブジェクト数の出力
#%dで整数型変数の出力
#len()でリスト内のオブジェクト数を取得
print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")