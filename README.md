
# Predicting Heart Disease Using Machine Learning

This project aims to develop a machine learning model to predict whether a patient has heart disease based on various medical attributes. It utilizes several Python-based machine learning and data science libraries.

## Table of Contents

1. [Problem Definition](#problem-definition)
2. [Data](#data)
3. [Evaluation](#evaluation)
4. [Features](#features)
5. [Modelling](#modelling)
6. [Experimentation](#experimentation)

## Problem Definition

Given clinical parameters, can we predict whether or not a patient has heart disease?

## Data

The original data comes from the Cleveland dataset from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/45/heart+disease). This multivariate dataset consists of 14 attributes, including age, sex, chest pain type, resting blood pressure, serum cholesterol, fasting blood sugar, resting electrocardiographic results, maximum heart rate achieved, exercise-induced angina, oldpeak, the slope of the peak exercise ST segment, number of major vessels, and Thalassemia.

## Evaluation

Our goal is to achieve 95% accuracy in predicting whether a patient has heart disease.

## Features

The key attributes in the dataset include:

1. Age
2. Sex
3. Chest Pain Type
4. Resting Blood Pressure
5. Serum Cholesterol
6. Fasting Blood Sugar
7. Resting Electrocardiographic Results
8. Maximum Heart Rate Achieved
9. Exercise-Induced Angina
10. Oldpeak (ST depression induced by exercise relative to rest)
11. The Slope of the Peak Exercise ST Segment
12. Number of Major Vessels
13. Thalassemia
14. Target (Presence of heart disease)

## Modelling

We utilize various classification algorithms to model the data, including:

- Random Forest Classifier
- Logistic Regression
- Ridge Classifier
- Decision Tree Classifier
- K-Nearest Neighbors Classifier
- Multinomial Naive Bayes
- Support Vector Classifier (SVC)
- Linear SVC

## Experimentation

We conduct data exploratory analysis (EDA) and model evaluation using metrics such as precision, confusion matrix, classification report, F1 score, recall score, and accuracy score. Additionally, we employ techniques like cross-validation, RandomizedSearchCV, GridSearchCV, and ROC AUC score for model optimization.

## Usage

To run this project, ensure you have the following libraries installed:

- pandas
- matplotlib
- seaborn
- NumPy
- sci-kit-learn

You can install the required libraries using:

```sh
pip install pandas matplotlib seaborn numpy sci-kit-learn
```

### Data Loading

The data can be loaded using:

```python
import pandas as pd
df = pd.read_csv("heart-disease.csv")
```

### Running the Models

You can run various models using the provided code snippets in the notebook.

---
