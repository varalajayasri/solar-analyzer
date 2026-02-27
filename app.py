import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Solar Energy Analyzer", layout="wide")

st.title("🌞 Solar Panel Efficiency & Power Generation Analyzer")
st.markdown("Advanced analysis of solar performance, financial savings & system health")

# -------------------------
# SIDEBAR INPUTS
# -------------------------
st.sidebar.header("🔧 System Inputs")

area = st.sidebar.number_input("Panel Area (m²)", min_value=0.1, value=1.6)
irradiance = st.sidebar.number_input("Solar Irradiance (W/m²)", min_value=100.0, value=1000.0)
efficiency = st.sidebar.slider("Panel Efficiency (%)", 5, 30, 18)
temperature = st.sidebar.slider("Panel Temperature (°C)", 0, 60, 25)
sun_hours = st.sidebar.number_input("Sunlight Hours per Day", min_value=1.0, value=5.5)
electricity_rate = st.sidebar.number_input("Electricity Rate (₹/kWh)", value=6.0)
installation_cost = st.sidebar.number_input("Total Installation Cost (₹)", value=80000.0)

# -------------------------
# CALCULATIONS
# -------------------------

eff = efficiency / 100
temp_coefficient = -0.004
adjusted_eff = eff * (1 + temp_coefficient * (temperature - 25))

power_output = area * irradiance * adjusted_eff
daily_energy = power_output * sun_hours / 1000
monthly_energy = daily_energy * 30
yearly_energy = daily_energy * 365

annual_savings = yearly_energy * electricity_rate
co2_saved = yearly_energy * 0.82

# ROI & Payback
if annual_savings > 0:
    payback_period = installation_cost / annual_savings
else:
    payback_period = 0

roi = (annual_savings / installation_cost) * 100 if installation_cost > 0 else 0

# -------------------------
# RESULTS SECTION
# -------------------------

st.subheader("📊 Energy Production")

col1, col2, col3 = st.columns(3)
col1.metric("Power Output (W)", f"{power_output:.2f}")
col2.metric("Daily Energy (kWh)", f"{daily_energy:.2f}")
col3.metric("Yearly Energy (kWh)", f"{yearly_energy:.2f}")

st.subheader("🌍 Environmental Impact")
st.write(f"🌱 CO₂ Saved Per Year: **{co2_saved:.2f} kg**")

st.subheader("💰 Financial Analysis")
st.write(f"💵 Annual Savings: **₹{annual_savings:.2f}**")
st.write(f"📈 ROI: **{roi:.2f}%**")
st.write(f"⏳ Payback Period: **{payback_period:.2f} years**")

# -------------------------
# SYSTEM RATING
# -------------------------

st.subheader("⚙️ System Performance Rating")

if adjusted_eff > 0.19:
    st.success("🟢 Excellent System Performance")
elif adjusted_eff > 0.15:
    st.warning("🟡 Moderate Performance")
else:
    st.error("🔴 Low Performance – Improvement Needed")

# -------------------------
# SMART ADVICE
# -------------------------

st.subheader("💡 Smart Recommendations")

if temperature > 35:
    st.warning("High temperature reduces efficiency. Improve ventilation or cooling.")

if irradiance < 600:
    st.info("Low irradiance detected. Solar trackers can improve sunlight capture.")

if efficiency < 15:
    st.error("Consider upgrading to higher efficiency panels (Monocrystalline).")

if payback_period > 7:
    st.info("Try government subsidies or reduce installation cost for faster ROI.")

if daily_energy > 10:
    st.success("System generating strong daily energy output!")

# -------------------------
# GRAPHS SECTION
# -------------------------

st.subheader("📈 Performance Graphs")

# 1. Temperature vs Efficiency
temps = np.linspace(0, 60, 100)
eff_values = eff * (1 + temp_coefficient * (temps - 25))

plt.figure()
plt.plot(temps, eff_values * 100)
plt.xlabel("Temperature (°C)")
plt.ylabel("Efficiency (%)")
plt.title("Temperature vs Efficiency")
st.pyplot(plt)

# 2. Irradiance vs Power
irr_range = np.linspace(200, 1200, 100)
power_range = area * irr_range * adjusted_eff

plt.figure()
plt.plot(irr_range, power_range)
plt.xlabel("Irradiance (W/m²)")
plt.ylabel("Power Output (W)")
plt.title("Irradiance vs Power Output")
st.pyplot(plt)

# 3. Monthly Energy Projection (Seasonal Variation)
months = np.arange(1, 13)
season_factor = 0.8 + 0.4 * np.sin((months - 1) * np.pi / 6)
monthly_projection = daily_energy * 30 * season_factor

plt.figure()
plt.plot(months, monthly_projection)
plt.xlabel("Month")
plt.ylabel("Energy (kWh)")
plt.title("Estimated Monthly Energy Production")
st.pyplot(plt)

# 4. Savings Growth Over 10 Years
years = np.arange(1, 11)
savings_projection = annual_savings * years

plt.figure()
plt.plot(years, savings_projection)
plt.xlabel("Year")
plt.ylabel("Total Savings (₹)")
plt.title("10-Year Savings Projection")
st.pyplot(plt)

st.markdown("---")
st.markdown("🌞 Developed as a Professional Renewable Energy Engineering Model")