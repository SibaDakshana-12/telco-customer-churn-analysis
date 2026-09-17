# 📉 Customer Churn Analysis — Telco Dataset

Statistical analysis of customer churn drivers for a telecom company, using Python, pandas, and hypothesis testing to identify significant retention risk factors and inform business strategy.

## About the Project

This project analyzes the **IBM Telco Customer Churn** dataset (7,043 customers, 21 features) to answer one core business question:

> **What factors are driving customers to leave, and are these factors statistically significant — or just noise?**

Unlike a purely descriptive dashboard, this analysis goes a step further by applying **hypothesis testing (Chi-Square and t-tests)** to validate which churn drivers are statistically meaningful, giving retention strategy recommendations a rigorous, evidence-based foundation.

## Objectives

* Calculate the overall customer churn rate.
* Identify churn rate differences across contract type, payment method, internet service, and support add-ons.
* Quantify the relationship between tenure, monthly charges, and churn.
* Statistically validate which features are significantly associated with churn (Chi-Square tests).
* Test whether tenure differs significantly between churned and retained customers (t-test).
* Translate findings into actionable retention recommendations.

## Dataset

**Source:** [IBM Telco Customer Churn](https://github.com/IBM/telco-customer-churn-on-icp4d)

| Attribute | Description |
|---|---|
| Demographics | Gender, senior citizen status, partner, dependents |
| Account info | Tenure, contract type, payment method, paperless billing, monthly/total charges |
| Services | Phone, internet, online security, tech support, streaming TV/movies |
| Target | `Churn` (Yes/No) |

## Technologies Used

| Technology | Purpose |
|---|---|
| **Python / pandas** | Data loading, cleaning, aggregation |
| **matplotlib / seaborn** | Data visualization |
| **SciPy (stats)** | Chi-Square tests, independent t-test |
| **Jupyter Notebook** | Analysis narrative and reproducibility |

## Key Findings

| Driver | Insight |
|---|---|
| **Contract type** | Month-to-month churn (**42.7%**) is ~15x higher than two-year contracts (**2.8%**) |
| **Payment method** | Electronic check users churn at **45.3%** — nearly 3x automatic payment methods |
| **Tenure** | Churned customers average **18.0 months** vs. **37.6 months** for retained (statistically significant, p ≈ 1.2×10⁻²³²) |
| **Support add-ons** | No Tech Support / Online Security nearly **triples** churn risk (~41% vs. ~15%) |
| **Internet service** | Fiber optic customers churn more than double DSL customers (41.9% vs. 19.0%) |

All six analyzed categorical features showed a **statistically significant** association with churn (Chi-Square test, p < 0.001 in every case).

## Business Recommendations

1. **Incentivize longer contracts** — discount offers to convert month-to-month customers to annual plans.
2. **Push automatic payment adoption** among electronic-check users.
3. **Bundle tech support & security add-ons** at a discount for at-risk segments.
4. **Focus retention outreach on the 0–18 month window**, the highest-risk period.
5. **Investigate fiber optic pricing/service quality**, given its disproportionate churn rate.

## Project Structure

```text
churn-analysis/
│
├── data/
│   └── Telco-Customer-Churn.csv
│
├── outputs/
│   ├── 01_churn_distribution.png
│   ├── 02_churn_by_contract.png
│   ├── 03_tenure_by_churn.png
│   ├── 04_monthlycharges_by_churn.png
│   ├── 05_correlation_heatmap.png
│   ├── chi_square_results.csv
│   └── cleaned_churn_data.csv
│
├── churn_analysis.ipynb
├── analysis.py
├── requirements.txt
└── README.md
```

## How to Run

1. Clone the repository:
```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd churn-analysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the notebook:
```bash
jupyter notebook churn_analysis.ipynb
```

Or run the standalone script:
```bash
python analysis.py
```

## Methodology

1. **Data Cleaning** — Fixed `TotalCharges` (loaded as text due to blank values for new customers), handled missing values, dropped non-analytical identifier column.
2. **EDA** — Overall churn rate, distribution plots, tenure and monthly charges by churn status.
3. **Feature Analysis** — Churn rate breakdown across contract type, payment method, internet service, and support add-ons.
4. **Correlation Analysis** — Correlation heatmap for numeric features against churn.
5. **Hypothesis Testing** — Chi-Square tests for categorical associations; independent t-test for tenure differences.
6. **Business Translation** — Converted statistical findings into concrete retention actions.

## Author

**Siba Sankar Mallick**

- [GitHub](https://github.com/SibaDakshana-12)
