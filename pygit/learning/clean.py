import pandas as pd


df = pd.read_csv('all_issues.csv', on_bad_lines='skip')


print("Original Data Size:", len(df))
print(df.head()) # Print top 5 rows

# Cleaning
# Drop rows where 'body' is missing (NaN)
df = df.dropna(subset=['body'])

#  Encode Labels to Numbers
# Apply a simple function: If label is 'good first issue', make it 1. Else 0.
df['label_code'] = df['label'].apply(lambda x: 1 if x == 'good first issue' else 0)

print("\nCleaned Data Size:", len(df))
print(df[['label', 'label_code']].head()) # Check if the conversion worked
