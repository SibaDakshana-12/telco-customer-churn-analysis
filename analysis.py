
from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

sns.set_style("whitegrid")
plt.rcParams["figure.dpi"] = 110

DATA_PATH = Path("data/Telco-Customer-Churn.csv")
OUT = Path("outputs")
OUT.mkdir(parents=True, exist_ok=True)

# 1. Load data
df = pd.read_csv(DATA_PATH)

print("Dataset shape:", df.shape)
print(df.head())
print(df.info())

# 2. Clean data
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"], errors="coerce"
)

print("\nMissing values before cleaning:")
print(df.isnull().sum()[df.isnull().sum() > 0])

zero_tenure = df["tenure"] == 0
df.loc[zero_tenure, "TotalCharges"] = (
    df.loc[zero_tenure, "TotalCharges"].fillna(0)
)

df["TotalCharges"] = df["TotalCharges"].fillna(
    df["TotalCharges"].median()
)

df.drop(columns=["customerID"], inplace=True)

df["Churn_Flag"] = df["Churn"].map({
    "Yes": 1,
    "No": 0
})

if df["Churn_Flag"].isnull().any():
    raise ValueError("Unexpected values found in Churn column.")

print("\nData types:")
print(df.dtypes.value_counts())

# 3. Overall churn rate
churn_rate = df["Churn_Flag"].mean() * 100

print(f"\nOverall churn rate: {churn_rate:.2f}%")
print(df["Churn"].value_counts())

# 4. Churn distribution
counts = df["Churn"].value_counts().reindex(["No", "Yes"])

fig, ax = plt.subplots(figsize=(5, 4))
bars = ax.bar(
    counts.index,
    counts.values,
    color=["#4C72B0", "#DD8452"]
)

for bar, value in zip(bars, counts.values):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 50,
        f"{value}\n({value / len(df) * 100:.1f}%)",
        ha="center",
        fontweight="bold"
    )

ax.set_title("Customer Churn Distribution")
ax.set_ylabel("Number of Customers")
plt.tight_layout()
plt.savefig(OUT / "01_churn_distribution.png")
plt.close()

# 5. Churn by contract
contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn"],
    normalize="index"
).reindex(columns=["No", "Yes"]) * 100

contract_churn.plot(
    kind="bar",
    stacked=True,
    figsize=(6, 4),
    color=["#4C72B0", "#DD8452"]
)

plt.title("Churn Rate by Contract Type")
plt.ylabel("Percentage of Customers")
plt.xlabel("Contract Type")
plt.xticks(rotation=0)
plt.legend(title="Churn")
plt.tight_layout()
plt.savefig(OUT / "02_churn_by_contract.png")
plt.close()

print("\nChurn rate by contract:")
print(contract_churn.round(2))

# 6. Tenure distribution
fig, ax = plt.subplots(figsize=(7, 4))

sns.histplot(
    data=df,
    x="tenure",
    hue="Churn",
    multiple="stack",
    bins=30,
    hue_order=["No", "Yes"],
    palette={"No": "#4C72B0", "Yes": "#DD8452"},
    ax=ax
)

ax.set_title("Customer Tenure Distribution by Churn")
ax.set_xlabel("Tenure (months)")
plt.tight_layout()
plt.savefig(OUT / "03_tenure_by_churn.png")
plt.close()

# 7. Churn rate by tenure bands
df["TenureBand"] = pd.cut(
    df["tenure"],
    bins=[-1, 12, 24, 48, 60, 72],
    labels=[
        "0-12 months",
        "13-24 months",
        "25-48 months",
        "49-60 months",
        "61-72 months"
    ]
)

tenure_summary = df.groupby(
    "TenureBand",
    observed=False
).agg(
    Customers=("Churn_Flag", "size"),
    Churn_Rate=("Churn_Flag", "mean")
)

tenure_summary["Churn_Rate"] *= 100

print("\nChurn rate by tenure band:")
print(tenure_summary.round(2))

tenure_summary["Churn_Rate"].plot(
    kind="bar",
    figsize=(7, 4),
    color="#4C72B0"
)

plt.title("Churn Rate by Tenure Band")
plt.ylabel("Churn Rate (%)")
plt.xlabel("Tenure")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(OUT / "04_churn_by_tenure_band.png")
plt.close()

tenure_summary.to_csv(OUT / "tenure_summary.csv")

# 8. Monthly charges by churn
fig, ax = plt.subplots(figsize=(5, 4))

sns.boxplot(
    data=df,
    x="Churn",
    y="MonthlyCharges",
    order=["No", "Yes"],
    hue="Churn",
    hue_order=["No", "Yes"],
    palette={"No": "#4C72B0", "Yes": "#DD8452"},
    legend=False,
    ax=ax
)

ax.set_title("Monthly Charges by Churn Status")
plt.tight_layout()
plt.savefig(OUT / "05_monthlycharges_by_churn.png")
plt.close()

print("\nMonthly charges by churn:")
print(
    df.groupby("Churn")["MonthlyCharges"]
    .agg(["count", "mean", "median", "std"])
    .round(2)
)

# 9. Correlation analysis
numeric_cols = [
    "tenure",
    "MonthlyCharges",
    "TotalCharges",
    "SeniorCitizen",
    "Churn_Flag"
]

corr = df[numeric_cols].corr()

fig, ax = plt.subplots(figsize=(7, 5))

sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0,
    ax=ax
)

ax.set_title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(OUT / "06_correlation_heatmap.png")
plt.close()

print("\nCorrelation with churn:")
print(corr["Churn_Flag"].sort_values(ascending=False))

# 10. Categorical feature analysis
categorical_features = [
    "Contract",
    "InternetService",
    "PaymentMethod",
    "TechSupport",
    "OnlineSecurity",
    "PaperlessBilling"
]

feature_summary = []

for col in categorical_features:
    rates = (
        df.groupby(col, observed=False)["Churn_Flag"]
        .agg(["mean", "count"])
        .rename(columns={
            "mean": "Churn_Rate",
            "count": "Customers"
        })
    )

    rates["Churn_Rate"] *= 100
    rates["Feature"] = col
    rates["Category"] = rates.index

    feature_summary.append(rates.reset_index(drop=True))

feature_summary = pd.concat(
    feature_summary,
    ignore_index=True
)

feature_summary = feature_summary[
    ["Feature", "Category", "Customers", "Churn_Rate"]
]

print("\nChurn rate by categorical feature:")
print(feature_summary.round(2))

feature_summary.to_csv(
    OUT / "categorical_feature_summary.csv",
    index=False
)

# 11. Chi-square tests and Cramer's V
chi_results = []

for col in categorical_features:
    contingency = pd.crosstab(df[col], df["Churn"])

    chi2, p_value, dof, expected = stats.chi2_contingency(
        contingency
    )

    n = contingency.to_numpy().sum()
    rows, cols = contingency.shape

    cramers_v = np.sqrt(
        chi2 / (n * min(rows - 1, cols - 1))
    )

    chi_results.append({
        "Feature": col,
        "Chi2": chi2,
        "Degrees_of_Freedom": dof,
        "p_value": p_value,
        "Cramers_V": cramers_v,
        "Significant": p_value < 0.05
    })

chi_df = pd.DataFrame(chi_results)

chi_df = chi_df.sort_values(
    "Cramers_V",
    ascending=False
)

print("\nChi-square tests and Cramer's V:")
print(chi_df.round(4))

chi_df.to_csv(
    OUT / "chi_square_results.csv",
    index=False
)

# 12. Welch's t-test on tenure
tenure_churn = df.loc[
    df["Churn"] == "Yes", "tenure"
]

tenure_retained = df.loc[
    df["Churn"] == "No", "tenure"
]

t_stat, p_value = stats.ttest_ind(
    tenure_churn,
    tenure_retained,
    equal_var=False
)

mean_difference = (
    tenure_churn.mean() - tenure_retained.mean()
)

print("\nWelch's t-test: tenure")
print(f"Churned mean: {tenure_churn.mean():.2f} months")
print(f"Retained mean: {tenure_retained.mean():.2f} months")
print(f"Mean difference: {mean_difference:.2f} months")
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4e}")

# 13. Save cleaned dataset
df.to_csv(
    OUT / "cleaned_churn_data.csv",
    index=False
)

print("\nAll outputs saved to:", OUT.resolve())