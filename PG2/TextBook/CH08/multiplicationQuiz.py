import random
import time

import pyinputplus as pyip

number_of_questions = 5
correct_answers = 0
for question_number in range(number_of_questions):

    num1 = random.randint(11, 99)
    num2 = random.randint(11, 99)
    prompt = f'#{question_number}: {num1} + {num2} = '

    try:
        # 正解は allowRegexes で処理する
        # 不正解は blockRegexes で処理され、カスタムメッセージが表示される
        pyip.inputStr(
            prompt,
            allowRegexes=[f'^{num1 + num2}$'],
            blockRegexes=[('.*', '残念!')],
            timeout=10,
            limit=3
        )
    except pyip.TimeoutException:
        print('時間切れです!')
    except pyip.RetryLimitException:
        print('所定の回数を超えました!')
    else:
        # try ブロックで例外が発生しなかった場合に実行
        print('正解!')
        correct_answers += 1
    time.sleep(1)