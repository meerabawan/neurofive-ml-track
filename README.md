# 🚀 NeuroFive Machine Learning Track

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-blue?logo=numpy)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-f7931e?logo=scikitlearn)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-green)
![Status](https://img.shields.io/badge/Status-Week%203%20Tasks%20Completed-success)

# 📖 Overview

This repository contains my submissions for the **NeuroFive Machine Learning Track** internship.

The projects cover the fundamentals of Machine Learning, including data exploration, data cleaning, visualization, classification, regression, model evaluation, hyperparameter tuning, and solving a real-world business problem through customer churn prediction using Python and Scikit-Learn.

# 📂 Repository Structure

```text
neurofive-ml-track
│
├── Week1
│   ├── Task1
│   └── Task2
│
├── Week2
│   ├── Task3
│   └── Task4
│
├── Week3
│   ├── Task5
│   └── Task6
│
└── README.md
```

# 📅 Week 1

## ✅ Task 1 – Titanic Dataset Exploration

### Objective

Set up the Python Data Science environment and explore the Titanic dataset to understand its structure and features.

### Workflow

- Load Titanic dataset
- Explore dataset using Pandas
- Inspect data types
- Generate descriptive statistics
- Identify missing values

### Skills Learned

- Pandas
- Data Exploration
- Dataset Inspection
- Descriptive Statistics

---

## ✅ Task 2 – Data Cleaning & Visualization

### Objective

Clean the Titanic dataset and visualize important patterns using different charts.

### Workflow

- Handle missing values
- Detect outliers
- Perform feature analysis
- Create visualizations

### Visualizations

- Histogram
- Box Plot
- Bar Chart
- Correlation Heatmap

### Skills Learned

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Visualization
- Feature Analysis

---

# 📅 Week 2

## ✅ Task 3 – Titanic Survival Prediction

### Objective

Build a Machine Learning classification model to predict passenger survival on the Titanic dataset.

### Workflow

- Data Preprocessing
- Feature Selection
- Train-Test Split
- Logistic Regression
- Model Training
- Prediction
- Accuracy Evaluation
- Confusion Matrix

### Evaluation Metrics

- Accuracy Score
- Confusion Matrix

### Skills Learned

- Classification
- Logistic Regression
- Model Training
- Model Evaluation
- Accuracy Score

---

## ✅ Task 4 – House Price Prediction using Linear Regression

### Objective

Predict California house prices using a Linear Regression model.

### Dataset

California Housing Dataset (Scikit-Learn)

### Selected Features

- MedInc
- HouseAge
- AveRooms
- AveOccup

### Workflow

- Load Dataset
- Data Exploration
- Feature Selection
- Train-Test Split
- Train Linear Regression Model
- Predict House Prices
- Evaluate Model
- Visualize Results

### Evaluation Metrics

- RMSE (Root Mean Squared Error)
- R² Score

### Results

| Metric | Value |
|---------|-------|
| RMSE | **0.8108** |
| R² Score | **0.4983** |

### Visualization

- Actual vs Predicted Scatter Plot

### Skills Learned

- Regression
- Linear Regression
- Feature Selection
- RMSE
- R² Score
- Data Visualization

---

# 📅 Week 3

## ✅ Task 5 – Model Evaluation & Hyperparameter Tuning

### Objective

Evaluate the Titanic Survival Prediction model beyond accuracy and improve it using hyperparameter tuning.

### Workflow

- Load Titanic dataset
- Data Cleaning
- Encode Categorical Features
- Train-Test Split
- Train Logistic Regression Model
- Predict Test Data
- Calculate Accuracy
- Generate Confusion Matrix
- Generate Classification Report
- Calculate Precision, Recall and F1-score
- Explain why Accuracy alone can be misleading
- Apply GridSearchCV
- Tune Logistic Regression Hyperparameters
- Compare Original and Tuned Models

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

### Hyperparameters Tuned

- C (Regularization Strength)
- Solver

### Results

| Model | Accuracy |
|--------|----------|
| Original Logistic Regression | **81.01%** |
| Tuned Logistic Regression | **78.21%** |

### Key Learning

GridSearchCV automatically searched multiple combinations of hyperparameters using cross-validation. Although the tuned model achieved slightly lower test accuracy, the experiment demonstrated that hyperparameter tuning helps identify the most suitable model configuration instead of relying on manual parameter selection.

### Skills Learned

- Model Evaluation
- Precision
- Recall
- F1-score
- Hyperparameter Tuning
- GridSearchCV
- Cross Validation
- Performance Comparison

---

## ✅ Task 6 – Customer Churn Prediction using Decision Tree & Logistic Regression

### Objective

Build a Machine Learning model to predict customer churn using the Telco Customer Churn dataset and analyze the business factors influencing customer retention.

### Dataset

Telco Customer Churn Dataset (Kaggle)

### Workflow

- Load Telco Customer Churn dataset
- Explore dataset structure
- Inspect data types
- Identify missing values
- Convert TotalCharges to numeric format
- Handle missing values
- Encode target variable
- Perform One-Hot Encoding
- Perform Exploratory Data Analysis (EDA)
- Analyze customer churn distribution
- Visualize monthly charges
- Generate correlation heatmap
- Check class imbalance
- Split dataset into training and testing sets
- Train Logistic Regression model
- Train Decision Tree Classifier
- Compare model performance
- Evaluate models using Accuracy, Precision, Recall, F1-score and Confusion Matrix
- Identify Top 3 Important Features using Decision Tree Feature Importance
- Prepare a business summary based on the findings

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

### Models Used

- Logistic Regression
- Decision Tree Classifier

### Top Features Influencing Customer Churn

- Contract Type
- Tenure
- Monthly Charges

### Business Summary

The analysis showed that customers with month-to-month contracts, shorter tenure, and higher monthly charges are more likely to churn. Logistic Regression achieved strong predictive performance, while the Decision Tree model provided clear feature importance for business interpretation. These insights can help businesses identify at-risk customers early and improve customer retention through targeted offers and long-term contract plans.

### Skills Learned

- Customer Churn Prediction
- Decision Tree Classification
- Logistic Regression
- Data Preprocessing
- One-Hot Encoding
- Exploratory Data Analysis (EDA)
- Feature Importance
- Business Analytics
- Model Comparison
- Customer Retention Analysis

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- Jupyter Notebook

---

# 📚 Learning Outcomes

Through these projects, I learned:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Visualization
- Feature Engineering
- Feature Selection
- Classification
- Regression
- Logistic Regression
- Linear Regression
- Decision Tree Classification
- Customer Churn Prediction
- Model Training
- Model Evaluation
- Accuracy Score
- Precision
- Recall
- F1-score
- Confusion Matrix
- Hyperparameter Tuning
- GridSearchCV
- Cross Validation
- One-Hot Encoding
- Feature Importance
- Business Analytics
- Customer Retention Analysis
- Model Comparison
- Machine Learning Workflow

---

# 📌 Repository Highlights

✔ Titanic Dataset Exploration

✔ Data Cleaning & Visualization

✔ Titanic Survival Prediction

✔ House Price Prediction using Linear Regression

✔ Model Evaluation Beyond Accuracy

✔ Hyperparameter Tuning using GridSearchCV

✔ Customer Churn Prediction using Machine Learning

✔ Decision Tree Classification

✔ Feature Importance Analysis

✔ Real-World Business Problem Solving

---

# 👩‍💻 Author

**Meerab Awan**

⭐ If you found this repository helpful, feel free to give it a Star.