# 🔍 Customer Churn Prediction with ANN

A complete end-to-end machine learning project to predict **customer churn** using an **Artificial Neural Network (ANN)**. This project includes data exploration, preprocessing, model training, and deployment through a **Streamlit web app**.

---

## 📁 Project Files

| File Name                              | Description                                                                                     |
|---------------------------------------|-------------------------------------------------------------------------------------------------|
| `myapp.py`                            | 💻 Main Streamlit application for live customer churn prediction using user input               |
| `customer_churn_ann.h5`               | 🤖 Trained Artificial Neural Network (ANN) model saved in HDF5 format                           |
| `WA_Fn-UseC_-Telco-Customer-Churn.xlsx` | 📊 Raw Telco Customer Churn dataset used for exploratory data analysis and model development   |
| `CCP with ANN.ipynb`                  | 📓 Jupyter notebook with complete EDA, feature engineering, model training, and evaluation      |
| `data_dictionary.md` *(optional)*     | 🧾 Explanation of each column in the Telco dataset for better understanding                     |
| `README.md`                           | 🧾 This current file                                                                            |

---

## 🚀 App Features

- Predicts churn probability using a trained deep learning model
- Clean, responsive UI to input customer details
- Risk-based feedback and business recommendations
- Simple, single-click deployment using Streamlit

---

## 📊 Dataset

- **Source**: [Kaggle - Telco Customer Churn](https://www.kaggle.com/blastchar/telco-customer-churn)
- **Type**: Binary classification (Churn: Yes/No)
- **Features**:
  - Customer demographics (gender, senior citizen, dependents)
  - Service usage (phone, internet, streaming, support)
  - Contract and billing (monthly/total charges, payment method, contract type)

---

## 🔬 Model Development

Model built using **TensorFlow/Keras** in `CCP with ANN.ipynb`.

### Steps Included:

- Data cleaning & preprocessing
- Encoding categorical variables
- Feature scaling
- ANN architecture design (input → hidden layers → output)
- Model training and evaluation
- Model saved as `customer_churn_ann.h5`

---

## 🧪 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/customer-churn-ann-app.git
cd customer-churn-ann-app
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app

```bash
streamlit run myapp.py
```

---

## 📈 Example Output

```text
✅ Low Risk of Churn
There’s a 14.62% chance this customer will leave.
Recommendation: No immediate action needed; keep up the great service!
```

---

## 🧰 Tech Stack

* 🧠 TensorFlow & Keras – Neural Network modeling
* 🖥 Streamlit – Web app interface
* 📊 Pandas & NumPy – Data analysis & preprocessing
* 📈 Matplotlib – Visualizations
* 📦 scikit-learn – Evaluation metrics & encoders

---

## 👨‍💻 Author

**Muhammed John**
Aspiring Data Scientist & AI Engineer

🌐 [Portfolio](https://maha-jr10.github.io/Johns-website/)
💻 [GitHub](https://github.com/maha-jr10)
🔗 [LinkedIn](https://www.linkedin.com/in/Maha-Jr)

---

## 🙌 Acknowledgments

* [Kaggle Telco Dataset](https://www.kaggle.com/blastchar/telco-customer-churn)
* Streamlit community for app inspiration

```

