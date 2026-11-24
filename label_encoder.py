import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Label Encoding
departments = ["IT", "HR", "Finance", "IT", "Finance"]
encoder = LabelEncoder()
encoded = encoder.fit_transform(departments)
print("Encoded:", encoded)          # [2 1 0 2 0]
print("Classes:", encoder.classes_) # ['Finance' 'HR' 'IT']
