# 📉 Credit Risk Analysis

This project focuses on performing detailed **exploratory data analysis (EDA)** on customer credit data to identify patterns related to **delinquency risk**. By visualizing and analyzing features like credit score, credit utilization, and missed payments, this project aims to help financial institutions make informed decisions by understanding risk behaviors.

---

## 📁 Project Structure

Credit_Risk_Analysis/
│
├── eda.py # Python script for data analysis and visualizations
├── dataset.xlsx # Raw dataset
├── cleaned_dataset1.xlsx # Cleaned and preprocessed dataset
│
├── credit_score_vs_delinquency.png # Visualization: Credit Score vs Delinquency
├── credit_utilization_vs_delinquecy.png # Visualization: Credit Utilization vs Delinquency
│
├── EDA_Report_Geldium_Delinquency.docx # Final EDA report with observations
└── README.md # Project overview and instructions


---

## 🎯 Objectives

- Understand customer behaviors linked to credit delinquency
- Explore how features like credit score, utilization, and missed payments affect risk
- Present findings visually and statistically
- Provide clear insights for decision-making

---

## 🛠 Tools & Technologies

- **Python**
  - `pandas`, `matplotlib`, `seaborn`
- **Excel** – Data inspection & support
- **MS Word** – Final report documentation

---

## 📊 Key Insights

- 📉 **Low credit scores** strongly correlate with higher delinquency risk
- 🔺 Customers with **high credit utilization** are more prone to default
- ❗ **Missed payments** are significant warning signs in risk detection
- 📈 Visuals reinforce statistical patterns and help communicate findings clearly

---

## 🚀 How to Run

1. Make sure Python 3.x is installed
2. Open and run the `eda.py` script
3. Install required libraries:

```bash
pip install pandas matplotlib seaborn
Open your terminal or Git Bash in the project folder

Run the EDA script using:

python eda.py
The script will:

Load and process the dataset

Generate and save output graphs

Print correlation analysis results to the terminal
