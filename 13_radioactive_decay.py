initial_activity = 740
half_life = 6

for time in range(0, 25, 3):
	activity = initial_activity * (1 / 2) ** (time / half_life)
	print(f"{time}時間後：{activity:.1f} MBq")
