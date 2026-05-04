# Stroke Risk Prediction Using Machine Learning

## 📌 Project Overview

Stroke is a leading cause of long-term disability and mortality worldwide, particularly in low- and middle-income countries where access to advanced diagnostic tools may be limited. Early identification of individuals at high risk of stroke can support timely preventive interventions and improve clinical outcomes.

This project develops a **machine learning classification model** to predict stroke risk using routine demographic and clinical features. The aim is to demonstrate a practical, interpretable, and reproducible healthcare ML workflow suitable for educational and exploratory purposes.

---

## 🩺 Clinical Relevance

In clinical practice, stroke prevention relies heavily on identifying modifiable and non-modifiable risk factors such as age, hypertension, cardiovascular disease, and lifestyle factors. By leveraging these routinely collected variables, this project explores how machine learning can assist in **risk stratification**, especially in resource-limited healthcare settings.

---

## 📊 Dataset Description

The dataset contains **5,110 patient records** with the following features:

* Demographic variables: age, gender, residence type
* Clinical variables: hypertension, heart disease, average glucose level, BMI
* Lifestyle factors: smoking status, marital status, work type
* Target variable: `stroke` (0 = no stroke, 1 = stroke)

> Note: The dataset used in this project is of \\\\\\\*\\\\\\\*confidential source\\\\\\\*\\\\\\\* downloaded from \\\\\\\*kaggle.com\\\\\\\* - Use only for educational purposes. If you use this dataset in your research, please credit the author.

---

## 🧪 Methodology

### 1\. Data Preprocessing

* Handled missing BMI values by dropping the nulls
* Converted categorical variables using one-hot encoding (pd.get\_dummies())
* Standardized numerical features
* Examined distributions and outliers to better understand data. Possible outliers were left uncapped to avoid loss of important medical data (e.g. avg\_glucose\_level above 250 could be indicative of Diabetes Mellitus)

### 2\. Exploratory Data Analysis (EDA)

* Visualized class distribution and key feature patterns
* Identified class imbalance and potential implications for model performance
* Solve class imbalance using the random oversampling method (sampling\_strategy='minority')

### 3\. Model Development

* Algorithm: **Logistic Regression**
* Further addressed class imbalance using `class\\\\\\\_weight='balanced'`
* Train-test split: 80% training, 20% testing



---

## 👤 Author

**Habeeb O. Issa**  
Medical Student | Aspiring Healthcare ML Engineer

---

## 📄 Disclaimer

This project is intended for educational and exploratory purposes only. It does not constitute medical advice and should not be used for clinical decision-making.

