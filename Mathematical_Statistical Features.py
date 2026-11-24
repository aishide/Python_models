import pandas as pd

df = pd.DataFrame ({
  'price' : [200000, 150000, 300000],
  'sqft' : [1000, 800, 15000]
})

df['price_per_sqft'] = df['price'] / df['sqft']
print(df)
