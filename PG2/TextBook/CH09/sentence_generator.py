import pyinputplus as pyip


def change_text(adjective, noun, verb, adverb, file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        placeholders = {'ADJECTIVE': adjective, 'NOUN': noun, 'VERB': verb, 'ADVERB': adverb}
        for placeholder, replacement in placeholders.items():
            content = content.replace(placeholder, replacement)
    with open(file_path, 'w') as f:
        f.write(content)


def main():
    file_path = 'file_name.txt'
    prompts = {
        '形容詞を入力してください: ': 'adjective',
        '名詞を入力してください: ': 'noun',
        '動詞を入力してください: ': 'verb',
        '副詞を入力してください: ': 'adverb'
    }
    user_inputs = {key: pyip.inputStr(prompt) for prompt, key in prompts.items()}
    change_text(**user_inputs, file_path=file_path)


if __name__ == '__main__':
    main()