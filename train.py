# import pandas as pd
# df = pd.read_csv("data/raw/placement_data.csv")
# print(df.head())


# print("\nShape of Dataset:")
# print(df.shape)


# print("\nColumns:")
# print(df.columns)


# print("\nDataset Information:")
# print(df.info())


# print("\nMissing Values:")
# print(df.isnull().sum())




import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset
df = pd.read_csv("data/raw/placement_data.csv")

print(df.head())

# Create graph
plt.figure(figsize=(6,4))
sns.countplot(x="Placed", data=df)
plt.title("Placement Count")
plt.show()

print ("\nCorrelation Matrix:")
print(df.corr())

plt.figure(figsize=(10,6))

sns.heatmap(
    df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"

)         

plt.title("Correlation Heatmap")
plt.show()

X =df.drop("Placed",axis=1)

y=df["Placed"]

print("Features:")
print(X.head())

print ("\nTarget:")
print(y.head())


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Data:", X_train.shape)
print("Testing Data:", X_test.shape)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X_train, y_train)

print("Model trained successfully!")

predictions = model.predict(X_test)

print("Actual Values:")
print(y_test.values)

print("\nPredicted Values:")
print(predictions)

print("Predictions:")
print(predictions)

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test,predictions)
print("\nModel Accuracy:", accuracy)



import pickle 

with open("models/placement_model.pkl","wb") as file:
    pickle.dump(model,file)
print("Model saved sucessfully")    