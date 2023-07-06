# NumPy 라이브러리를 가져옵니다. NumPy는 파이썬에서 수치 계산을 수행하기 위한 라이브러리입니다.
import numpy as np
# scikit-learn 라이브러리에서 LinearRegression 클래스를 가져옵니다. LinearRegression은 선형 회귀 모델을 구축하는 데 사용됩니다.
from sklearn.linear_model import LinearRegression

# 독립 변수 X를 정의합니다. 2차원 NumPy 배열로 구성되어 있으며, 이 경우에는 1차원의 값을 가진 5개의 데이터 포인트가 있습니다.
X = np.array([[30], [40], [50], [60], [70]])
# 종속 변수 y를 정의합니다. 1차원 NumPy 배열로 구성되어 있으며, X와 대응하는 5개의 결과 값입니다.
y = np.array([100, 150, 200, 250, 300])
# LinearRegression 클래스의 인스턴스를 생성하여 모델 객체를 만듭니다.
model = LinearRegression()
# X와 y 데이터를 사용하여 선형 회귀 모델을 훈련시킵니다. 즉, 주어진 데이터에 맞게 모델을 학습시킵니다.
model.fit(X, y)

size = int(input("주택평수입력?"))
# 예측할 새로운 데이터 포인트를 정의합니다. 이 경우에는 2차원 NumPy 배열로 구성되어 있으며, 하나의 값을 가지고 있습니다.
house_size = np.array([[size]])
# 학습된 모델을 사용하여 new_data에 대한 예측을 수행합니다. predict 메서드는 주어진 입력에 대한 예측 값을 반환합니다.
predict_price = model.predict(house_size)
print(predict_price)
    