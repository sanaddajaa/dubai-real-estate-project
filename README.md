# 🏠 Dubai Real Estate Rent Predictor

A machine learning project for analyzing Dubai's rental market
and predicting annual rental prices based on property characteristics.

---

## 📌 Project Overview

This project analyzes rental property listings in Dubai and builds
a machine learning model to estimate annual rental prices.

The project includes:

- Exploratory Data Analysis (EDA)
- Data cleaning
- Feature analysis
- Machine learning model comparison
- Cross-validation
- Error analysis
- Model deployment
- Interactive Streamlit dashboard

---

## 🎯 Problem Statement

Rental prices in Dubai vary significantly depending on:

- Property size
- Number of bedrooms
- Number of bathrooms
- Property type
- Furnishing status
- Location
- Listing age

The goal of this project is to build a machine learning model
that can estimate the annual rental price of a Dubai property.

---

## 📊 Dataset

This project uses the **Dubai Real Estate Goldmine, UAE Rental Market Data**
dataset by Azhar Saleem.

The dataset contains rental property listings across the UAE and was
used for exploratory data analysis and machine learning.

Source:
https://www.kaggle.com/datasets/azharsaleem/real-estate-goldmine-dubai-uae-rental-market

License: Apache 2.0

The dataset is used for educational and portfolio purposes.

## 🧹 Data Preparation

The following steps were performed:

1. Loaded the rental listings dataset.
2. Filtered the data to Dubai.
3. Removed invalid rental prices.
4. Removed properties with more than 7 bedrooms for modeling.
5. Checked missing values.
6. Checked duplicate records.
7. Investigated rental price outliers.
8. Analyzed rental prices by property type and number of bedrooms.

Final modeling dataset:

**34,199 Dubai rental listings**

---

## 🔍 Exploratory Data Analysis

The analysis investigated:

### Rent vs Area

There is a positive relationship between property area
and annual rental price.

The correlation between area and rent was approximately:

**0.50**

### Bedrooms

Rental prices generally increase as the number of bedrooms increases.

### Property Type

Villas and penthouses generally have higher rental prices
than apartments.

### Furnishing

Furnished and unfurnished properties were compared to understand
their effect on rental prices.

---

## 🤖 Machine Learning

Several models and configurations were evaluated.

The final model is:

**Random Forest Regressor**

The target variable was transformed using:

```python
log1p(Rent)