import streamlit as st
import pickle
import numpy as np

# Load the model and dataset
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# Page configuration
st.set_page_config(page_title="Laptop Price Predictor", layout="centered")

# Sidebar
st.sidebar.title("Laptop Configuration")
st.sidebar.write("Fill in the details below to predict the laptop price.")

# Form for input
with st.form("laptop_form"):
    col1, col2 = st.columns(2)

    with col1:
        company = st.selectbox("Brand", df["Company"].unique())
        type_ = st.selectbox("Type", df["TypeName"].unique())
        ram = st.selectbox("RAM (GB)", [2, 4, 6, 8, 12, 16, 24, 32, 64])
        weight = st.number_input("Weight (kg)", min_value=0.5, max_value=5.0, step=0.1)
        cpu = st.selectbox("Processor", df["Cpu brand"].unique())

    with col2:
        touchscreen = st.radio("Touchscreen", ["No", "Yes"])
        ips = st.radio("IPS Display", ["No", "Yes"])
        screen_size = st.slider("Screen Size (inches)", 10.0, 18.0, 15.6)
        resolution = st.selectbox("Resolution", [
            "1920x1080", "1366x768", "1600x900", "3840x2160", 
            "3200x1800", "2880x1800", "2560x1600", "2560x1440", "2304x1440"
        ])
        gpu = st.selectbox("Graphics Card", df["Gpu brand"].unique())
    
    hdd = st.selectbox("HDD (GB)", [0, 128, 256, 512, 1024, 2048])
    ssd = st.selectbox("SSD (GB)", [0, 8, 128, 256, 512, 1024])
    os = st.selectbox("Operating System", df["os"].unique())

    # Submit button
    submitted = st.form_submit_button("Predict Price")

# Prediction
if submitted:
    # Processing inputs
    touchscreen = 1 if touchscreen == "Yes" else 0
    ips = 1 if ips == "Yes" else 0
    X_res, Y_res = map(int, resolution.split("x"))
    ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size

    # Prepare input array
    query = np.array([company, type_, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os]).reshape(1, -1)

    # Make prediction
    predicted_price = int(np.exp(pipe.predict(query)[0]))

    # Display result
    st.subheader("Predicted Laptop Price")
    st.metric(label="Estimated Price", value=f"{predicted_price}")

