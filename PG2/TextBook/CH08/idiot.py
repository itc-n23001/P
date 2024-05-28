import pyinputplus as pyip
while True:
    prompt = 'バカを何時間も忙しくさせておく方法をしりたいですか？\n'
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        break
    print('ありがとう、ごきげんよう')
    response = pyip.inputYesNo(prompt, yesVal='はい', noVal='いいえ')
    if response == 'いいえ':
        break