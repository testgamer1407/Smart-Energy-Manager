import streamlit as st
import pandas as pd
import plotly.express as px

# ==============================
# PAGE CONFIGURATION
# ==============================
st.set_page_config(page_title="Smart Energy Manager", page_icon="⚡", layout="wide")

# ==============================
# HEADER
# ==============================
st.title("⚡ Smart Energy Manager")
st.markdown("**SDG 7: Affordable and Clean Energy** 🌍")
st.write("Track your household appliance usage, identify energy drains, and get smart recommendations to lower your electricity bill and carbon footprint.")
st.divider()

# ==============================
# SIDEBAR - USER INPUTS
# ==============================
st.sidebar.header("🔌 Daily Appliance Usage")
st.sidebar.write("Adjust the hours each appliance is used per day:")

ac_hours = st.sidebar.slider("AC", min_value=0.0, max_value=24.0, value=4.0, step=0.5)
fan_hours = st.sidebar.slider("Fan", min_value=0.0, max_value=24.0, value=8.0, step=0.5)
light_hours = st.sidebar.slider("Light", min_value=0.0, max_value=24.0, value=6.0, step=0.5)
tv_hours = st.sidebar.slider("TV", min_value=0.0, max_value=24.0, value=3.0, step=0.5)

st.sidebar.divider()
rate = st.sidebar.number_input("Electricity Rate (₹ per kWh)", min_value=1.0, value=7.0, step=0.5)

# SMARTER FEATURE: Let users adjust the power of their specific appliances
with st.sidebar.expander("⚙️ Advanced Settings (Wattage)"):
    ac_power = st.number_input("AC Wattage (W)", value=1500)
    fan_power = st.number_input("Fan Wattage (W)", value=75)
    light_power = st.number_input("Light Wattage (W)", value=10)
    tv_power = st.number_input("TV Wattage (W)", value=120)

# ==============================
# CALCULATIONS
# ==============================
ac_units = (ac_power * ac_hours * 30) / 1000
fan_units = (fan_power * fan_hours * 30) / 1000
light_units = (light_power * light_hours * 30) / 1000
tv_units = (tv_power * tv_hours * 30) / 1000

total_units = ac_units + fan_units + light_units + tv_units
bill = total_units * rate

# ==============================
# DASHBOARD UI
# ==============================
# Top row metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Monthly Energy", value=f"{total_units:.2f} kWh")
with col2:
    st.metric(label="Estimated Monthly Bill", value=f"₹ {bill:.2f}")
with col3:
    # Energy Status Indicator
    if total_units > 300:
        st.error("🔴 High Consumption")
    elif total_units > 150:
        st.warning("🟡 Moderate Consumption")
    else:
        st.success("🟢 Low Consumption")

st.divider()

# Middle row: Charts and Insights
col_chart, col_insights = st.columns(2)

with col_chart:
    st.subheader("📊 Energy Breakdown")
    
    # Create a Pandas DataFrame for the chart
    data = pd.DataFrame({
        "Appliance": ["AC", "Fan", "Light", "TV"],
        "Consumption (kWh)": [ac_units, fan_units, light_units, tv_units]
    })
    
    # Generate an interactive Donut chart using Plotly
    if total_units > 0:
        fig = px.pie(data, values="Consumption (kWh)", names="Appliance", hole=0.4, 
                     color_discrete_sequence=px.colors.sequential.Teal)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Adjust the sliders on the left to see your energy breakdown.")

with col_insights:
    st.subheader("🤖 Smart Recommendation")
    
    if total_units > 0:
        # Find highest-consuming appliance
        highest_appliance = data.loc[data["Consumption (kWh)"].idxmax()]
        app_name = highest_appliance["Appliance"]
        app_consumption = highest_appliance["Consumption (kWh)"]
        percentage = (app_consumption / total_units) * 100
        
        st.error(f"**⚠️ Highest Consumer:** {app_name}")
        st.write(f"It uses **{app_consumption:.2f} kWh/month**, making up **{percentage:.1f}%** of your total bill.")
        
        st.write("### 💡 How to reduce it:")
        if app_name == "AC":
            st.write("• Set the AC temperature around 24–26°C.")
            st.write("• Keep doors and windows closed while running.")
            saving = (ac_power * 1 * 30) / 1000
        elif app_name == "Fan":
            st.write("• Turn off the fan when leaving the room.")
            st.write("• Use natural ventilation whenever possible.")
            saving = (fan_power * 1 * 30) / 1000
        elif app_name == "Light":
            st.write("• Switch off lights when leaving a room.")
            st.write("• Replace old bulbs with energy-efficient LED bulbs.")
            saving = (light_power * 1 * 30) / 1000
        else:
            st.write("• Turn off the TV instead of leaving it on standby.")
            st.write("• Use the TV's energy-saving mode.")
            saving = (tv_power * 1 * 30) / 1000
            
        saving_money = saving * rate
        st.success(f"**💰 Potential Saving:** If you reduce {app_name} usage by just 1 hour/day, you will save **{saving:.2f} kWh** (₹ {saving_money:.2f}) every month!")

# Footer
st.markdown("---")
st.caption("🌱 Developed for the Hackathon | Building a sustainable future, one watt at a time.")
