# Credit Risk Modeling Using Machine Learning

## Project Overview

This project predicts whether a loan applicant is likely to default on a loan using Machine Learning techniques. The objective is to assist financial institutions in assessing credit risk and making informed lending decisions.

The project includes data preprocessing, exploratory data analysis (EDA), feature engineering, model training, evaluation, and deployment using Streamlit.


## Dataset

The dataset contains information about loan applicants, including personal, financial, and credit history details.

### Features

- person_age
- person_income
- person_home_ownership
- person_emp_length
- loan_intent
- loan_grade
- loan_amnt
- loan_int_rate
- loan_percent_income
- cb_person_default_on_file
- cb_person_cred_hist_length

### Target Variable

- loan_status
  - 0 = No Default
  - 1 = Default


## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook


## Project Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Data Preprocessing
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Model Saving
10. Streamlit Deployment


## Machine Learning Model

- Logistic Regression
  

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix
- Classification Report


## Project Structure

```
Credit-Risk-Model/

│
├── data/
│   └── credit_risk_dataset.csv
│
├── notebooks/
│   └── Credit_Risk_Model.ipynb
│
├── models/
│   └── credit_risk_model.pkl
│
├── app.py
├── README.md
├── requirements.txt
└── images/
```


## Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project directory

```bash
cd Credit-Risk-Model
```

Install the required packages

```bash
pip install -r requirements.txt
```

---

## Run the Jupyter Notebook

```bash
jupyter notebook
```

Open:

```
Credit_Risk_Model.ipynb
```

Run all cells in order.

---

## Run the Streamlit Application

```bash
streamlit run app.py
```

---

## Results

The Logistic Regression model predicts whether a borrower is likely to default based on the applicant's financial and credit information.

The model is evaluated using multiple classification metrics to measure its performance.


## Future Improvements

- Random Forest Classifier
- LightGBM Model
- Hyperparameter Tuning
- Cross Validation
- SHAP Explainability
- Feature Importance Analysis
- Cloud Deployment


## Author

Shivam Kumar

B.Tech (Artificial Intelligence and Data Science)


## License

This project is developed for educational and learning purposes.
