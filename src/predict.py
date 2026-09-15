import joblib
import numpy as np
import pandas as pd
from pathlib import Path


# Get the project root folder
BASE_DIR = Path(__file__).resolve().parents[1]

# Path to the saved model
MODEL_PATH = BASE_DIR / "models" / "dubai_rent_model_small.pkl"

# Load the trained model
model = joblib.load(MODEL_PATH)


def predict_rent(
    beds,
    baths,
    property_type,
    area_sqft,
    furnishing,
    location,
    age_of_listing_in_days
):
    """
    Predict annual rental price in AED.
    """

    data = pd.DataFrame([{
        "Beds": beds,
        "Baths": baths,
        "Type": property_type,
        "Area_in_sqft": area_sqft,
        "Furnishing": furnishing,
        "Location": location,
        "Age_of_listing_in_days": age_of_listing_in_days
    }])

    # Model predicts log(Rent)
    log_prediction = model.predict(data)[0]

    # Convert back to AED
    prediction = np.expm1(log_prediction)

    return prediction


if __name__ == "__main__":

    predicted_rent = predict_rent(
        beds=2,
        baths=2,
        property_type="Apartment",
        area_sqft=1200,
        furnishing="Furnished",
        location="Dubai Marina",
        age_of_listing_in_days=10
    )

    print(f"Predicted Annual Rent: {predicted_rent:,.0f} AED")