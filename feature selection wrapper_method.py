from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

X = [[1, 2, 10], [2, 3, 20], [3, 4, 30], [4, 5, 40]]
y = [0, 0, 1, 1]

model = LogisticRegression()
rfe = RFE(estimator=model, n_features_to_select=2)
X_selected = rfe.fit_transform(X, y)
print("Selected Features Mask:", rfe.support_)
