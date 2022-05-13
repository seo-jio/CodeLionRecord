from googletrans import Translator

translator = Translator()
sentence = input("번역할 문장을 입력해주세요: ")
dst = input("어떤 언어로 번역을 원하시나요? ")
detected = translator.detect(sentence)
trans = translator.translate(sentence, dst)

print("=========출력 결과========")
print(detected.lang,":",sentence)
print(trans.dest,":",trans.text)
print("========================")