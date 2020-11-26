from googletrans import Translator

translator = Translator()
with open("text_4.txt", "r", encoding="utf-8") as f:
    content = f.read()
    result = translator.translate(content, dest='ru', src='en')

with open("text_4_1.txt", "w", encoding="utf-8") as f:
    f.writelines(result.text)
