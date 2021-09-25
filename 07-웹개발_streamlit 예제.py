import streamlit as st

st.text("일반 텍스트입니다.")
st.text("아무말이나 써볼게요.")
st.text("코드 수정할 때마다")
st.text("저장 단축키 눌러보시면")
st.text("수정 사항이 웹페이지에 바로 반영이 됩니다.")

st.write("---")
st.write("이렇게도 됩니다.")
st.write("# 이렇게도 됩니다.")
st.write("## 이렇게도 됩니다.")
st.write("### 이렇게도 됩니다.")
st.write("#### 이렇게도 됩니다.")
st.write("##### 이렇게도 됩니다.")
st.write("###### 이렇게도 됩니다.")

st.write("> 이렇게도 됩니다.")
st.write(">> 이렇게도 됩니다.")
st.write(">>> 이렇게도 됩니다.")

st.write("https://www.naver.com")

foo = {"짜장면":5000, "짬뽕":6000, "탕수육":10000}
st.write(foo)

st.write(1234)

st.code("print('Hello World')")

st.write("---")

"그냥 이렇게만 해도 됩니다."

"""
# 매직 커맨드
---
> 표를 띄우고 싶으면, 코드에 표를 그리면 됩니다.

|          |  수학    |    국어    |
|----------|:---------:|:----------:|
|철수      | 90 (Good)|  100 (Good)|
|영희      | 30 (Bad) |  40 (Bad)  |

https://www.naver.com

```python
print("Hello World")
```
"""
