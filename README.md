#  Task 4 — Feature Encoding & Scaling  
### AI & ML Internship  
### By: Pranav S P

---

## Project Overview
This project performs **feature encoding and numerical scaling** on the Adult Income dataset.  
A fully modular, reusable, and professional preprocessing pipeline was built using separate Python modules.

---

##  Project Structure

```
AI_ML_Task4/
│
├── data/
│   └── adult.csv
│
├── src/
│   ├── encoder.py
│   ├── scaler.py
│   └── feature_utils.py
│
├── notebooks/
│   └── preprocessing.ipynb
│
├── outputs/
│   ├── processed/
│   │   └── adult_processed.csv
│   └── screenshots/
│       ├── head_output.txt
│       ├── feature_types.txt
│       ├── encoding_columns.txt
│       ├── numerical_after_encoding.txt
│       ├── scaled_head_output.txt
│       ├── scaling_report.txt
│       └── (plot images if created)
│
└── reports/
    └── task4_feature_engineering.md
```

---

## 🛠 Tech Stack

- **Python**
- **Pandas**
- **NumPy**
- **scikit-learn**
- **Matplotlib**
- Custom preprocessing modules:
  - `encoder.py`
  - `scaler.py`
  - `feature_utils.py`

---

##  What This Project Does

### **1️. Feature Cleaning**
- Removes extra spaces  
- Standardizes column names  

### **2️. Feature Encoding**
- Automatically classifies features  
- Applies:
  - Label Encoding (for low-unique categorical features)
  - One-Hot Encoding (for high-unique categorical features)

### **3️. Feature Scaling**
- StandardScaler applied to all numerical features  
- Before/after comparison generated  

### **4️. Output Export**
- Cleaned, encoded, scaled dataset exported as:  
  ```
  outputs/processed/adult_processed.csv
  ```

---

## 📘 What I Learnt From This Task

- Practical feature encoding (Label vs One-Hot)
- Why scaling is necessary for ML models
- How to build reusable encoding/scaling modules
- How to clean messy datasets before encoding
- How to automate project structure professionally
---


