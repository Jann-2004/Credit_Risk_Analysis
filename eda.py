import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ----------------------------------------
# LOAD the cleaned dataset
# ----------------------------------------
df = pd.read_csv(r'd:\Credit_Risk_Analysis\cleaned_dataset1.csv')  # ✅ Ensure path is correct

# ----------------------------------------
# CORRELATION ANALYSIS
# ----------------------------------------
corr = df.corr(numeric_only=True)
print("\nCorrelation with Delinquent_Account:")
print(corr['Delinquent_Account'].sort_values(ascending=False))

# ----------------------------------------
# VISUAL PATTERN CHECKS
# ----------------------------------------

# 1. Credit Utilization vs Delinquency
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Delinquent_Account', y='Credit_Utilization')
plt.title("Credit Utilization vs. Delinquency")
plt.savefig("credit_utilization_vs_delinquency.png")
plt.show()

# 2. Missed Payments vs Delinquency
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Delinquent_Account', y='Missed_Payments')
plt.title("Missed Payments vs. Delinquency")
plt.savefig("missed_payments_vs_delinquency.png")
plt.show()

# 3. Credit Score vs Delinquency
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Delinquent_Account', y='Credit_Score')
plt.title("Credit Score vs. Delinquency")
plt.savefig("credit_score_vs_delinquency.png")
plt.show()

print("✅ Risk‑pattern plots saved and displayed.")
