# 🏙️ Dubai Real Estate Rental Analysis & Rent Prediction

[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-Streamlit-red)](https://dubai-real-estate-project-qyaj55fygmqjpa5e7ttzqr.streamlit.app/)

An end-to-end Machine Learning project for analyzing the Dubai rental market and predicting annual property rent using real-world UAE rental listing data.

## 📌 Overview

This project analyzes rental property listings in Dubai and builds a Machine Learning model to estimate annual rental prices based on property characteristics such as:

- Number of bedrooms
- Number of bathrooms
- Property type
- Property area
- Furnishing status
- Location
- Listing age

The project includes exploratory data analysis, data preprocessing, Machine Learning model development, evaluation, error analysis, and an interactive Streamlit dashboard.

## 🚀 Live Demo

Try the interactive application:

👉 https://dubai-real-estate-project-qyaj55fygmqjpa5e7ttzqr.streamlit.app/

The dashboard includes:

- 🏠 Rent Predictor
- 📊 Market Analysis
- 🤖 Model Information

## 🎯 Project Objectives

- Understand rental price patterns in Dubai.
- Explore the relationship between property characteristics and rent.
- Identify important factors affecting rental prices.
- Build a Machine Learning model for rent prediction.
- Deploy the model as an interactive web application.

## 📊 Dataset

The project uses the **Dubai Real Estate Goldmine, UAE Rental Market Data** dataset from Kaggle.

Source:

https://www.kaggle.com/datasets/azharsaleem/real-estate-goldmine-dubai-uae-rental-market

The dataset contains rental property listings across the UAE and was compiled from Bayut.com.

**License:** Apache 2.0

For this project, the analysis was focused on properties located in Dubai.

## 🧹 Data Preparation

The original dataset contained approximately **73,742 listings**.

The data preparation process included:

- Filtering properties located in Dubai.
- Removing invalid rental prices.
- Removing extremely sparse bedroom categories from the modeling dataset.
- Handling categorical variables using One-Hot Encoding.
- Applying `log1p()` transformation to the rental price target.
- Splitting the dataset into training and testing sets.

Final modeling dataset:

**34,199 Dubai rental listings**

## 🔍 Exploratory Data Analysis

Key findings from the analysis:

- Property area has a strong positive relationship with rental price.
- Location is one of the most important factors affecting rent.
- Villas generally have higher rental prices than apartments.
- Rental prices increase substantially with the number of bedrooms.
- The model performs better on the normal and mid-market segments than on luxury properties.

### Example observations

| Property Type | General Price Level |
|---|---|
| Apartment | Lower |
| Townhouse | Medium |
| Villa | Higher |
| Penthouse | Higher / Luxury |

## 🤖 Machine Learning Model

The final model is a **Random Forest Regressor** trained on the logarithm of annual rent.

### Model Features

- `Beds`
- `Baths`
- `Type`
- `Area_in_sqft`
- `Furnishing`
- `Location`
- `Age_of_listing_in_days`

### Why Random Forest?

Random Forest was selected because it can capture nonlinear relationships between property characteristics and rental prices and works well with a mixture of numerical and categorical features.

## 📈 Model Performance

### Test Set

| Metric | Result |
|---|---:|
| MAE | **34,262 AED** |
| RMSE | **115,848 AED** |
| R² | **0.816** |

### 5-Fold Cross-Validation

| Metric | Average |
|---|---:|
| MAE | **37,510 AED** |
| RMSE | **139,931 AED** |
| R² | **0.756** |

> R² is a goodness-of-fit metric, not prediction accuracy.

## ⚠️ Error Analysis & Limitations

Prediction error increases for very expensive properties.

Mean Absolute Percentage Error by rent segment:

| Annual Rent | MAPE |
|---|---:|
| 0–100K AED | 11.7% |
| 100K–250K AED | 12.0% |
| 250K–500K AED | 14.5% |
| 500K–1M AED | 22.5% |
| 1M+ AED | 26.9% |

The main limitation is the relatively small number of luxury properties compared with the much larger normal-market segment.

Future improvements could include:

- More historical rental data.
- Additional location/geographic features.
- Distance to Metro stations and landmarks.
- Property amenities.
- More advanced gradient boosting models.
- Separate models for luxury and standard properties.

## 🖥️ Streamlit Dashboard

The project includes an interactive Streamlit application with three main sections.

### 🏠 Rent Predictor

Users can enter property details and receive an estimated annual and monthly rental price.

### 📊 Market Analysis

The dashboard provides:

- Rental price distribution
- Median rent by property type
- Area vs. rent analysis
- Median rent by number of bedrooms
- Key market statistics

### 🤖 Model Information

The application displays:

- Model type
- Input features
- Test-set performance
- Cross-validation results
- Model limitations

## 📁 Project Structure

```text
dubai-real-estate-project/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── dubai_properties.csv
│
├── models/
│   └── dubai_rent_model_small.pkl
│
├── notebooks/
│   └── 01_data_analysis.ipynb
│
└── src/
    └── predict.py
   
```

## ⚙️ Run Locally

```text 

### 1. Clone the repository

    git clone https://github.com/sanaddajaa/dubai-real-estate-project.git
    cd dubai-real-estate-project

### 2. Create and activate a virtual environment

    python -m venv venv

Windows:

    venv\Scripts\activate

### 3. Install dependencies

    pip install -r requirements.txt

### 4. Run the Streamlit application

    streamlit run app.py

The application will open in your browser.

```

## 🔮 Future Improvements

```text 

Potential improvements include:

- Geospatial analysis using latitude and longitude.
- Interactive Dubai location maps.
- Property price per square foot analysis.
- Advanced boosting models.
- Hyperparameter optimization.
- Separate models for different property segments.
- Real-time or regularly updated rental data.

```

## 👨‍💻 Author

```text 

**Sanad dajaa**

AI & Data Science Student

Interested in Machine Learning, Data Science, and AI applications in real-world business problems.

---

⭐ If you found this project useful, feel free to explore the repository and try the live application.
