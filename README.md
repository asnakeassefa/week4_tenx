### Exploratory Data Analysis (EDA) on Customer Purchasing Behavior
### Task Overview
This project aims to explore customer purchasing behavior in various stores, with a particular focus on how factors like promotions, store openings, and competition affect sales. The insights gained will help guide decision-making for marketing strategies and store operations. The task involves two major steps:

### Data Cleaning
We preprocess the data to handle missing values, outliers, and prepare it for analysis.
### Exploratory Data Analysis (EDA): 
We generate visualizations and statistical summaries to explore trends and relationships in the data.
### Data Cleaning
To ensure high-quality insights, the dataset was cleaned through the following steps:

### Handling Missing Data
Missing values in columns like CompetitionDistance, CompetitionOpenSinceMonth, and PromoInterval were either imputed with logical defaults or flagged with special categories. Missing numeric data was filled with the column mean or mode where appropriate.
Outlier Detection
We used box plots and scatter plots to detect and handle outliers in key numeric columns like Sales and Customers.
### Feature Engineering: 
Date-related features were extracted (e.g., year, month, day of the week, and whether a date falls on a weekend) to provide more granular analysis.
Data Pipeline: A data cleaning pipeline was implemented using Scikit-learn's Pipeline to ensure a reproducible process for handling missing data and scaling numerical features.
### Exploratory Data Analysis (EDA)
Through a series of visualizations and statistical tests, we explored the following key questions:

Promotion Distribution: We compared the distribution of promotions between the training and test sets to ensure they were similarly distributed.
Sales Before, During, and After Holidays: Analyzed the effect of holidays (e.g., Christmas, Easter) on sales behavior.
Seasonal Purchase Behavior: We identified trends in purchasing behavior around key seasonal events.
### Sales vs. Customers: 
We explored the correlation between the number of customers and sales using scatter plots and correlation coefficients.
Effect of Promotions on Sales: We evaluated how promotions influence both customer numbers and sales.
Impact of Store Opening and Closing: Investigated how store hours and weekdays vs. weekend operations impact sales.
Assortment Type and Sales: Examined the effect of different assortment types on store sales.
Competitor Distance: We explored how the distance to a competitor affects store performance, particularly in densely populated areas like city centers.
Effect of Competitor Openings: Analyzed the impact of nearby competitors opening or reopening on store sales.
Key Insights
Promotion Effectiveness: Stores with active promotions showed a significant increase in sales, but the effect was store-dependent.
Holiday Sales Patterns: Holiday periods like Christmas and Easter saw sharp increases in sales, especially for stores with special assortments.
### Customer and Sales Correlation: 
There is a strong positive correlation between the number of customers and sales, indicating that increasing foot traffic drives revenue.
### Competitor Distance: 
Stores closer to competitors tended to have slightly lower sales, but this effect was less pronounced in city center locations.
Logging and Reproducibility
We have implemented logging throughout the data cleaning and analysis process using Python’s logging library. This ensures traceability and allows us to easily reproduce results by tracking each step of the data processing pipeline.

### Visualization
All visualizations were generated using matplotlib and seaborn. These include:

Distribution plots for promotions and holidays
Line charts showing sales trends over time
Scatter plots and correlation matrices for relationships between sales and other features
Bar plots to compare sales with and without promotions