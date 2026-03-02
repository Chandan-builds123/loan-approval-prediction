# 🏦 LoanIQ — Smart Loan Approval Prediction (Full ML Demonstration System)

LoanIQ is an end-to-end Machine Learning Web Application that predicts whether a loan application will be approved or rejected based on applicant details.

The model is built using a Random Forest Classifier and deployed using Flask with an interactive user interface.

---

## 🚀 How to Run

### Step 1 — Install dependencies

pip install flask scikit-learn pandas numpy

---

### Step 2 — Train the model (do this ONCE)

python train_model.py

This creates:
- model.pkl

---

### Step 3 — Start the Flask app

python app.py

---

### Step 4 — Open in browser

Main UI:
http://127.0.0.1:5000/

---

## 📁 Project Structure

loan_approval_prediction/
│
├── app.py                 ← Flask backend
├── train_model.ipynb      ← ML training notebook
├── train.csv              ← Loan dataset
├── model.pkl              ← Trained Random Forest model
├── requirements.txt
├── templates/
│   └── index.html         ← Prediction UI
└── venv/

---

## 🎯 Model Performance

Algorithm: Random Forest Classifier  
Models Compared: 7 ML Algorithms  
Best Accuracy: ~80% (Random Forest)  
Evaluation Metric: Accuracy Score  
Features Used: 10 key applicant features  

Models Evaluated:
- Logistic Regression  
- Decision Tree  
- Random Forest ⭐ (Best Performer)  
- KNN  
- SVM  
- Naive Bayes  
- Gradient Boosting  

---

## 📊 Input Features

The model predicts approval using:

- Gender  
- Marital Status  
- Dependents  
- Education  
- Self Employed  
- Credit History  
- Property Area  
- Loan Amount Term  
- Loan Amount  
- Total Monthly Income  

---

## 🧠 ML Pipeline Overview

1. Data Cleaning  
2. Missing Value Handling  
3. Label Encoding  
4. Feature Selection  
5. Train/Test Split  
6. Model Training (7 algorithms)  
7. Cross Validation  
8. Final Model Selection (Random Forest)  
9. Model Serialization using pickle  

---

## 💡 Application Features

- Real-time loan prediction  
- Confidence score display  
- Feature importance visualization  
- Loan-to-Income ratio calculation  
- Smart improvement suggestions  
- Interactive UI  
- Educational ML demonstration  

---

## 🛠 Technologies Used

- Python  
- Flask  
- Scikit-learn  
- NumPy  
- Pandas  
- HTML / CSS / JavaScript  
- Random Forest  

---

## 📈 Future Improvements

- Deploy on Render / Railway  
- Add User Authentication  
- Store Predictions in Database  
- Add SHAP Explainability  
- Add Admin Dashboard  
- Improve Model Accuracy  

---

## 👥 Team

This project was collaboratively developed as part of an academic group project.

---

## 📜 License

This project is licensed under the MIT License.