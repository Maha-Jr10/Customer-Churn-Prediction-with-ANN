# 📘 Data Dictionary: Telco Customer Churn Dataset

This document explains the columns in the Telco Customer Churn dataset used for training and prediction in this project.

---

## 🔢 Customer Information

| Column Name         | Description                                                         |
|---------------------|---------------------------------------------------------------------|
| `customerID`        | Unique ID assigned to each customer                                |
| `gender`            | Customer’s gender (Male or Female)                                 |
| `SeniorCitizen`     | Whether the customer is a senior citizen (1 = Yes, 0 = No)         |
| `Partner`           | Whether the customer has a partner (Yes or No)                     |
| `Dependents`        | Whether the customer has dependents (Yes or No)                    |

---

## 📞 Services Signed Up

| Column Name           | Description                                                                     |
|------------------------|---------------------------------------------------------------------------------|
| `PhoneService`         | Whether the customer has a phone service (Yes or No)                            |
| `MultipleLines`        | Whether the customer has multiple lines (Yes, No, or No phone service)          |
| `InternetService`      | Type of internet service (DSL, Fiber optic, or No)                              |
| `OnlineSecurity`       | Whether the customer has online security addon (Yes, No, or No internet service)|
| `OnlineBackup`         | Whether the customer has online backup addon (Yes, No, or No internet service)  |
| `DeviceProtection`     | Whether the customer has device protection addon (Yes, No, or No internet service) |
| `TechSupport`          | Whether the customer has technical support addon (Yes, No, or No internet service) |
| `StreamingTV`          | Whether the customer streams TV (Yes, No, or No internet service)               |
| `StreamingMovies`      | Whether the customer streams movies (Yes, No, or No internet service)           |

---

## 💳 Account Information

| Column Name        | Description                                                               |
|---------------------|---------------------------------------------------------------------------|
| `Contract`          | Type of contract (Month-to-month, One year, Two year)                    |
| `PaperlessBilling`  | Whether the customer receives paperless billing (Yes or No)              |
| `PaymentMethod`     | Payment method (Electronic check, Mailed check, Bank transfer, Credit card) |
| `MonthlyCharges`    | The amount charged to the customer monthly                               |
| `TotalCharges`      | The total amount charged to the customer                                 |

---

## 🎯 Target Variable

| Column Name | Description                                      |
|--------------|--------------------------------------------------|
| `Churn`      | Whether the customer left the company (Yes or No)|

---

## ✅ Notes

- `SeniorCitizen` is numeric, where 1 = Yes and 0 = No.
- Missing values in `TotalCharges` may exist where tenure is zero.
- All service columns with "No internet service" or "No phone service" are treated accordingly in preprocessing.
