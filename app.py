import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

# App title and description
st.set_page_config(page_title="🏡 House Price Predictor", layout="centered")
st.title("🏡 House Price Predictor")
st.markdown("Enter property details below to estimate the **sale price**.")

# Section 1: Basic Property Features
st.markdown("### 📋 General Property Information")
col1, col2, col3 = st.columns(3)

with col1:
    home_and_income = st.selectbox("Home & Income?", [0, 1])
with col2:
    sea_view = st.selectbox("Sea View?", [0, 1])
with col3:
    share_driveway = st.selectbox("Shared Driveway?", [0, 1])

st.markdown("---")

# Section 2: Ratings
st.markdown("### 🏗️ Ratings")

col4, col5 = st.columns(2)
with col4:
    house_condition = st.slider("🏠 House Condition (1 = Poor, 5 = Excellent)", 1, 5, 3)
    slope = st.slider("⛰️ Slope (1 = Flat, 5 = Steep)", 1, 5, 3)
with col5:
    density_rating = st.slider("🏘️ Density (1 = Spacious, 5 = Crowded)", 1, 5, 3)
    school_zone_rating = st.slider("🎓 School Zone (1 = Poor, 5 = Excellent)", 1, 5, 3)

st.markdown("---")

# Section 3: Size Details
st.markdown("### 📐 Property Size & Layout")

col6, col7, col8 = st.columns(3)
with col6:
    bedrooms = st.number_input("Bedrooms", 0, step=1, value=3)
    living_rooms = st.number_input("Living Rooms", 0, step=1, value=1)
with col7:
    bathrooms = st.number_input("Bathrooms", 0, step=1, value=1)
    carparks = st.number_input("Carparks", 0, step=1, value=1)
with col8:
    land_area = st.number_input("Land Area (sqm)", min_value=0.0, value=300.0)
    floor_area = st.number_input("Floor Area (sqm)", min_value=0.0, value=150.0)

st.markdown("---")

# Section 4: Financial & Historical
st.markdown("### 💰 Value & Timing")
capital_value = st.number_input("Capital Value ($)", min_value=0.0, value=1000000.0)
year_built = st.number_input("Year Built", min_value=1800, max_value=2025, value=1970)
distance_to_school = st.number_input("Distance to Nearest School (km)", value=1.0)

sold_year = st.number_input("Sold Year", min_value=2000, max_value=2030, value=2025)
sold_month = st.slider("Sold Month", 1, 12, 5)

st.markdown("---")

# Section 5: Location & Type
st.markdown("### 📍 Location & Type")

col9, col10 = st.columns(2)

with col9:
    suburb = st.radio("Suburb", ["Mairangi Bay", "Other"])
    suburb_mairangi = 1 if suburb == "Mairangi Bay" else 0

with col10:
    property_type = st.radio("Property Type", ["Crosslease", "Freehold", "Townhouse"])
    property_type_crosslease = 1 if property_type == "Crosslease" else 0
    property_type_freehold = 1 if property_type == "Freehold" else 0
    property_type_townhouse = 1 if property_type == "Townhouse" else 0

listing_type = st.radio("Listing Type", ["Auction", "No Auction"])
listing_type_auction = 1 if listing_type == "Auction" else 0
listing_type_no_auction = 1 if listing_type == "No Auction" else 0

# Final Input Dictionary
new_data = {
    'Home_And_Income': home_and_income,
    'House_Condition_Rating': house_condition,
    'Bedrooms': bedrooms,
    'Bathrooms': bathrooms,
    'Living_Rooms': living_rooms,
    'Carparks': carparks,
    'Capital_Value': capital_value,
    'Sea_View': sea_view,
    'Share_Drive_Way': share_driveway,
    'Slope': slope,
    'Density_Rating': density_rating,
    'Land_Area': land_area,
    'Floor_Area': floor_area,
    'School_Zone_Rating': school_zone_rating,
    'Year_built': year_built,
    'Distance_to_School': distance_to_school,
    'Suburb_Mairangi Bay': suburb_mairangi,
    'Property_Type_Crosslease': property_type_crosslease,
    'Property_Type_Freehold': property_type_freehold,
    'Property_Type_Townhouse': property_type_townhouse,
    'Listing_Type_Auction': listing_type_auction,
    'Listing_Type_No Auction': listing_type_no_auction,
    'Sold_Year': sold_year,
    'Sold_Month': sold_month
}

st.markdown("---")

# Prediction
if st.button("🔍 Predict House Price"):
    new_df = pd.DataFrame([new_data])
    prediction = model.predict(new_df)[0]
    st.success(f"💰 Predicted House Price: ${round(prediction):,}")
