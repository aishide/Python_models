import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 1. One-Hot Encoding
df = pd.DataFrame({'city': ['NY', 'LA', 'NY', 'SF']})
df_encoded = pd.get_dummies(df, columns=['city'])
print(df_encoded)

# 2. Label Encoding
departments = ["IT", "HR", "Finance", "IT", "Finance"]
encoder = LabelEncoder()
encoded = encoder.fit_transform(departments)
print("Encoded:", encoded)          # [2 1 0 2 0]
print("Classes:", encoder.classes_) # ['Finance' 'HR' 'IT']
