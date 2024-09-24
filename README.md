# Exploratory Data Analysis (EDA) on Customer Purchasing Behavior

## Overview
This project explores customer purchasing behavior in Rossmann stores to understand how factors like promotions, holidays, and competition influence sales. The analysis focuses on cleaning the data, visualizing patterns, and providing insights to support better decision-making.

## Data Cleaning
- **Missing Data**: Handled missing values in `CompetitionDistance`, `PromoInterval`, and other columns with suitable defaults.
- **Outlier Detection**: Identified and treated outliers in `Sales` and `Customers` to prevent skewed analysis.
- **Feature Engineering**: Created time-related features such as `day`, `month`, and `holidays` to capture key effects.

## EDA Insights
- **Promotions**: Promotions generally increased sales, with varying effectiveness across stores.
- **Holidays**: Sales saw significant spikes during Christmas and Easter.
- **Sales-Customer Correlation**: A strong correlation was found between the number of customers and sales.
- **Competitor Impact**: Proximity to competitors slightly reduced sales, especially outside city centers.

## Visualizations
The analysis includes:
- Sales trends over time (before, during, and after holidays)
- Correlation between customers and sales
- Comparison of sales for stores with and without promotions
- Impact of competitor distance on sales

## Logging & Reproducibility
All steps are logged using Python’s `logging` library for traceability. Data cleaning and analysis pipelines are reusable and automated.

## How to Run the Analysis
1. Clone the repository:
    ```bash
    git clone <repo_url>
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Jupyter notebook:
    ```bash
    jupyter notebook eda_customer_behavior.ipynb
    ```

---

This version is formatted as a typical README.md file, making it easy to follow and understand.