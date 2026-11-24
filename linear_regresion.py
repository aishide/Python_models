from sklearn.liner_model import LinearRegression
import numpy as np

#Data X="study hours" and y="marks"
x = np.array([ [1], [2], [3], [4], [5] ])
y = np.array([ 34, 65, 77, 88, 92 ])

model = LinearRegression()
model.fit(x, y)

print("Slope (m) : " , model.coef_[0] )
print("Intercept (c) : ", model.intercept_ )
print(" Prediction for 6 hours study is : ", model.predict ([[6]]) [0] )
