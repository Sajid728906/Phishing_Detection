import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

print("Step1: Loading Dataset...")
df = pd.read_csv("Phising_dataset_predict.csv")

df = df.dropna(subset=['Phising'])

x = df.drop(columns=['Phising']).fillna(0)
y = df['Phising'].values

print("Step2: Spliting Data (80% Train, 20% Test)....")
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print("Step3: Training Random Forest (For 95% Accuracy)..")
model = RandomForestClassifier(n_estimators=100, max_depth=15, random_state=42)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

plt.figure(figsize=(6,4))
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Safe', 'Phising'], yticklabels=['Safe', 'Phising'])
plt.ylabel('Actual Classes')
plt.xlabel('Predicted Classes')
plt.title('Cyber Security - Confusion matrix')
plt.savefig('Accuracy_graph.png')
print("Graph image saved as 'Accuracy_graph.png'")

with open('cyber_phising_model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("Model saved successfully as 'cyber_phising_model.pkl'")
