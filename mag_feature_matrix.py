import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# Example data (replace this with your dataset)
data = {
}

# Separate features and target
X = pd.DataFrame(data, columns=['numeric_feature', 'categorical_feature'])
y = data['target']

# Define preprocessing steps
numeric_features = ['numeric_feature']
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_features = ['categorical_feature']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Apply preprocessing to features
X_preprocessed = preprocessor.fit_transform(X)

# Convert the preprocessed array back to a DataFrame for better visualization
columns = numeric_features + preprocessor.transformers_[1][1]['onehot'].get_feature_names_out(categorical_features).tolist()
X_preprocessed_df = pd.DataFrame(X_preprocessed, columns=columns)

# Concatenate with the target variable
result_df = pd.concat([X_preprocessed_df, pd.DataFrame({'target': y})], axis=1)

print(f"\n\n\n{result_df}\n\n\n")
