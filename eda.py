import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ----------------------------------------
# LOAD the cleaned dataset
# ----------------------------------------
df = pd.read_csv(r'd:\TCS\cleaned_dataset1.csv')   # <- path & name must match your saved file

# ----------------------------------------
# CORRELATION ANALYSIS
# ----------------------------------------
corr = df.corr(numeric_only=True)
print("\nCorrelation with Delinquent_Account:")
print(corr['Delinquent_Account'].sort_values(ascending=False))

# ----------------------------------------
# VISUAL PATTERN CHECKS
# ----------------------------------------
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Delinquent_Account', y='Credit_Utilization')
plt.title("Credit Utilization vs. Delinquency")
plt.savefig("credit_utilization_vs_delinquency.png")
plt.clf()

sns.boxplot(data=df, x='Delinquent_Account', y='Missed_Payments')
plt.title("Missed Payments vs. Delinquency")
plt.savefig("missed_payments_vs_delinquency.png")
plt.clf()

sns.boxplot(data=df, x='Delinquent_Account', y='Credit_Score')
plt.title("Credit Score vs. Delinquency")
plt.savefig("credit_score_vs_delinquency.png")
plt.clf()

print("✅ Risk‑pattern plots saved to your TCS folder.")
