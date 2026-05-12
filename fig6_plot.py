import matplotlib.pyplot as plt

models = ["SVM", "Random Forest"]
accuracies = [0.953, 0.907]

plt.figure(figsize=(6, 4))
plt.bar(models, accuracies)
plt.ylim(0.85, 1.0)

plt.xlabel("Classifier")
plt.ylabel("Accuracy")
plt.title("Accuracy Comparison of ML Models using InceptionV3 Features")

for i, v in enumerate(accuracies):
    plt.text(i, v + 0.005, f"{v:.3f}", ha="center")

plt.show()
