# 📉 Telecom Customer Churn Analysis

Statistical analysis of customer churn in a telecom company using Python, pandas, and hypothesis testing to identify retention risk factors and inform business recommendations.

## About the Project

This project analyzes the **IBM Telco Customer Churn** dataset (7,043 customers, 21 features) to answer:

> What factors are associated with customers leaving, and are these relationships statistically significant?

Beyond descriptive analysis, this project uses **Chi-Square tests and an independent-samples t-test** to investigate churn patterns and assess statistical significance.

## Objectives

* Calculate the overall customer churn rate.
* Analyze churn across contract type, payment method, internet service, and support add-ons.
* Examine relationships between tenure, monthly charges, and churn.
* Test categorical associations with churn using Chi-Square tests.
* Test tenure differences between churned and retained customers.
* Translate findings into business recommendations.

## Dataset

**Source:** [IBM Telco Customer Churn Dataset](https://github.com/IBM/telco-customer-churn-on-icp4d)

The dataset contains 7,043 customer records and 21 original features.

| Category            | Examples                                                    |
| ------------------- | ----------------------------------------------------------- |
| Demographics        | Gender, senior citizen status, partner, dependents          |
| Account information | Tenure, contract, payment method, monthly and total charges |
| Services            | Phone, internet, online security, tech support, streaming   |
| Target              | `Churn` (Yes/No)                                            |

## Technologies Used

| Technology            | Purpose                             |
| --------------------- | ----------------------------------- |
| Python, pandas, NumPy | Data cleaning and analysis          |
| Matplotlib, Seaborn   | Data visualization                  |
| SciPy                 | Statistical hypothesis testing      |
| Jupyter Notebook      | Reproducible analysis and narrative |

## Key Findings

| Factor           | Finding                                                                                                                    |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Contract type    | Month-to-month churn is **42.71%**, compared with **2.83%** for two-year contracts—about 15 times the rate.                |
| Payment method   | Electronic-check customers have a **45.29%** churn rate, compared with approximately **15–19%** for other payment methods. |
| Tenure           | Churned customers average **17.98 months**, versus **37.57 months** for retained customers.                                |
| Tech support     | Churn is **41.64%** among customers without tech support, compared with **15.17%** among those with it.                    |
| Online security  | Churn is **41.77%** among customers without online security, compared with **14.61%** among those with it.                 |
| Internet service | Fiber-optic customers have a **41.89%** churn rate, compared with **18.96%** for DSL customers.                            |

### Statistical Findings

* All six categorical features tested showed statistically significant associations with churn (**p < 0.001**).
* The tenure comparison between churned and retained customers was statistically significant (**Welch’s t-test, p ≈ 1.20 × 10⁻²³²**).
* Statistical significance indicates evidence of an association or difference; it does not establish causation.

## Business Recommendations

1. **Evaluate longer-contract incentives** — test discounts or benefits for month-to-month customers considering annual plans.
2. **Review payment experience** — investigate barriers to automatic payment adoption among electronic-check customers.
3. **Evaluate support and security bundles** — test whether targeted offers are associated with improved retention.
4. **Prioritize early-tenure customers** — focus retention analysis on customers in the **0–12 month** band, where churn is **47.44%**.
5. **Investigate fiber-optic churn** — examine service quality, pricing, and customer feedback to understand the higher observed churn rate.

These are proposed actions to evaluate, not proven churn-reduction effects.

## Methodology

1. **Data cleaning** — converted `TotalCharges` to numeric, handled blank values, and removed the customer identifier from analytical features.
2. **Exploratory analysis** — calculated churn rate and examined churn distributions.
3. **Feature analysis** — compared churn rates across customer segments.
4. **Correlation analysis** — examined correlations between numeric features and churn.
5. **Hypothesis testing** — used Chi-Square tests for categorical associations and Welch’s t-test for tenure differences.
6. **Business interpretation** — translated observed patterns into recommendations for further evaluation.

## Project Structure

```text
telco-customer-churn-analysis/
├── data/
│   └── Telco-Customer-Churn.csv
├── outputs/
│   ├── 01_churn_distribution.png
│   ├── 02_churn_by_contract.png
│   ├── 03_tenure_by_churn.png
│   ├── 04_tenure_by_churn_band.png
│   ├── 05_monthlycharges_by_churn.png
│   ├── 06_correlation_heatmap.png
│   ├── categorical_feature_summary.csv
│   ├── chi_square_results.csv
│   ├── cleaned_churn_data.csv
│   ├── contract_churn_summary.csv
│   └── tenure_summary.csv
├── analysis.py
├── churn_analysis.ipynb
├── README.md
└── requirements.txt
```

## How to Run

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd telco-customer-churn-analysis
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the notebook

```bash
jupyter notebook churn_analysis.ipynb
```

Alternatively, run the Python script:

```bash
python analysis.py
```

## Author

**Siba Sankar Mallick**

[GitHub Profile](https://github.com/SibaDakshana-12)
