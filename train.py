import os
import numpy as np
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input


# Load InceptionV3
model = InceptionV3(
    weights="imagenet",
    include_top=False,
    pooling="avg"
)

DATASET_PATH = "dataset"
classes = ["organic", "plastic", "paper", "metal"]

X = []  # features
y = []  # labels

print("Extracting features...")

for label, cls in enumerate(classes):
    folder = os.path.join(DATASET_PATH, cls)
    for file in os.listdir(folder):
        img_path = os.path.join(folder, file)

        # Load and preprocess image
        img = image.load_img(img_path, target_size=(299, 299))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        # Extract features
        features = model.predict(img_array, verbose=0)
        X.append(features.flatten())
        y.append(label)

print("Feature extraction complete")
print("Total samples:", len(X))
print("Feature size:", X[0].shape)

from sklearn.model_selection import train_test_split

# Convert to NumPy arrays
X = np.array(X)
y = np.array(y)

print("X shape:", X.shape)
print("y shape:", y.shape)

# Train-test split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

print("\nTraining SVM model...")

# Create SVM model
svm_model = SVC(kernel="rbf", probability=True)

# Train
svm_model.fit(X_train, y_train)

# Predict
y_pred = svm_model.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, y_pred)
print("SVM Accuracy:", acc)

from sklearn.metrics import classification_report

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=["organic", "plastic", "paper", "metal"]
))

from sklearn.ensemble import RandomForestClassifier

print("\nTraining Random Forest model...")

rf_model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    class_weight="balanced"
)

rf_model.fit(X_train, y_train)

y_pred_rf = rf_model.predict(X_test)

acc_rf = accuracy_score(y_test, y_pred_rf)
print("Random Forest Accuracy:", acc_rf)

print("\nRandom Forest Classification Report:")
print(classification_report(
    y_test,
    y_pred_rf,
    target_names=["organic", "plastic", "paper", "metal"]
))

from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Confusion Matrix (SVM)
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["organic", "plastic", "paper", "metal"],
    yticklabels=["organic", "plastic", "paper", "metal"]
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - SVM")
plt.show()

import pickle

# Create models folder if it doesn't exist
os.makedirs("models", exist_ok=True)

# Save trained SVM model
with open("models/svm_model.pkl", "wb") as f:
    pickle.dump(svm_model, f)

print("SVM model saved successfully")

# Save class labels
class_names = ["organic", "plastic", "paper", "metal"]

with open("models/class_names.pkl", "wb") as f:
    pickle.dump(class_names, f)

print("Class names saved successfully")

# Save the scaler
with open("models/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("Scaler saved successfully")

import matplotlib.pyplot as plt

models = ["SVM", "Random Forest"]
accuracies = [0.953, 0.907]   # your final K=2048 values

plt.figure(figsize=(6, 4))
plt.bar(models, accuracies)
plt.ylim(0.85, 1.0)

plt.xlabel("Classifier")
plt.ylabel("Accuracy")
plt.title("Accuracy Comparison of ML Models using InceptionV3 Features")

for i, v in enumerate(accuracies):
    plt.text(i, v + 0.005, f"{v:.3f}", ha="center")

# THIS LINE forces a popup window
plt.show(block=True)
plt.savefig("fig6_accuracy_comparison.png", dpi=300, bbox_inches="tight")
print("Accuracy comparison chart saved as fig6_accuracy_comparison.png")

import matplotlib.pyplot as plt

models = ["SVM", "Random Forest"]
accuracies = [0.953, 0.907]

print(models)
print(accuracies)

plt.figure(figsize=(6, 4))
plt.bar(models, accuracies)

plt.ylim(0.85, 1.0)
plt.xlabel("Classifier")
plt.ylabel("Accuracy")
plt.title("Accuracy Comparison of ML Models using InceptionV3 Features")

for i, v in enumerate(accuracies):
    plt.text(i, v + 0.005, f"{v:.3f}", ha="center")

plt.show(block=True)
print("Scaler saved successfully")

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix (SVM):")
print(cm)