df = pd.DataFrame({'date': pd.to_datetime(['2025-01-01', '2025-01-02', '2025-01-03'])})
df['day'] = df['date'].dt.day
df['weekday'] = df['date'].dt.weekday  # 0 = Monday, 6 = Sunday
