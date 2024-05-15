spam = ['apples', 'bananas', 'tofu', 'cats']

# 'and' を追加した文字列を作成
output = ', '.join(spam[:-1]) + ', and ' + spam[-1]
print(output)