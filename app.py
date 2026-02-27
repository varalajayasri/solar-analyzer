import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Solar Panel Efficiency Analyzer", layout="wide")

st.title("🌞 Solar Panel Efficiency & Power Generation Analyzer")

st.markdown("This system analyzes solar panel performance, energy generation, savings and environmental impact.")

# ---------------- USER INPUTS ----------------
st.sidebar.header("Enter System Details")

area = st.sidebar.number_input("Panel Area (m²)", min_value=1.0, value=10.0)
irradiance = st.sidebar.number_input("Solar Irradiance (W/m²)", min_value=200.0, value=1000.0)
efficiency = st.sidebar.slider("Panel Efficiency (%)", 5, 30, 18)
temperature = st.sidebar.number_input("Temperature (°C)", min_value=0.0, value=30.0)
sun_hours = st.sidebar.slider("Sunlight Hours per Day", 1, 12, 6)

# ---------------- CALCULATIONS ----------------
efficiency = efficiency / 100

temp_loss = max(0, (temperature - 25) * 0.005)
adjusted_efficiency = efficiency * (1 - temp_loss)

power_output = irradiance * area * adjusted_efficiency
daily_energy = power_output * sun_hours / 1000
monthly_energy = daily_energy * 30
yearly_energy = daily_energy * 365

electricity_rate = 6
yearly_savings = yearly_energy * electricity_rate
co2_reduction = yearly_energy * 0.82

# ---------------- RESULTS ----------------
st.subheader("📊 System Performance Results")

st.write(f"🔋 Adjusted Efficiency: {adjusted_efficiency*100:.2f}%")
st.write(f"⚡ Power Output: {power_output:.2f} W")
st.write(f"📅 Daily Energy: {daily_energy:.2f} kWh")
st.write(f"📆 Monthly Energy: {monthly_energy:.2f} kWh")
st.write(f"📈 Yearly Energy: {yearly_energy:.2f} kWh")
st.write(f"💰 Estimated Yearly Savings: ₹ {yearly_savings:.2f}")
st.write(f"🌱 CO₂ Reduction per Year: {co2_reduction:.2f} kg")

# ---------------- ADVICE ----------------
st.subheader("💡 Recommendations")

if temperature > 35:
    st.warning("High temperature detected. Efficiency decreases at high temperatures. Consider ventilation or cooling systems.")

if sun_hours < 4:
    st.info("Low sunlight hours. Installing panels at optimal tilt angle may improve output.")

if adjusted_efficiency < 0.15:
    st.error("Panel efficiency is low. Upgrading to higher efficiency panels is recommended.")

if adjusted_efficiency >= 0.18:
    st.success("Your system is operating efficiently. Good performance!")

# ---------------- GRAPHS ----------------
st.subheader("📈 Graphical Analysis")

# -------- Graph 1 --------
fig1 = plt.figure()
energy_values = [daily_energy, monthly_energy, yearly_energy]
labels = ["Daily", "Monthly", "Yearly"]
plt.bar(labels, energy_values)
plt.xlabel("Time Period")
plt.ylabel("Energy (kWh)")
plt.title("Energy Production Comparison")
st.pyplot(fig1)

st.markdown("""
**Explanation:**  
This graph compares daily, monthly, and yearly energy production.  
It shows how small daily energy generation accumulates into large annual output, demonstrating long-term benefits of solar installation.
""")

# -------- Graph 2 --------
fig2 = plt.figure()
temp_range = np.arange(0, 60, 1)
eff_range = efficiency * (1 - np.maximum(0, (temp_range - 25) * 0.005))
plt.plot(temp_range, eff_range * 100)
plt.xlabel("Temperature (°C)")
plt.ylabel("Efficiency (%)")
plt.title("Efficiency vs Temperature")
st.pyplot(fig2)

st.markdown("""
**Explanation:**  
This graph shows how solar panel efficiency decreases as temperature increases.  
Panels perform best around 25°C. Higher temperatures cause efficiency loss due to increased internal resistance.
""")

# -------- Graph 3 --------
fig3 = plt.figure()
values = [yearly_savings, co2_reduction]
labels = ["Yearly Savings (₹)", "CO₂ Reduction (kg)"]
plt.bar(labels, values)
plt.title("Financial & Environmental Impact")
st.pyplot(fig3)

st.markdown("""
**Explanation:**  
This graph compares financial savings and environmental benefits.  
It highlights how solar panels not only reduce electricity costs but also significantly decrease carbon emissions annually.
""")

st.markdown("---")
st.markdown("Developed for Renewable Energy Performance Analysis 🌞")