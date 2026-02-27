import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Solar Analyzer", layout="wide")

st.title("🌞 Solar Panel Efficiency & Performance Analyzer")
st.markdown("Analyze solar panel performance, savings, and system health.")

st.sidebar.header("🔧 Input Parameters")

# Sidebar Inputs
area = st.sidebar.number_input("Panel Area (m²)", min_value=0.1, value=1.6)
irradiance = st.sidebar.number_input("Solar Irradiance (W/m²)", min_value=100.0, value=1000.0)
efficiency = st.sidebar.slider("Panel Efficiency (%)", 5, 30, 18)
temperature = st.sidebar.slider("Temperature (°C)", 0, 60, 25)
sun_hours = st.sidebar.number_input("Sunlight Hours per Day", min_value=1.0, value=5.5)
electricity_rate = st.sidebar.number_input("Electricity Rate (₹/kWh)", value=6.0)

# Convert efficiency
eff = efficiency / 100

# Temperature effect
temp_coefficient = -0.004
adjusted_eff = eff * (1 + temp_coefficient * (temperature - 25))

# Calculations
power_output = area * irradiance * adjusted_eff
daily_energy = power_output * sun_hours / 1000
monthly_energy = daily_energy * 30
yearly_energy = daily_energy * 365
annual_savings = yearly_energy * electricity_rate
co2_saved = yearly_energy * 0.82

# Performance Rating
if adjusted_eff > 0.18:
    rating = "🟢 Excellent Performance"
elif adjusted_eff > 0.14:
    rating = "🟡 Moderate Performance"
else:
    rating = "🔴 Low Performance"

# Display Results
st.subheader("📊 System Results")

col1, col2, col3 = st.columns(3)

col1.metric("Power Output (W)", f"{power_output:.2f}")
col2.metric("Daily Energy (kWh)", f"{daily_energy:.2f}")
col3.metric("Yearly Energy (kWh)", f"{yearly_energy:.2f}")

st.markdown("### 🌍 Environmental & Financial Impact")
st.write(f"🌱 CO₂ Saved per Year: **{co2_saved:.2f} kg**")
st.write(f"💰 Annual Savings: **₹{annual_savings:.2f}**")

st.markdown("### ⚙️ System Health Rating")
st.success(rating)

# Smart Advice Section
st.markdown("### 💡 Smart Recommendations")

if temperature > 35:
    st.warning("High temperature detected! Consider installing cooling or proper ventilation.")

if irradiance < 600:
    st.info("Low sunlight intensity. Installing solar trackers may improve output.")

if efficiency < 15:
    st.error("Panel efficiency is low. Consider upgrading to high-efficiency panels.")

if daily_energy > 10:
    st.success("Your system is generating strong daily output!")

# -----------------------------
# 📈 GRAPH SECTION
# -----------------------------

st.markdown("## 📈 Performance Graphs")

# Graph 1: Temperature vs Efficiency
temps = np.linspace(0, 60, 50)
eff_values = eff * (1 + temp_coefficient * (temps - 25))

plt.figure()
plt.plot(temps, eff_values * 100)
plt.xlabel("Temperature (°C)")
plt.ylabel("Efficiency (%)")
plt.title("Temperature vs Efficiency")
st.pyplot(plt)

# Graph 2: Irradiance vs Power Output
irr_range = np.linspace(200, 1200, 50)
power_range = area * irr_range * adjusted_eff

plt.figure()
plt.plot(irr_range, power_range)
plt.xlabel("Solar Irradiance (W/m²)")
plt.ylabel("Power Output (W)")
plt.title("Irradiance vs Power Output")
st.pyplot(plt)

# Graph 3: Monthly Energy Projection
months = np.arange(1, 13)
season_factor = 0.8 + 0.4 * np.sin((months - 1) * np.pi / 6)
monthly_projection = daily_energy * 30 * season_factor

plt.figure()
plt.plot(months, monthly_projection)
plt.xlabel("Month")
plt.ylabel("Energy (kWh)")
plt.title("Estimated Monthly Energy Production")
st.pyplot(plt)

st.markdown("---")
st.markdown("🌞 Developed as an Engineering Working Model for Renewable Energy Analysis")