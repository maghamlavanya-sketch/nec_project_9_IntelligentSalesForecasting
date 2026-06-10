# Intelligent Sales Forecasting & Inventory Dashboard

## Live Demo

Render Deployment URL:

https://intelligentsalesforecasting.onrender.com

---

## Project Overview

Intelligent Sales Forecasting & Inventory Dashboard is an end-to-end machine learning application built using Python, Streamlit, Scikit-Learn, Pandas, and Plotly.

The system helps businesses analyze historical sales data, forecast future revenue, optimize inventory levels, generate reports, and visualize business performance through interactive dashboards.

Users can either:

* Upload their own sales dataset
* Use the built-in sample dataset

The application automatically processes data, trains machine learning models, generates forecasts, and provides business insights.

---

## Key Features

### Dataset Management

* Upload custom sales dataset
* Use default sample dataset
* Live dataset preview
* Dataset statistics

### Data Preprocessing

* Missing value analysis
* Duplicate detection
* Revenue distribution analysis
* Outlier visualization
* Feature engineering pipeline
* Processed dataset download

### Exploratory Data Analysis (EDA)

* Revenue trends
* Product analysis
* Category performance
* Region performance
* Sales distributions
* Interactive visualizations

### Model Training

* Revenue prediction model
* Train/Test evaluation
* Actual vs Predicted Sales graph
* Model accuracy metrics
* R² Score calculation
* Model saving and loading

### Sales Forecasting

#### Single Revenue Prediction

Predict revenue based on:

* Quantity
* Unit Price
* Month

#### Batch Forecasting

* Forecast multiple records
* CSV-based prediction
* Revenue projections

### Inventory Optimization

#### Manual Inventory Calculator

Calculate:

* Safety Stock
* Reorder Point
* Inventory Status

#### Data Driven Inventory Insights

Generates:

* Product-wise inventory summary
* Average Daily Sales
* Total Quantity Sold
* Average Revenue
* Inventory recommendations

### Reports

Download reports as:

* Excel (.xlsx)
* PDF (.pdf)
* Processed dataset exports

### Executive Dashboard

Business KPIs:

* Total Revenue
* Total Orders
* Product Count
* Region Count

Interactive Analytics:

* Daily Revenue Trend
* Monthly Revenue Trend
* Region Performance
* Top Products
* Leading / Medium / Low Performing Regions
* Revenue Distribution
* Recent Sales Monitoring

Filters:

* Year
* Region
* Category

---

## Machine Learning Model

### Algorithm Used

Random Forest Regressor

### Features

* Quantity
* Unit Price
* Month

### Target

* Revenue

### Evaluation Metric

* R² Score

---

## Technology Stack

### Frontend

* Streamlit

### Data Processing

* Pandas
* NumPy

### Visualization

* Plotly

### Machine Learning

* Scikit-Learn

### Reporting

* OpenPyXL
* ReportLab

---

## Project Structure

```text
IntelligentSalesForecasting/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── default_dataset.csv
│   └── processed_dataset.csv
│
├── models/
│   └── revenue_model.pkl
│
├── ml/
│   ├── predictor.py
│   ├── train_revenue.py
│   └── train_forecast.py
│
├── pages/
│   ├── 1_Dataset.py
│   ├── 2_Preprocessing.py
│   ├── 3_EDA.py
│   ├── 4_ModelTraining.py
│   ├── 5_Forecasting.py
│   ├── 6_Inventory.py
│   ├── 7_Reports.py
│   └── 8_Dashboard.py
│
├── pipelines/
│   ├── preprocessing.py
│   └── feature_engineering.py
│
├── reports/
│   ├── excel_generator.py
│   └── pdf_generator.py
│
└── utils/
    ├── data_manager.py
    ├── charts.py
    └── helpers.py
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/IntelligentSalesForecasting.git
```

### Navigate

```bash
cd IntelligentSalesForecasting
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## Future Enhancements

* XGBoost Forecasting
* Prophet Forecasting
* Real-Time Sales Monitoring
* Demand Forecasting APIs
* Automated Email Reports
* Cloud Database Integration
* Advanced Inventory Optimization

---

## Author

Lavanya Magham

AI / Machine Learning Project
