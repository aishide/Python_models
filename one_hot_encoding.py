import pandas as pd
from sklearn.preprocessing import LabelEncoder

# One-Hot Encoding
df = pd.DataFrame({'city': ['NY', 'LA', 'NY', 'SF']})
df_encoded = pd.get_dummies(df, columns=['city'])
print(df_encoded)
