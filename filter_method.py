import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif, chi2, mutual_info_classif

# 1. Correlation (Numeric vs Numeric)
df_num = pd.DataFrame({
    "age": [20, 22, 25, 30, 35],
    "salary": [20000, 22000, 25000, 28000, 35000],
    "purchases": [1, 2, 3, 4, 5]
})
print(df_num.corr()["purchases"].drop("purchases"))

# 2. ANOVA F-test (Numeric features vs Categorical target)
df_anova = pd.DataFrame({
    "math_score": [80, 60, 90, 50, 70],
    "science_score": [75, 55, 95, 45, 68],
    "passed": [1, 0, 1, 0, 1]
})
f_vals, p_vals = f_classif(df_anova[["math_score", "science_score"]], df_anova["passed"])
print("F-values:", f_vals)

# 3. Mutual Information (Classification)
X_cat = pd.DataFrame({"gender": [0, 1, 0, 1], "owns_car": [1, 1, 0, 0]})
y_cat = [1, 1, 0, 0]
mi_scores = mutual_info_classif(X_cat, y_cat, discrete_features=True)
print("MI Scores:", mi_scores)
