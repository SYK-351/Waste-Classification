# Waste Classification System using Machine Learning

## Overview

This project is a machine learning-based waste classification system that classifies waste images into different categories such as:

- Organic
- Plastic
- Paper
- Metal

The system uses image feature extraction techniques along with machine learning models to automate waste segregation and improve recycling efficiency.

---

## Features

- Waste image classification
- Feature extraction using deep learning features
- Multiple machine learning model comparison
- Accuracy evaluation and visualization
- Confusion matrix generation
- Model and scaler saving for future predictions

---

## Technologies Used
# Waste Classification System using Machine Learning

## Overview

This project is a machine learning-based waste classification system that classifies waste images into different categories such as:

- Organic
- Plastic
- Paper
- Metal

The system uses image feature extraction techniques along with machine learning models to automate waste segregation and improve recycling efficiency.

---

## Features

- Waste image classification
- Feature extraction using deep learning features
- Multiple machine learning model comparison
- Accuracy evaluation and visualization
- Confusion matrix generation
- Model and scaler saving for future predictions

---

## Technologies Used

- Python
- TensorFlow / Keras
- Scikit-learn
- NumPy
- Matplotlib
- OpenCV

---

## Project Structure

```text
Waste-classification/
│
├── app.py
├── train.py
├── requirements.txt
├── .gitignore
├── fig6_plot.py
├── fig7_confusion_matrix.py
├── fig6_accuracy_comparison.png
├── dataset/
├── models/
└── README.md
```

---

## Dataset

The dataset contains images of different waste categories:

- Organic
- Plastic
- Paper
- Metal

The images are preprocessed before feature extraction and training.

---

## Machine Learning Models Used

### 1. Support Vector Machine (SVM)

- Accuracy: **95.31%**

### 2. Random Forest

- Accuracy: **90.77%**

---

## Model Performance

### SVM Classification Report

```text
              precision    recall  f1-score   support

     organic       0.98      0.96      0.97       135
     plastic       0.94      0.95      0.94       182
       paper       0.95      0.96      0.95       214
       metal       0.95      0.94      0.95       173

    accuracy                           0.95       704
   macro avg       0.96      0.95      0.95       704
weighted avg       0.95      0.95      0.95       704
```

---

### Random Forest Classification Report

```text
              precision    recall  f1-score   support

     organic       0.97      0.95      0.96       135
     plastic       0.88      0.88      0.88       182
       paper       0.88      0.97      0.92       214
       metal       0.93      0.83      0.87       173

    accuracy                           0.91       704
   macro avg       0.91      0.91      0.91       704
weighted avg       0.91      0.91      0.91       704
```

---

## Confusion Matrix (SVM)

```text
[[130   1   3   1]
 [  1 173   5   3]
 [  1   4 205   4]
 [  0   7   3 163]]
```

---

## Accuracy Comparison

| Model | Accuracy |
|------|------|
| SVM | 95.31% |
| Random Forest | 90.77% |

---

## Installation

### Clone Repository

```bash
git clone <your-repository-link>
cd Waste-classification
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

#### Windows

```bash
.\.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Project

### Train Model

```bash
python train.py
```

### Run Application

```bash
python app.py
```

---

## Outputs Generated

- Trained SVM model
- Random Forest model
- Accuracy comparison graph
- Confusion matrix
- Saved scaler and class labels

---

## Future Improvements

- Add real-time webcam waste detection
- Deploy using Flask or Streamlit
- Improve dataset size and diversity
- Add more waste categories
- Use deep learning CNN models directly for classification

---

## Conclusion

This project demonstrates the use of machine learning and image processing techniques for intelligent waste classification. The SVM model achieved the best performance with an accuracy of 95.31%, showing strong potential for automated waste management systems.
- Python
- TensorFlow / Keras
- Scikit-learn
- NumPy
- Matplotlib
- OpenCV

---

## Project Structure

```text
Waste-classification/
│
├── app.py
├── train.py
├── requirements.txt
├── .gitignore
├── fig6_plot.py
├── fig7_confusion_matrix.py
├── fig6_accuracy_comparison.png
├── dataset/
├── models/
└── README.md
```

---

## Dataset

The dataset contains images of different waste categories:

- Organic
- Plastic
- Paper
- Metal

The images are preprocessed before feature extraction and training.

---

## Machine Learning Models Used

### 1. Support Vector Machine (SVM)

- Accuracy: **95.31%**

### 2. Random Forest

- Accuracy: **90.77%**

---

## Model Performance

### SVM Classification Report

```text
              precision    recall  f1-score   support

     organic       0.98      0.96      0.97       135
     plastic       0.94      0.95      0.94       182
       paper       0.95      0.96      0.95       214
       metal       0.95      0.94      0.95       173

    accuracy                           0.95       704
   macro avg       0.96      0.95      0.95       704
weighted avg       0.95      0.95      0.95       704
```

---

### Random Forest Classification Report

```text
              precision    recall  f1-score   support

     organic       0.97      0.95      0.96       135
     plastic       0.88      0.88      0.88       182
       paper       0.88      0.97      0.92       214
       metal       0.93      0.83      0.87       173

    accuracy                           0.91       704
   macro avg       0.91      0.91      0.91       704
weighted avg       0.91      0.91      0.91       704
```

---

## Confusion Matrix (SVM)

```text
[[130   1   3   1]
 [  1 173   5   3]
 [  1   4 205   4]
 [  0   7   3 163]]
```

---

## Accuracy Comparison

| Model | Accuracy |
|------|------|
| SVM | 95.31% |
| Random Forest | 90.77% |

---

## Installation

### Clone Repository

```bash
git clone <your-repository-link>
cd Waste-classification
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

#### Windows

```bash
.\.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Project

### Train Model

```bash
python train.py
```

### Run Application

```bash
python app.py
```

---

## Outputs Generated

- Trained SVM model
- Random Forest model
- Accuracy comparison graph
- Confusion matrix
- Saved scaler and class labels

---

## Future Improvements

- Add real-time webcam waste detection
- Deploy using Flask or Streamlit
- Improve dataset size and diversity
- Add more waste categories
- Use deep learning CNN models directly for classification

---

## Conclusion

This project demonstrates the use of machine learning and image processing techniques for intelligent waste classification. The SVM model achieved the best performance with an accuracy of 95.31%, showing strong potential for automated waste management systems.