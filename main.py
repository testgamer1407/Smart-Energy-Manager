import streamlit as st

# ==============================
# APP CONFIGURATION
# ==============================
st.set_page_config(page_title="Smart Energy Manager", page_icon="⚡", layout="centered")

st.title("⚡ SMART ENERGY MANAGER")
st.markdown("### 🌍 SDG 7 - Affordable and Clean Energy")
st.divider()

# Electricity rate
rate = 7

# ==============================
# APPLIANCE INPUTS
# ==============================
st.header("📊 Appliance Inputs")
st.write("Enter the number of hours each appliance is used per day:")

# Using columns to make the layout look like a dashboard
col1, col2 = st.columns(2)

with col1:
    ac_hours = st.number_input("❄️ AC (1500W)", min_value=0.0, max_value=24.0, value=5.0, step=0.5)
    fan_hours = st.number_input("🌀 Fan (75W)", min_value=0.0, max_value=24.0, value=8.0, step=0.5)

with col2:
    light_hours = st.number_input("💡 Light (10W)", min_value=0.0, max_value=24.0, value=6.0, step=0.5)
    tv_hours = st.number_input("📺 TV (120W)", min_value=0.0, max_value=24.0, value=3.0, step=0.5)

# Calculate units (kWh/month)
ac_power = 1500
fan_power = 75
light_power = 10
tv_power = 120

ac_units = (ac_power * ac_hours * 30) / 1000
fan_units = (fan_power * fan_hours * 30) / 1000
light_units = (light_power * light_hours * 30) / 1000
tv_units = (tv_power * tv_hours * 30) / 1000

total_units = ac_units + fan_units + light_units + tv_units
bill = total_units * rate

# ==============================
# CALCULATE BUTTON
# ==============================
if st.button("Calculate Energy Usage", type="primary"):
    
    st.divider()
    
    # ==============================
    # ENERGY REPORT
    # ==============================
    st.header("📋 Energy Report")
    
    # Display individual metrics in a row
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("AC", f"{round(ac_units, 2)} kWh")
    m2.metric("Fan", f"{round(fan_units, 2)} kWh")
    m3.metric("Light", f"{round(light_units, 2)} kWh")
    m4.metric("TV", f"{round(tv_units, 2)} kWh")
    
    st.write("") # Spacing
    
    # Display total metrics
    c1, c2 = st.columns(2)
    c1.metric("Total Energy", f"{round(total_units, 2)} kWh/month")
    c2.metric("Estimated Bill", f"₹ {round(bill, 2)}")

    st.divider()
    
    # ==============================
    # SMART RECOMMENDATION SYSTEM
    # ==============================
    st.header("🤖 Smart Recommendation")
    
    appliances = {
        "AC": {"units": ac_units, "power": ac_power},
        "Fan": {"units": fan_units, "power": fan_power},
        "Light": {"units": light_units, "power": light_power},
        "TV": {"units": tv_units, "power": tv_power}
    }
    
    highest_appliance = max(appliances, key=lambda x: appliances[x]["units"])
    highest_consumption = appliances[highest_appliance]["units"]
    appliance_power = appliances[highest_appliance]["power"]
    
    # Avoid division by zero if all inputs are 0
    if total_units > 0:
        percentage = (highest_consumption / total_units) * 100
    else:
        percentage = 0
        
    st.warning(f"⚠️ **{highest_appliance}** is consuming the most energy ({round(percentage, 1)}% of total).")
    
    st.subheader("💡 How to Reduce It")
    if highest_appliance == "AC":
        st.write("• Set the AC temperature around 24–26°C.")
        st.write("• Reduce AC usage by 1 hour/day.")
        st.write("• Keep doors and windows closed while AC is running.")
    elif highest_appliance == "Fan":
        st.write("• Turn off the fan when leaving the room.")
        st.write("• Use the fan only when required.")
        st.write("• Use natural ventilation whenever possible.")
    elif highest_appliance == "Light":
        st.write("• Switch off lights when leaving a room.")
        st.write("• Use natural daylight whenever possible.")
        st.write("• Replace old bulbs with energy-efficient LED bulbs.")
    else:
        st.write("• Turn off the TV instead of leaving it on standby.")
        st.write("• Reduce unnecessary screen time.")
        st.write("• Use the TV's energy-saving mode.")
        
    saving = (appliance_power * 1 * 30) / 1000
    saving_money = saving * rate
    
    st.info(f"**💰 Potential Saving:** If you reduce **{highest_appliance}** usage by 1 hour/day, you save **{round(saving, 2)} kWh** (₹ {round(saving_money, 2)}) per month!")
    
    st.divider()
    
    # ==============================
    # OVERALL ENERGY STATUS
    # ==============================
    st.header("📈 Overall Energy Status")
    
    if total_units > 300:
        st.error("🔴 **HIGH ENERGY CONSUMPTION**\n\nYour household should take immediate steps to reduce unnecessary electricity usage.")
    elif total_units > 150:
        st.warning("🟡 **MODERATE ENERGY CONSUMPTION**\n\nYour consumption is moderate. Small changes can reduce your electricity bill.")
    else:
        st.success("🟢 **LOW ENERGY CONSUMPTION**\n\nGreat! Your energy usage is relatively efficient.")
        
    st.caption("🌱 USE ENERGY RESPONSIBLY! | SDG 7: Affordable and Clean Energy")
