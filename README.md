# 🚀 NeuroFive Machine Learning Track

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Visualization-4C72B0)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikit-learn)
![Status](https://img.shields.io/badge/Status-Week%202%20Completed-success)

---

## 📖 About

This repository contains my work completed during the **NeuroFive Solutions Machine Learning Internship**.

The tasks focus on building strong foundations in **Python, Data Analysis, Data Cleaning, Data Visualization, and Machine Learning**.

---

# 📂 Repository Structure

```text
Week1
│
├── Task1
│   ├── Titanic_EDA.ipynb
│   └── train.csv
│
└── Task2
    ├── Titanic_Data_Cleaning_Visualization.ipynb
    └── train.csv

Week2
│
└── Task3
    ├── Titanic_Survival_Prediction.ipynb
    └── train.csv
````

---

# 📅 Week 1

## 📌 Task 1 – Titanic Dataset Exploration (EDA)

### 🎯 Objectives

* Load the Titanic dataset
* Explore the dataset
* Understand dataset structure
* Identify missing values
* Perform Exploratory Data Analysis (EDA)

### 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Jupyter Notebook

---

## 📌 Task 2 – Clean & Visualize Real-World Data

### 🎯 Objectives

* Handle missing values
* Detect outliers
* Create visualizations
* Analyze survival patterns

### 📊 Visualizations

* Histogram
* Boxplot
* Bar Chart
* Correlation Heatmap

### 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

---

# 📅 Week 2

## 📌 Task 3 – Titanic Survival Prediction — Your First Classification Model

### 🎯 Objectives

* Prepare the Titanic dataset for machine learning
* Handle missing values
* Encode categorical columns
* Split the dataset into training and testing sets
* Train a Logistic Regression model
* Predict passenger survival
* Evaluate the model using accuracy score
* Print and analyze a confusion matrix

---

### 🧹 Data Cleaning

The original Titanic dataset contained missing values in the `Age`, `Cabin`, and `Embarked` columns.

The following steps were performed:

* The `Cabin` column was dropped because it contained a large number of missing values.
* Missing values in the `Age` column were filled using the median.
* Missing values in the `Embarked` column were filled using the mode.

---

### 🎯 Feature Selection

The following columns were removed because they were not useful as direct predictive features:

* `PassengerId`
* `Name`
* `Ticket`

The target variable was:

* `Survived`

The remaining columns were used as input features.

---

### 🔤 Categorical Encoding

The `Sex` and `Embarked` columns contain categorical values.

One-Hot Encoding was used to convert these categorical values into numerical features so they could be processed by the machine learning model.

---

### ✂️ Train-Test Split

The dataset was divided into training and testing sets using `train_test_split`.

* **80%** of the data was used for training.
* **20%** of the data was used for testing.
* `random_state=42` was used to make the split reproducible.

---

### 🤖 Machine Learning Model

**Logistic Regression** was used for this classification task.

Logistic Regression was selected because the target variable is binary:

* `0` – Did not survive
* `1` – Survived

---

### 📊 Model Evaluation

The model was evaluated using `accuracy_score`.

The Logistic Regression model achieved an accuracy of:

**81.01%**

This means the model correctly classified approximately 81% of the passengers in the test dataset.

---

### 📌 Confusion Matrix

A confusion matrix was used to understand the correct and incorrect predictions made by the model.

The resulting confusion matrix was:

```text
[[90 15]
 [19 55]]
```

The results were:

* **90** passengers were correctly predicted as not survived.
* **15** passengers were incorrectly predicted as survived.
* **19** passengers were incorrectly predicted as not survived.
* **55** passengers were correctly predicted as survived.

The model made **145 correct predictions out of 179 test samples**.

---

### 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Jupyter Notebook

---

# 📁 Dataset

* Titanic Dataset (`train.csv`)

---

# 📚 Skills Learned

* Data Cleaning
* Handling Missing Values
* Outlier Detection
* Data Visualization
* Exploratory Data Analysis (EDA)
* Correlation Analysis
* Feature Selection
* Categorical Encoding
* One-Hot Encoding
* Train-Test Split
* Logistic Regression
* Classification
* Model Training
* Model Prediction
* Model Evaluation
* Accuracy Score
* Confusion Matrix
* Python Programming
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn

---

# 🎯 Internship Progress

| Week   | Task        | Status      |
| ------ | ----------- | ----------- |
| Week 1 | Task 1      | ✅ Completed |
| Week 1 | Task 2      | ✅ Completed |
| Week 2 | Task 3      | ✅ Completed |
| Week 3 | Coming Soon | ⏳           |
| Week 4 | Coming Soon | ⏳           |

---

# 👩‍💻 Author

**Meerab Awan**

---

## ⭐ Thank You

Thank you for visiting this repository.

If you found this repository useful, feel free to ⭐ star it.

```
```
