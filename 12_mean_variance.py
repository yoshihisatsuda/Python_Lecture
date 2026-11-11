print("5つの実数を入力してください。")

values = []
for i in range(5):
	value = float(input(f"{i + 1}つ目の値："))
	values.append(value)

total = 0
for value in values:
	total += value
mean = total / 5

squared_deviation_total = 0
for value in values:
	squared_deviation_total += (value - mean) ** 2
variance = squared_deviation_total / 5

print(f"平均値：{mean}")
print(f"分散：{variance}")

