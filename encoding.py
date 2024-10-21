import pandas as pd
import numpy as np

# Step 1: Create a DataFrame
data = {'Category': ['Low', 'Medium', 'High', 'Medium', 'Low', 'High']}
df = pd.DataFrame(data)

# Step 2: Define a mapping for ordinal encoding
ordinal_mapping = {'Low': 1, 'Medium': 2, 'High': 3}

# Step 3: Apply the mapping using Pandas' `map` function
df['Category_Encoded'] = df['Category'].map(ordinal_mapping)

# Step 4: Display the DataFrame with the encoded column
print(df)


# Step 1: Create a DataFrame with categorical values
data = {'Category': ['Low', 'Medium', 'High', 'Medium', 'Low', 'High']}
df = pd.DataFrame(data)

# Step 2: Perform One-Hot Encoding using pandas' get_dummies function
one_hot_encoded = pd.get_dummies(df['Category'], prefix='Category')

# Step 3: Concatenate the original DataFrame with the one-hot encoded DataFrame
df_one_hot = pd.concat([df, one_hot_encoded], axis=1)

# Step 4: Drop the original 'Category' column if needed
df_one_hot.drop('Category', axis=1, inplace=True)

# Step 5: Display the DataFrame with one-hot encoded columns
print(df_one_hot)
