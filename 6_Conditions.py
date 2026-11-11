# change this code
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

#[中身があるかどうか？]の確認の時はif 変数:でOK
if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

#「配列が存在する（かつ）」かつ「その最初の要素（first_array[0]）が 1 である」かどうか？
if first_array and first_array[0] == 1:
    print("5")

#second_number が「ゼロ」ではないか？
if not second_number:
    print("6")
