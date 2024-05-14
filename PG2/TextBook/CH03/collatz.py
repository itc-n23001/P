def collatz(number):
    sequence = [number]
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        sequence.append(number)
    return sequence

# 例として、整数を指定して実行してみます
starting_number = 3
result_sequence = collatz(starting_number)

print(f"コラッツの数列 ({starting_number} から開始): {result_sequence}")