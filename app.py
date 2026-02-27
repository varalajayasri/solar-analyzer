import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("🌞 Solar Panel Efficiency & Power Generation Analyzer")

st.write("Enter the solar panel details below:")

# User Inputs
area = st.number_input("Panel Area (m²)", min_value=0.1, value=1.5)
irradiance = st.number_input("Solar Irradiance (W/m²)", min_value=100.0, value=1000.0)
efficiency = st.slider("Panel Efficiency (%)", 5, 30, 18)
temperature = st.slider("Temperature (°C)", 0, 60, 25)
sun_hours = st.number_input("Sunlight Hours per Day", min_value=1.0, value=5.0)

# Convert efficiency to decimal
eff = efficiency / 100

# Temperature effect (approximate)
temp_coefficient = -0.004  # -0.4% per degree increase
temp_difference = temperature - 25
adjusted_eff = eff * (1 + temp_coefficient * temp_difference)

# Power Calculation
power_output = area * irradiance * adjusted_eff

# Daily Energy
daily_energy = power_output * sun_hours / 1000  # kWh

st.subheader("📊 Results")

st.write(f"🔋 Power Output: {power_output:.2f} Watts")
st.write(f"⚡ Daily Energy Generated: {daily_energy:.2f} kWh")

# Graph for Temperature vs Efficiency
temps = np.linspace(0, 60, 50)
eff_values = eff * (1 + temp_coefficient * (temps - 25))

plt.figure()
plt.plot(temps, eff_values * 100)
plt.xlabel("Temperature (°C)")
plt.ylabel("Efficiency (%)")
plt.title("Temperature vs Efficiency")
st.pyplot(plt)