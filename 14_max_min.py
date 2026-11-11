print("5つの実数を入力してください。")

values = []
for i in range(1, 6):
	values.append(float(input(f"{i}つ目の値：")))

maximum = values[0]
minimum = values[0]

for value in values[1:]:
	if value > maximum:
		maximum = value
	if value < minimum:
		minimum = value

print(f"最大値：{maximum}")
print(f"最小値：{minimum}")
