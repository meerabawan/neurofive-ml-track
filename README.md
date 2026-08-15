# 🚀 NeuroFive Machine Learning Track

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-blue?logo=numpy)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-f7931e?logo=scikitlearn)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-green)
![Joblib](https://img.shields.io/badge/Joblib-Model%20Serialization-blue)
![XGBoost](https://img.shields.io/badge/XGBoost-Ensemble%20Learning-red)

# 📖 Overview

This repository contains my submissions for the **NeuroFive Machine Learning Track** internship.

The projects cover the fundamentals of Machine Learning, including data exploration, data cleaning, visualization, classification, regression, model evaluation, hyperparameter tuning, feature engineering, machine learning pipelines, ensemble learning, and solving a real-world business problem through customer churn prediction using Python and Scikit-Learn.

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
├── Week4
│   ├── Task7
│   └── Task8
│
└── README.md
```

# 📅 Week 1

## ✅ Task 1 – Titanic Dataset Exploration

### Objective

Set up the Python Data Science environment and explore the Titanic dataset to understand its structure and features.

### Workflow

* Load Titanic dataset
* Explore dataset using Pandas
* Inspect data types
* Generate descriptive statistics
* Identify missing values

### Skills Learned

* Pandas
* Data Exploration
* Dataset Inspection
* Descriptive Statistics

---

## ✅ Task 2 – Data Cleaning & Visualization

### Objective

Clean the Titanic dataset and visualize important patterns using different charts.

### Workflow

* Handle missing values
* Detect outliers
* Perform feature analysis
* Create visualizations

### Visualizations

* Histogram
* Box Plot
* Bar Chart
* Correlation Heatmap

### Skills Learned

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Data Visualization
* Feature Analysis

---

# 📅 Week 2

## ✅ Task 3 – Titanic Survival Prediction

### Objective

Build a Machine Learning classification model to predict passenger survival on the Titanic dataset.

### Workflow

* Data Preprocessing
* Feature Selection
* Train-Test Split
* Logistic Regression
* Model Training
* Prediction
* Accuracy Evaluation
* Confusion Matrix

### Evaluation Metrics

* Accuracy Score
* Confusion Matrix

### Skills Learned

* Classification
* Logistic Regression
* Model Training
* Model Evaluation
* Accuracy Score

---

## ✅ Task 4 – House Price Prediction using Linear Regression

### Objective

Predict California house prices using a Linear Regression model.

### Dataset

California Housing Dataset (Scikit-Learn)

### Selected Features

* MedInc
* HouseAge
* AveRooms
* AveOccup

### Workflow

* Load Dataset
* Data Exploration
* Feature Selection
* Train-Test Split
* Train Linear Regression Model
* Predict House Prices
* Evaluate Model
* Visualize Results

### Evaluation Metrics

* RMSE (Root Mean Squared Error)
* R² Score

### Results

| Metric   | Value      |
| -------- | ---------- |
| RMSE     | **0.8108** |
| R² Score | **0.4983** |

### Visualization

* Actual vs Predicted Scatter Plot

### Skills Learned

* Regression
* Linear Regression
* Feature Selection
* RMSE
* R² Score
* Data Visualization

---

# 📅 Week 3

## ✅ Task 5 – Model Evaluation & Hyperparameter Tuning

### Objective

Evaluate the Titanic Survival Prediction model beyond accuracy and improve it using hyperparameter tuning.

### Workflow

* Load Titanic dataset
* Data Cleaning
* Encode Categorical Features
* Train-Test Split
* Train Logistic Regression Model
* Predict Test Data
* Calculate Accuracy
* Generate Confusion Matrix
* Generate Classification Report
* Calculate Precision, Recall and F1-score
* Explain why Accuracy alone can be misleading
* Apply GridSearchCV
* Tune Logistic Regression Hyperparameters
* Compare Original and Tuned Models

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

### Hyperparameters Tuned

* C (Regularization Strength)
* Solver

### Results

| Model                        | Accuracy   |
| ---------------------------- | ---------- |
| Original Logistic Regression | **81.01%** |
| Tuned Logistic Regression    | **78.21%** |

### Key Learning

GridSearchCV automatically searched multiple combinations of hyperparameters using cross-validation. Although the tuned model achieved slightly lower test accuracy, the experiment demonstrated that hyperparameter tuning helps identify the most suitable model configuration instead of relying on manual parameter selection.

### Skills Learned

* Model Evaluation
* Precision
* Recall
* F1-score
* Hyperparameter Tuning
* GridSearchCV
* Cross Validation
* Performance Comparison

---

## ✅ Task 6 – Customer Churn Prediction using Decision Tree & Logistic Regression

### Objective

Build a Machine Learning model to predict customer churn using the Telco Customer Churn dataset and analyze the business factors influencing customer retention.

### Dataset

Telco Customer Churn Dataset (Kaggle)

### Workflow

* Load Telco Customer Churn dataset
* Explore dataset structure
* Inspect data types
* Identify missing values
* Convert TotalCharges to numeric format
* Handle missing values
* Encode target variable
* Perform One-Hot Encoding
* Perform Exploratory Data Analysis (EDA)
* Analyze customer churn distribution
* Visualize monthly charges
* Generate correlation heatmap
* Check class imbalance
* Split dataset into training and testing sets
* Train Logistic Regression model
* Train Decision Tree Classifier
* Compare model performance
* Evaluate models using Accuracy, Precision, Recall, F1-score and Confusion Matrix
* Identify Top 3 Important Features using Decision Tree Feature Importance
* Prepare a business summary based on the findings

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

### Models Used

* Logistic Regression
* Decision Tree Classifier

### Top Features Influencing Customer Churn

* Contract Type
* Tenure
* Monthly Charges

### Business Summary

The analysis showed that customers with month-to-month contracts, shorter tenure, and higher monthly charges are more likely to churn. Logistic Regression achieved strong predictive performance, while the Decision Tree model provided clear feature importance for business interpretation. These insights can help businesses identify at-risk customers early and improve customer retention through targeted offers and long-term contract plans.

### Skills Learned

* Customer Churn Prediction
* Decision Tree Classification
* Logistic Regression
* Data Preprocessing
* One-Hot Encoding
* Exploratory Data Analysis (EDA)
* Feature Importance
* Business Analytics
* Model Comparison
* Customer Retention Analysis

---

# 📅 Week 4

## ✅ Task 7 – ML Pipeline with Feature Engineering

### Objective

Build a professional and reusable Machine Learning pipeline using Scikit-Learn's Pipeline and ColumnTransformer. Apply preprocessing and feature engineering in a single workflow and evaluate whether engineered features improve model performance.

### Dataset

Titanic Dataset

### Workflow

* Load Titanic dataset
* Separate features and target variable
* Split data into training and testing sets
* Identify numerical and categorical features
* Apply SimpleImputer to handle missing values
* Apply StandardScaler to numerical features
* Apply OneHotEncoder to categorical features
* Build a ColumnTransformer
* Combine preprocessing and Logistic Regression into a single Pipeline
* Train and evaluate the baseline pipeline
* Create new engineered features
* Create FamilySize feature using SibSp and Parch
* Create IsAlone feature based on FamilySize
* Build an engineered preprocessing pipeline
* Train and evaluate the engineered pipeline
* Compare baseline and engineered pipeline performance
* Save the final pipeline using Joblib
* Load and verify the saved pipeline

### Feature Engineering

Two new features were created:

* **FamilySize** = SibSp + Parch + 1
* **IsAlone** = Indicates whether the passenger was traveling alone

### Preprocessing

Numerical features were processed using:

* Median Imputation
* StandardScaler

Categorical features were processed using:

* Most Frequent Imputation
* OneHotEncoder

### Model Used

* Logistic Regression

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

### Results

| Model               | Accuracy   |
| ------------------- | ---------- |
| Baseline Pipeline   | **80.45%** |
| Engineered Pipeline | **81.56%** |

### Feature Engineering Improvement

The baseline pipeline achieved **80.45%** accuracy, while the engineered pipeline achieved **81.56%** accuracy. Feature engineering improved the model performance by approximately **1.12 percentage points**.

### Final Pipeline

The final engineered pipeline was saved using Joblib:

`titanic_ml_pipeline.joblib`

The saved pipeline was successfully loaded and evaluated again, confirming that the complete preprocessing and model workflow can be reused for future predictions.

### Key Learning

Using Scikit-Learn Pipelines makes Machine Learning workflows cleaner, reusable, consistent, and less prone to preprocessing errors and data leakage. ColumnTransformer allows different preprocessing techniques to be applied to numerical and categorical features within the same workflow.

### Skills Learned

* Machine Learning Pipelines
* Scikit-Learn Pipeline
* ColumnTransformer
* Feature Engineering
* StandardScaler
* OneHotEncoder
* SimpleImputer
* Logistic Regression
* Data Preprocessing
* Model Evaluation
* Joblib
* Model Serialization
* Data Leakage Prevention
* Reusable ML Workflows

---

## ✅ Task 8 – Ensemble Learning: Random Forest vs XGBoost

### Objective

Compare ensemble learning methods with earlier single Machine Learning models using the Titanic dataset. Random Forest and XGBoost were trained and evaluated against Logistic Regression and Decision Tree models.

### Dataset

Titanic Dataset

### Models Used

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier
* XGBoost Classifier

### Workflow

* Load Titanic dataset
* Data preprocessing
* Handle missing values
* Encode categorical variables
* Train-Test Split
* Train Logistic Regression baseline model
* Train Decision Tree baseline model
* Train Random Forest ensemble model
* Train XGBoost ensemble model
* Compare model accuracy
* Visualize model performance
* Analyze Random Forest feature importance
* Analyze XGBoost feature importance
* Compare important features between both ensemble models

### Evaluation Metric

* Accuracy

### Model Comparison

| Model               | Metric   |      Score |
| ------------------- | -------- | ---------: |
| Logistic Regression | Accuracy | **80.45%** |
| Decision Tree       | Accuracy | **75.98%** |
| Random Forest       | Accuracy | **80.45%** |
| XGBoost             | Accuracy | **79.89%** |

### Feature Importance

Random Forest identified **Fare, Age, and Sex** as some of the most influential features for predicting Titanic passenger survival.

XGBoost also identified important Titanic passenger characteristics, with the importance distribution differing from Random Forest due to the different ensemble learning strategies used by the two models.

### Random Forest vs XGBoost

Random Forest combines multiple decision trees that are trained independently using random subsets of the data and features. XGBoost builds trees sequentially, where each new tree focuses on improving the errors made by the previous trees. Random Forest uses a bagging approach to reduce variance and overfitting, while XGBoost uses boosting to improve prediction performance. In this experiment, Random Forest achieved **80.45%** accuracy, while XGBoost achieved **79.89%** accuracy.

### Conclusion

Among the four tested models, Logistic Regression and Random Forest achieved the highest accuracy of **80.45%**. XGBoost achieved **79.89%**, while Decision Tree achieved **75.98%**. The results demonstrate that ensemble models can provide competitive performance compared with traditional single models, although the best-performing model depends on the dataset and model configuration.

### Files

* `ensemble_learning.ipynb`
* `random_forest_importance.png`
* `xgboost_importance.png`

### Skills Learned

* Ensemble Learning
* Random Forest
* XGBoost
* Bagging
* Boosting
* Feature Importance
* Model Comparison
* Classification
* Model Evaluation
* Data Preprocessing
* One-Hot Encoding
* Machine Learning Workflow

---

# 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* XGBoost
* Joblib
* Jupyter Notebook

---

# 📚 Learning Outcomes

Through these projects, I learned:

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Data Visualization
* Feature Engineering
* Feature Selection
* Classification
* Regression
* Logistic Regression
* Linear Regression
* Decision Tree Classification
* Random Forest
* XGBoost
* Ensemble Learning
* Bagging
* Boosting
* Customer Churn Prediction
* Machine Learning Pipelines
* Model Training
* Model Evaluation
* Accuracy Score
* Precision
* Recall
* F1-score
* Confusion Matrix
* Hyperparameter Tuning
* GridSearchCV
* Cross Validation
* One-Hot Encoding
* Feature Importance
* Business Analytics
* Customer Retention Analysis
* Model Comparison
* Machine Learning Workflow

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

✔ Machine Learning Pipelines

✔ Feature Engineering

✔ Joblib Model Serialization

✔ Random Forest Classification

✔ XGBoost Classification

✔ Ensemble Learning

✔ Feature Importance Analysis

✔ Model Performance Comparison

✔ Real-World Business Problem Solving

---

# 👩‍💻 Author

**Meerab Awan**

⭐ If you found this repository helpful, feel free to give it a Star.
