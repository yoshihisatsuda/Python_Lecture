#タプルの作成
data = ("John", "Doe", 53.44)
#タプルの内容を出力　%が演算子、sが文字列型変数の出力、dが整数型変数の出力、fが浮動小数点型変数の出力
format_string = "Hello %s %s. Your current balance is $%s."

#ここで%s(プレースホルダー)の値を設定
print(format_string % data)