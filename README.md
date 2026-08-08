# Waste Classification using Inception V3 + SVM

Image-based waste classification system using deep feature extraction (Inception V3) and SVM classifier. Trained on TacoTrash and TrashNet datasets.

---

## Models & Results

| Model | Accuracy |
|-------|----------|
| SVM | **95.31%** |
| Random Forest | 90.77% |

---

## Tech Stack

`Python` `TensorFlow/Keras` `Scikit-learn` `OpenCV` `NumPy` `Matplotlib`

---

## Project Structure

```
Waste-classification/
├── train.py                      # Training pipeline
├── app.py                        # Inference app
├── fig6_plot.py                  # Accuracy comparison plot
├── fig7_confusion_matrix.py      # Confusion matrix
├── fig6_accuracy_comparison.png  # Output graph
├── requirements.txt
├── dataset/
└── models/
```

---

## Setup & Run

```bash
git clone https://github.com/SYK-351/Waste-Classification.git
cd Waste-classification
python -m venv .venv
.\.venv\Scripts\activate        # Windows
pip install -r requirements.txt

python train.py   # Train model
python app.py     # Run app
```

---

## Future Scope

- Real-time webcam detection
- Streamlit deployment
- Direct CNN classification (no SVM)
- Expand waste categories
