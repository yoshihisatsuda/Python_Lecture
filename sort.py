print("5つの実数を入力してください。")

# 5つの数値を入力してリストに保存する
numbers = []
for i in range(5):
	value = float(input(f"{i + 1}つ目の値："))
	numbers.append(value)

# 並べ替え前のリストを表示する
print("並べ替え前：", numbers, sep="")

# 隣り合う値を比較して入れ替え、大きい順に並べる
for i in range(4):
	for j in range(4 - i):
		if numbers[j] < numbers[j + 1]:
			numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# 並べ替え後のリストを表示する
print("並べ替え後：", numbers, sep="")
