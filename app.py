import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from src.predict import predict_rent


# =========================================================
# Paths
# =========================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = BASE_DIR / "data" / "dubai_properties.csv"


# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="Dubai Real Estate AI",
    page_icon="🏠",
    layout="wide"
)


# =========================================================
# Load Data
# =========================================================

@st.cache_data
def load_data():

    df = pd.read_csv(DATA_PATH)

    # Keep Dubai only
    df = df[df["City"] == "Dubai"].copy()

    # Remove invalid rents
    df = df[df["Rent"] >= 5000].copy()

    # Keep realistic bedroom range used by the model
    df = df[df["Beds"] <= 7].copy()

    return df


df = load_data()


# =========================================================
# Sidebar
# =========================================================

st.sidebar.title("🏠 Dubai Real Estate AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Rent Predictor",
        "📊 Market Analysis",
        "🤖 Model Information"
    ]
)


st.sidebar.divider()

st.sidebar.write(
    "Machine Learning project for analyzing and predicting "
    "Dubai rental prices."
)


# =========================================================
# PAGE 1 — RENT PREDICTOR
# =========================================================

if page == "🏠 Rent Predictor":

    st.title("🏠 Dubai Rent Predictor")

    st.write(
        "Enter the property details below to estimate "
        "the annual rental price."
    )

    st.divider()

    # -----------------------------
    # Property Inputs
    # -----------------------------

    st.subheader("Property Details")

    col1, col2, col3 = st.columns(3)

    with col1:

        beds = st.number_input(
            "🛏️ Bedrooms",
            min_value=0,
            max_value=7,
            value=2,
            step=1
        )

        baths = st.number_input(
            "🚿 Bathrooms",
            min_value=1,
            max_value=10,
            value=2,
            step=1
        )

    with col2:

        property_type = st.selectbox(
            "🏢 Property Type",
            [
                "Apartment",
                "Villa",
                "Townhouse",
                "Penthouse",
                "Hotel Apartment"
            ]
        )

        area_sqft = st.number_input(
            "📐 Area (sqft)",
            min_value=100,
            max_value=20000,
            value=1200,
            step=50
        )

    with col3:

        furnishing = st.selectbox(
            "🛋️ Furnishing",
            [
                "Furnished",
                "Unfurnished"
            ]
        )

        location = st.text_input(
            "📍 Location",
            value="Dubai Marina"
        )

        age_of_listing_in_days = st.number_input(
            "📅 Listing Age (days)",
            min_value=0,
            max_value=3650,
            value=10,
            step=1
        )

    st.divider()

    # -----------------------------
    # Prediction
    # -----------------------------

    if st.button(
        "🔮 Predict Rent",
        use_container_width=True
    ):

        predicted_rent = predict_rent(
            beds=beds,
            baths=baths,
            property_type=property_type,
            area_sqft=area_sqft,
            furnishing=furnishing,
            location=location,
            age_of_listing_in_days=age_of_listing_in_days
        )

        monthly_rent = predicted_rent / 12

        st.success("Prediction completed successfully! 🎉")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "💰 Estimated Annual Rent",
                f"{predicted_rent:,.0f} AED"
            )

        with col2:

            st.metric(
                "📅 Estimated Monthly Rent",
                f"{monthly_rent:,.0f} AED"
            )


# =========================================================
# PAGE 2 — MARKET ANALYSIS
# =========================================================

elif page == "📊 Market Analysis":

    st.title("📊 Dubai Rental Market Analysis")

    st.write(
        "Explore rental prices and property characteristics "
        "from the Dubai rental listings dataset."
    )

    st.divider()

    # -----------------------------
    # KPIs
    # -----------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "🏠 Listings",
            f"{len(df):,}"
        )

    with col2:

        st.metric(
            "💰 Median Rent",
            f"{df['Rent'].median():,.0f} AED"
        )

    with col3:

        st.metric(
            "📐 Median Area",
            f"{df['Area_in_sqft'].median():,.0f} sqft"
        )

    with col4:

        st.metric(
            "🛏️ Median Bedrooms",
            f"{df['Beds'].median():.0f}"
        )

    st.divider()

    # -----------------------------
    # Rent Distribution
    # -----------------------------

    st.subheader("💰 Rent Distribution")

    fig, ax = plt.subplots()

    ax.hist(
        df["Rent"],
        bins=50
    )

    ax.set_xlabel("Annual Rent (AED)")
    ax.set_ylabel("Number of Listings")
    ax.set_title("Distribution of Annual Rental Prices")

    st.pyplot(fig)


    # -----------------------------
    # Rent by Property Type
    # -----------------------------

    st.subheader("🏢 Rent by Property Type")

    type_data = (
        df.groupby("Type")["Rent"]
        .median()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots()

    type_data.plot(
        kind="bar",
        ax=ax
    )

    ax.set_xlabel("Property Type")
    ax.set_ylabel("Median Annual Rent (AED)")
    ax.set_title("Median Rent by Property Type")

    plt.xticks(rotation=45)

    st.pyplot(fig)


    # -----------------------------
    # Rent vs Area
    # -----------------------------

    st.subheader("📐 Area vs Rent")

    # Remove extreme outliers for visualization
    chart_data = df[
        (df["Area_in_sqft"] <= 10000) &
        (df["Rent"] <= 1000000)
    ]

    fig, ax = plt.subplots()

    ax.scatter(
        chart_data["Area_in_sqft"],
        chart_data["Rent"],
        alpha=0.3
    )

    ax.set_xlabel("Area (sqft)")
    ax.set_ylabel("Annual Rent (AED)")
    ax.set_title("Relationship Between Area and Rent")

    st.pyplot(fig)


    # -----------------------------
    # Rent by Bedrooms
    # -----------------------------

    st.subheader("🛏️ Rent by Number of Bedrooms")

    bedroom_data = (
        df.groupby("Beds")["Rent"]
        .median()
        .sort_index()
    )

    fig, ax = plt.subplots()

    bedroom_data.plot(
        kind="bar",
        ax=ax
    )

    ax.set_xlabel("Bedrooms")
    ax.set_ylabel("Median Annual Rent (AED)")
    ax.set_title("Median Rent by Number of Bedrooms")

    st.pyplot(fig)


# =========================================================
# PAGE 3 — MODEL INFORMATION
# =========================================================

elif page == "🤖 Model Information":

    st.title("🤖 Machine Learning Model")

    st.write(
        "The final model is a Random Forest Regressor trained "
        "to predict annual rental prices in Dubai."
    )

    st.divider()

    # -----------------------------
    # Model Details
    # -----------------------------

    st.subheader("Model Details")

    st.markdown("""
    **Algorithm:** Random Forest Regressor

    **Target:** Annual Rental Price

    **Target Transformation:** `log1p(Rent)`

    **Number of Trees:** 100

    **Training Data:** Dubai rental listings

    **Features:**

    - Bedrooms
    - Bathrooms
    - Property Type
    - Area in sqft
    - Furnishing
    - Location
    - Listing Age
    """)

    st.divider()

    # -----------------------------
    # Performance
    # -----------------------------

    st.subheader("📈 Model Performance")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "R²",
            "0.816"
        )

    with col2:

        st.metric(
            "MAE",
            "34,262 AED"
        )

    with col3:

        st.metric(
            "RMSE",
            "115,848 AED"
        )

    st.divider()

    st.subheader("Cross-Validation")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "CV R²",
            "0.756"
        )

    with col2:

        st.metric(
            "CV MAE",
            "37,510 AED"
        )

    with col3:

        st.metric(
            "CV RMSE",
            "139,931 AED"
        )

    st.warning(
        "The model performs better on normal and mid-market "
        "rental properties. Luxury properties have higher "
        "prediction errors because they are less common in "
        "the dataset."
    )