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

- Demographic variables: age, gender, residence type  
- Clinical variables: hypertension, heart disease, average glucose level, BMI  
- Lifestyle factors: smoking status, marital status, work type  
- Target variable: `stroke` (0 = no stroke, 1 = stroke)

> Note: The dataset used in this project is of **confidential source** downloaded from *kaggle.com* - Use only for educational purposes. If you use this dataset in your research, please credit the author.

---

## 🧪 Methodology

### 1. Data Preprocessing
- Handled missing BMI values by dropping the nulls  
- Converted categorical variables using one-hot encoding (pd.get_dummies()) 
- Standardized numerical features  
- Examined distributions and outliers to better understand data. Possible outliers were left uncapped to avoid loss of important medical data (e.g. avg_glucose_level above 250 could be indicative of Diabetes Mellitus) 

### 2. Exploratory Data Analysis (EDA)
- Visualized class distribution and key feature patterns  
- Identified class imbalance and potential implications for model performance
- Solve class imbalance using the random oversampling method (sampling_strategy='minority') 

### 3. Model Development
- Algorithm: **Logistic Regression**
- Further addressed class imbalance using `class_weight='balanced'`
- Train-test split: 80% training, 20% testing

### 4. Model Evaluation
Evaluation metrics included:
- Accuracy  
- Precision  
- Recall  
- F1-score  
- Confusion matrix and CM Display 

These metrics were chosen to provide a balanced assessment, particularly in the context of imbalanced medical data where accuracy alone may be misleading.

---

## 📈 Results Summary
The final model achieved an overall accuracy of approximately **79%**, with balanced precision and recall across classes. The confusion matrix demonstrated that the model successfully predicts both stroke and non-stroke cases, though some false negatives remain.

> From a clinical perspective, false negatives are particularly important, as missed high-risk patients may delay preventive care. This highlights the trade-off between sensitivity and specificity inherent in many medical ML applications.

---

## ⚠️ Limitations 
- No imaging, laboratory biomarkers, or longitudinal follow-up data were included  
- The model has not been externally validated on independent datasets  
- Logistic regression was used as a baseline model; more complex models may yield improved performance  

---

## 🔮 Future Improvements
Potential extensions of this project include:
- Comparison with tree-based and ensemble models (Random Forest, XGBoost)  
- Application of SMOTE and other resampling techniques  
- Optimization for recall to reduce false negatives  
- ROC-AUC and threshold tuning  
- Validation using real-world clinical datasets  

---

## 🛠️ Technologies Used
- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  
- Jupyter Notebook  

---

## 👤 Author
**Habeeb O. Issa**  
Medical Student | Aspiring Healthcare ML Engineer 

---

## 📄 Disclaimer
This project is intended for educational and exploratory purposes only. It does not constitute medical advice and should not be used for clinical decision-making.
