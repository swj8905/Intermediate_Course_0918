from konlpy.tag import Okt

okt = Okt() # Okt 분석기를 사용하겠다.
# result = okt.pos("안녕하세요. 저는 파이썬 공부를 하고 있습니다.")
# print(result)
result = okt.nouns("이런 것도 분석할 수 있냨ㅋㅋㅋㅋㅋ")
print(result)