

# COVID-19 Data Analysis & Power BI Dashboard

## 🌐 Project Overview

The *COVID-19 Data Analysis & Prediction Dashboard* is an end-to-end analytical solution for monitoring, understanding, and forecasting the global progression of the COVID-19 pandemic. This project integrates robust data engineering, exploratory data analysis (EDA), machine learning forecasting, and business intelligence visualization to derive actionable insights that assist researchers, policymakers, and the public in comprehending pandemic trends and preparing for potential future outbreaks.

## 🎯 Objectives

- To consolidate and analyze global COVID-19 time-series data focusing on confirmed, recovered, active, and death cases.  
- To implement predictive models that forecast case trajectories, enabling proactive healthcare and policy planning.  
- To build an interactive, user-friendly dashboard that visualizes key metrics dynamically across countries and timelines.  
- To demonstrate data science best practices in public health analytics and communicate insights effectively.

## 📊 Features & Capabilities

### Data Analysis  
- Time-series exploration of COVID-19 metrics including cumulative and daily counts.  
- Computation of epidemiologically relevant rates such as case fatality rate (CFR) and recovery rate.  
- Identification of temporal patterns, trends, and anomalies at global and country-level granularity.

### Predictive Modeling  
- Machine learning regression models based on scikit-learn predicting future confirmed, recovered, active, and death cases.  
- Model validation through time-based splits to simulate real-world forecasting scenarios and ensure robustness.  
- Visualization of forecasted trends alongside historical data to contextualize predictions.

### Visualization & Dashboard  
- Interactive Power BI dashboard featuring:  
  - Key Performance Indicators (KPIs) with summary statistics.  
  - Trend charts with dynamic slicers for filtering by country and date range.  
  - Bar and pie charts highlighting top 10 most affected countries.  
  - User-friendly interface to facilitate exploratory analysis by non-technical stakeholders.

## 📁 Repository Structure

```
covid19_data_insights/
├─ covid_19_data_analysis.ipynb       # Jupyter Notebook: Detailed data processing, analysis, and modeling  
├─ covid19dashboard.pbix              # Power BI Dashboard file: Interactive visualization and reporting  
├─ images/                           # Repository of screenshots for documentation and demo  
├─ README.md                        # Project documentation and usage guide  
```

## 🛠 Technical Stack

- **Programming:** Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn) for data processing, visualization, and modeling.  
- **Business Intelligence:** Microsoft Power BI for creating interactive dashboards and reports.  
- **Data Sources:** Publicly available COVID-19 datasets from Kaggle, Our World in Data, and Johns Hopkins CSSE repositories ensuring data reliability and completeness.

## 🚀 Installation & Execution Guide

### 1. Clone the Repository  
```bash
git clone https://github.com/s56874/covid19_data_insights.git
cd covid19_data_insights
```

### 2. Install Required Python Packages  
Ensure you have Python 3.7+ installed, then run:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### 3. Run Data Analysis & Prediction Notebook  
- Open `covid_19_data_analysis.ipynb` in Jupyter Notebook or VS Code.  
- Execute the notebook cells sequentially to preprocess data, perform exploratory analyses, and generate forecasts.  

### 4. Launch the Power BI Dashboard  
- Open `covid19dashboard.pbix` with Power BI Desktop.  
- Interact with the dashboard using slicers to explore datasets by country, timeline, and various metrics.

## 🔍 Methodology

### Data Preparation & Cleaning  
- Imported raw time-series datasets detailing COVID-19 case counts by country and date.  
- Performed data imputation for missing values, outlier detection, and normalization where required.  
- Calculated derived metrics such as active cases (`confirmed - recovered - deaths`) and epidemiologically significant rates.

### Exploratory Data Analysis  
- Visualized cumulative and daily trends globally and in key countries using line plots, heatmaps, and distribution plots.  
- Analyzed statistical properties and correlation between different COVID-19 indicators.

### Machine Learning Modeling  
- Selected regression models including Random Forest and Gradient Boosted Trees to predict future case numbers.  
- Feature engineering included lagged variables, moving averages, and calendar effects.  
- Model evaluation involved rolling-origin cross-validation and error metrics like RMSE and MAE.  
- Forecasts visualized to assess alignment with actual outcomes and guide scenario planning.

### Dashboard Visualization  
- Dynamic filtering using Power BI slicers enhances usability across different user segments.  
- Aggregated KPIs summarize pandemic status, while graphical representations reveal intricate temporal and spatial patterns.  
- Dashboard designed for clarity and intuitiveness, facilitating data-driven decisions.

## 📈 Key Insights & Impact

- Monitored and compared COVID-19 impact across countries, highlighting disproportionate effects.  
- Tracked improvement or deterioration in recovery and death rates, providing indicators of healthcare system performance.  
- Forecasts enable anticipation of infection surges, supporting timely interventions.  
- Interactive visuals democratize access to complex epidemiological data for diverse stakeholders.

## 🔜 Future Development

- Automate ingestion of live data via APIs from sources like Our World in Data for real-time updates.  
- Integrate advanced time-series forecasting models such as Prophet or LSTM neural networks to improve prediction accuracy.  
- Extend dashboard to include vaccination data, mobility patterns, and demographic stratification.  
- Incorporate uncertainty quantification and scenario analysis for richer forecasting insights.  
- Strengthen reproducibility by containerizing environment with Docker and adding CI/CD for scheduled updates.

## ⚠️ Limitations & Ethical Considerations

- Forecasts are probabilistic and depend on past trends; unforeseen policy changes or virus mutations may alter future trajectories.  
- Data completeness and reporting standards vary by country, impacting accuracy.  
- The dashboard is a decision-support tool and should be complemented with expert domain knowledge.  
- Responsible data use and privacy considerations observed by using only publicly available aggregated data.

## 🙋♂️ About the Author

Samarth Kokate is a Computer Science Engineering student specializing in Data Science, with a passion for leveraging AI and analytics to tackle public health challenges.

- GitHub: https://github.com/s56874  
- LinkedIn:https://linkedin.com/in/samarth-kokate-b696ab348  
- Email: samarthkokate555@gmail.com

