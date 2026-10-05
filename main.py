import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Smart Energy Manager", page_icon="⚡", layout="wide")

st.title("⚡ Smart Energy Manager")
st.markdown("**SDG 7: Affordable and Clean Energy** 🌍")
st.divider()

st.sidebar.header("🔌 Daily Appliance Usage")
ac_hours = st.sidebar.slider("AC", min_value=0.0, max_value=24.0, value=4.0, step=0.5)
fan_hours = st.sidebar.slider("Fan", min_value=0.0, max_value=24.0, value=8.0, step=0.5)
light_hours = st.sidebar.slider("Light", min_value=0.0, max_value=24.0, value=6.0, step=0.5)
tv_hours = st.sidebar.slider("TV", min_value=0.0, max_value=24.0, value=3.0, step=0.5)

rate = st.sidebar.number_input("Electricity Rate (₹ per kWh)", min_value=1.0, value=7.0, step=0.5)

with st.sidebar.expander("⚙️ Advanced Settings (Wattage)"):
    ac_power = st.number_input("AC Wattage (W)", value=1500)
    fan_power = st.number_input("Fan Wattage (W)", value=75)
    light_power = st.number_input("Light Wattage (W)", value=10)
    tv_power = st.number_input("TV Wattage (W)", value=120)

ac_units = (ac_power * ac_hours * 30) / 1000
fan_units = (fan_power * fan_hours * 30) / 1000
light_units = (light_power * light_hours * 30) / 1000
tv_units = (tv_power * tv_hours * 30) / 1000

total_units = ac_units + fan_units + light_units + tv_units
bill = total_units * rate

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Monthly Energy", value=f"{total_units:.2f} kWh")
with col2:
    st.metric(label="Estimated Monthly Bill", value=f"₹ {bill:.2f}")
with col3:
    if total_units > 300:
        st.error("🔴 High Consumption")
    elif total_units > 150:
        st.warning("🟡 Moderate Consumption")
    else:
        st.success("🟢 Low Consumption")

st.divider()

col_chart, col_insights = st.columns(2)

with col_chart:
    st.subheader("📊 Energy Breakdown")
    data = pd.DataFrame({
        "Appliance": ["AC", "Fan", "Light", "TV"],
        "Consumption (kWh)": [ac_units, fan_units, light_units, tv_units]
    })
    
    if total_units > 0:
        # Simplified chart generation to avoid color library errors
        fig = px.pie(data, values="Consumption (kWh)", names="Appliance", hole=0.4)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Adjust the sliders on the left to see your energy breakdown.")

with col_insights:
    st.subheader("🤖 Smart Recommendation")
    if total_units > 0:
        highest_appliance = data.loc[data["Consumption (kWh)"].idxmax()]
        app_name = highest_appliance["Appliance"]
        app_consumption = highest_appliance["Consumption (kWh)"]
        percentage = (app_consumption / total_units) * 100
        
        st.error(f"**⚠️ Highest Consumer:** {app_name}")
        st.write(f"It uses **{app_consumption:.2f} kWh/month**, making up **{percentage:.1f}%** of your total bill.")
        
        st.write("### 💡 How to reduce it:")
        if app_name == "AC":
            st.write("• Set the AC temperature around 24–26°C.")
            saving = (ac_power * 1 * 30) / 1000
        elif app_name == "Fan":
            st.write("• Turn off the fan when leaving the room.")
            saving = (fan_power * 1 * 30) / 1000
        elif app_name == "Light":
            st.write("• Switch off lights when leaving a room.")
            saving = (light_power * 1 * 30) / 1000
        else:
            st.write("• Turn off the TV instead of leaving it on standby.")
            saving = (tv_power * 1 * 30) / 1000
            
        saving_money = saving * rate
        st.success(f"**💰 Potential Saving:** Reduce {app_name} usage by 1 hour/day to save **{saving:.2f} kWh** (₹ {saving_money:.2f}) monthly!")
