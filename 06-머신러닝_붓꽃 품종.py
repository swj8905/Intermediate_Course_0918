from sklearn.svm import SVC
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv("./iris.csv")
label = df["variety"]
data = df[["sepal.length", "sepal.width", "petal.length", "petal.width"]]
train_data, valid_data, train_label, valid_label = train_test_split(data, label)

model = SVC() # Support Vector Machine Classifier
model.fit(train_data, train_label) # 학습시키기

# 검증하기
result = model.predict(valid_data)
score = accuracy_score(result, valid_label)
print(score)
