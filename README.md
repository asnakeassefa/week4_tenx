# Insurance Data Analysis

This repository provides a comprehensive analysis of an insurance dataset. The analysis includes **data summarization**, **univariate and bivariate analysis**, **geographical trend comparison**, and **outlier detection**. The goal is to understand trends, relationships, and anomalies in the data, helping improve decision-making and insights into insurance practices.

## Table of Contents
- [Installation](#installation)
- [Data Summarization](#data-summarization)
- [Univariate Analysis](#univariate-analysis)
- [Bivariate/Multivariate Analysis](#bivariate-multivariate-analysis)
- [Data Comparison by Geography](#data-comparison-by-geography)
- [Outlier Detection](#outlier-detection)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/insurance-data-analysis.git
    cd insurance-data-analysis
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

    Required packages include:
    - `pandas`
    - `matplotlib`
    - `seaborn`
    - `numpy`

## Data Summarization

The first step is to calculate **descriptive statistics** and review the **data structure** to understand the variability and formatting of each column.

### Descriptive Statistics
We calculate variability for numerical features such as:
- `TotalPremium`
- `TotalClaims`
- `SumInsured`
- `CalculatedPremiumPerTerm`

Example code:
```python
# Descriptive statistics
df.describe()
