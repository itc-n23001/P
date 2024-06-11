import random
guess = ''
while guess not in ('表', '裏'):
    print('コインの表裏を当てて下さい。表か裏を入力して下さい:')
    guess = input()
toss = random.randint(0, 1)
if toss == guess:
    print('当たり！')
else:
    print('はずれ！もう一回当てて！')
    guess = input()
    if toss == guess:
        print('当たり！')
    else:
        print('はずれ。このゲームは苦手ですね。')