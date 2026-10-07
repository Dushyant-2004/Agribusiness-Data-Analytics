Agribusiness Data Analytics
A practical end-to-end data analytics project developed as part of the Junior Data Analyst – Agribusiness Virtual Internship at Yauva Intern.
The project demonstrates how agricultural data can be collected, cleaned, analyzed, visualized, forecasted, evaluated, and converted into strategic recommendations.
Project Overview
This project combines the complete four-week internship workflow into one Python-based analytics project:
- Week 1 – Data Collection, Exploration and Cleaning
- Week 2 – Data Visualization and Reporting
- Week 3 – Predictive Analysis and Trend Forecasting
- Week 4 – Performance Evaluation and Strategic Recommendations
The project uses publicly available agricultural production data and demonstrates an end-to-end approach to data-driven agribusiness decision-making.
Project Objectives
The main objectives of the project are to:
- Prepare agricultural data for reliable analysis
- Identify important production trends and patterns
- Create meaningful agricultural visualizations
- Apply machine learning and time-series forecasting techniques
- Evaluate agribusiness performance using KPIs
- Compare performance against analytical benchmarks
- Generate practical strategic recommendations
- Demonstrate how data analytics can support agribusiness decisions
Week 1 – Data Collection, Exploration and Cleaning
The first stage focuses on preparing agricultural data for analysis.
Activities
- Identify relevant public agricultural data sources
- Load agricultural production data
- Explore dataset structure
- Analyze data types and missing values
- Remove duplicate records
- Handle missing observations
- Convert numerical fields to appropriate data types
- Remove invalid negative values
- Clean text fields
- Prepare a structured dataset for further analysis
Main Output
data/cleaned_agriculture_data.csv
Week 2 – Data Visualization and Reporting
The second stage converts cleaned agricultural data into meaningful visual insights.
Visualizations Generated
1. Top 10 Crops by Production
2. Yearly Agricultural Production Trend
3. Top 10 States by Production
4. Agricultural Data Correlation Heatmap
Purpose
These visualizations help identify:
- Major producing crops
- Major producing states
- Production trends over time
- Relationships between numerical agricultural variables
Visualization Technologies
- Matplotlib
- Seaborn
- Pandas
Week 3 – Predictive Analysis and Trend Forecasting
The third stage applies predictive analytics to historical agricultural production data.
Models Used
Linear Regression
Used as a baseline predictive model for understanding relationships between historical production features and future production.
Random Forest
Used to capture nonlinear relationships between lagged production features and the target variable.
ARIMA
Used as a time-series forecasting model to analyze historical production patterns and generate future production forecasts.
Features Used
- Lag 1 production
- Lag 2 production
- Three-period rolling average
- Historical production
Model Evaluation Metrics
- MAE – Mean Absolute Error
- RMSE – Root Mean Squared Error
- MAPE – Mean Absolute Percentage Error
- R² – Coefficient of Determination
- Bias
Outputs
- data/model_comparison.csv
- data/future_production_forecast.csv
Week 4 – Performance Evaluation and Strategic Recommendations
The final stage evaluates agribusiness performance and converts analytical results into strategic recommendations.
Key Performance Indicators
The project evaluates:
1. Production Efficiency
2. Yield Performance
3. Production Growth
4. Crop Diversity
5. State Coverage
6. Top 10 Crop Production Share
The evaluation framework also discusses broader business indicators such as:
- Market profitability
- Price realization
- Resource productivity
- Post-harvest losses
- Sustainability
KPI Evaluation Process
Agricultural Data
       ↓
KPI Calculation
       ↓
Benchmark Comparison
       ↓
Performance Gap Analysis
       ↓
Strategic Recommendations
       ↓
Ongoing Monitoring
Week 4 Outputs
- data/agribusiness_kpi_results.csv
- data/kpi_benchmark_comparison.csv
- data/strategic_recommendations.csv
- visualizations/kpi_performance_vs_benchmark.png
Benchmarking
The project uses analytical reference benchmarks to demonstrate performance comparison.
Benchmarking considers:
- Historical performance
- Comparable peer performance
- Industry or official references
- Management targets
Benchmark values used in the technical demonstration are clearly treated as illustrative analytical reference values, not as official industry standards.
Complete Data Analytics Workflow
Public Agricultural Data
          ↓
     Data Collection
          ↓
    Data Exploration
          ↓
     Data Cleaning
          ↓
 Exploratory Analysis
          ↓
    Visualization
          ↓
 Feature Engineering
          ↓
 Predictive Modeling
          ↓
 Model Evaluation
          ↓
 Future Forecasting
          ↓
      KPI Analysis
          ↓
 Benchmark Comparison
          ↓
 Performance Evaluation
          ↓
 Strategic Recommendations
Dataset
The project uses a publicly available Indian crop production dataset containing:
- State
- District
- Crop Year
- Season
- Crop
- Area
- Production
Dataset Source
https://raw.githubusercontent.com/dibyendubiswas1998/Crop-Production-Analysis/main/DATA/crop_production.csv
Official Agricultural Data Source
Government of India's Open Government Data Platform:
https://www.data.gov.in/
Other relevant public data sources considered in the internship analysis include:
- FAOSTAT
- India Meteorological Department
- e-NAM
- World Bank Data
Technologies Used
Programming
- Python
Data Analysis
- Pandas
- NumPy
Data Visualization
- Matplotlib
- Seaborn
Machine Learning
- Scikit-learn
Time-Series Forecasting
- Statsmodels
- ARIMA
Development
- Visual Studio Code
- Python Virtual Environment
Version Control
- Git
- GitHub
Project Structure
Agribusiness-Data-Analytics/
│
├── data/
│   ├── cleaned_agriculture_data.csv
│   ├── model_comparison.csv
│   ├── future_production_forecast.csv
│   ├── agribusiness_kpi_results.csv
│   ├── kpi_benchmark_comparison.csv
│   └── strategic_recommendations.csv
│
├── src/
│   ├── __init__.py
│   ├── data_cleaning.py
│   ├── visualization.py
│   ├── forecasting.py
│   └── performance_evaluation.py
│
├── visualizations/
│   ├── top_10_crops_production.png
│   ├── yearly_production_trend.png
│   ├── top_states_production.png
│   ├── correlation_heatmap.png
│   ├── actual_vs_predicted.png
│   ├── future_production_forecast.png
│   └── kpi_performance_vs_benchmark.png
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
Data Cleaning Methodology
The cleaning module performs:
1. Standardizes column names
2. Converts numerical columns to appropriate data types
3. Removes rows with missing critical fields
4. Removes duplicate records
5. Removes negative area values
6. Removes negative production values
7. Cleans text fields
8. Resets dataframe indexes
The cleaned dataset is saved to:
data/cleaned_agriculture_data.csv
Visualization Methodology
The visualization module generates:
Top 10 Crops by Production
Identifies crops with the highest total production.
Yearly Production Trend
Shows changes in total agricultural production over time.
Top 10 States by Production
Compares production across major agricultural states.
Correlation Heatmap
Displays relationships between Crop Year, Area, and Production.
Forecasting Methodology
The forecasting module performs:
1. Crop selection
2. Yearly production aggregation
3. Lag feature creation
4. Rolling average calculation
5. Time-based train/test splitting
6. Linear Regression training
7. Random Forest training
8. ARIMA modeling
9. Model evaluation
10. Future production forecasting
The use of time-based splitting helps prevent future observations from being used to train models for earlier periods.
Model Evaluation
Metric	Purpose
MAE	Measures average absolute prediction error
RMSE	Gives greater weight to larger prediction errors
MAPE	Measures average percentage prediction error
R²	Measures how well the model explains target variation
Bias	Identifies systematic overprediction or underprediction


Model results are saved to:
data/model_comparison.csv
KPI Evaluation Methodology
The Week 4 module calculates and evaluates agricultural performance indicators.
Production Efficiency
Production Efficiency = Production / Area
Measures production relative to cultivated area.
Production Growth
Growth (%) =
((Latest Production - Earlier Production)
 / Earlier Production) × 100
Crop Diversity
Measures the number of distinct crops represented in the dataset.
State Coverage
Measures the number of states represented in the agricultural dataset.
Production Concentration
Measures the share of total production represented by the top producing crops.
Strategic Recommendations
The Week 4 evaluation framework generates recommendations based on identified KPI gaps.
Potential strategic actions include:
- Improving production efficiency
- Investigating yield gaps
- Reducing post-harvest losses
- Improving market price realization
- Monitoring input and resource productivity
- Increasing crop diversification where appropriate
- Establishing regular KPI monitoring
- Combining forecasting with performance evaluation
Recommendations are linked to observed KPI performance and are intended to support practical decision-making.
Generated Outputs
Data Files
- cleaned_agriculture_data.csv
- model_comparison.csv
- future_production_forecast.csv
- agribusiness_kpi_results.csv
- kpi_benchmark_comparison.csv
- strategic_recommendations.csv
Visualization Files
- top_10_crops_production.png
- yearly_production_trend.png
- top_states_production.png
- correlation_heatmap.png
- actual_vs_predicted.png
- future_production_forecast.png
- kpi_performance_vs_benchmark.png
How to Run the Project
1. Clone the Repository
git clone <YOUR_GITHUB_REPOSITORY_URL>
2. Open the Project
cd Agribusiness-Data-Analytics
3. Create a Virtual Environment
python -m venv venv
4. Activate the Environment on Windows PowerShell
venv\Scripts\activate
5. Install Dependencies
pip install -r requirements.txt
6. Run the Complete Project
python main.py
The main.py file controls the complete Weeks 1–4 workflow.
It automatically:
- Loads the public dataset
- Cleans the data
- Saves the cleaned dataset
- Creates visualizations
- Runs predictive models
- Evaluates model performance
- Generates future forecasts
- Calculates agribusiness KPIs
- Compares KPIs against benchmarks
- Generates strategic recommendations
- Saves analytical outputs
Complete Execution Architecture
                    main.py
                       │
       ┌───────────────┼────────────────┐
       ↓               ↓                ↓
data_cleaning.py  visualization.py  forecasting.py
       │               │                │
       └───────────────┼────────────────┘
                       ↓
              performance_evaluation.py
                       │
                       ↓
              Final Analytical Outputs
Practical Applications
The project demonstrates how agricultural analytics can support:
- Crop production planning
- Regional performance comparison
- Historical trend analysis
- Production forecasting
- Resource planning
- Market analysis
- Performance monitoring
- Risk identification
- Strategic decision-making
- Agricultural decision-support systems
Limitations
The current project primarily uses historical crop production data.
Several real-world factors are not directly included in the current predictive implementation, including:
- Rainfall
- Temperature
- Soil characteristics
- Fertilizer usage
- Irrigation data
- Commodity prices
- Market demand
- Extreme weather events
Therefore, the forecasting and KPI outputs should be considered an analytical demonstration rather than official agricultural or financial predictions.
The Week 4 benchmark values are also illustrative reference values used to demonstrate the evaluation methodology.
Future Improvements
The project can be extended by integrating:
- India Meteorological Department weather data
- Rainfall and temperature datasets
- Agricultural market prices
- Soil data
- Fertilizer and irrigation information
- Satellite imagery
- XGBoost
- LSTM networks
- Advanced time-series models
- Power BI dashboards
- Interactive web dashboards
- Real-time agricultural market APIs
- Automated KPI monitoring
Internship Deliverables
The project supports the four internship stages:
Week	Focus	Main Deliverable
Week 1	Data Collection, Exploration & Cleaning	Clean agricultural dataset
Week 2	Data Visualization & Reporting	Agricultural visualizations
Week 3	Predictive Analysis & Forecasting	Model comparison and forecasts
Week 4	Performance Evaluation & Recommendations	KPI evaluation and strategic recommendations




Detailed Word reports for each internship week are submitted separately as required by the internship process.
Author
Dushyant Vasisht
B.Tech – Computer Science & Engineering
SGT University, Gurugram
Project Purpose
This project was developed as a practical demonstration of data analytics, visualization, machine learning, time-series forecasting, performance evaluation, and strategic thinking applied to the agribusiness domain.
It brings together the analytical concepts covered across all four internship tasks into one reproducible Python project.