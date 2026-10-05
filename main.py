print("====================================")
print("       SMART ENERGY MANAGER ⚡")
print("       SDG 7 - CLEAN ENERGY")
print("====================================")

print()

# Electricity rate
rate = 7

# ==============================
# APPLIANCE INPUTS
# ==============================

# AC
print("AC")
ac_power = 1500
ac_hours = float(input("AC is used for how many hours/day: "))
ac_units = (ac_power * ac_hours * 30) / 1000

# Fan
print("\nFan")
fan_power = 75
fan_hours = float(input("Fan is used for how many hours/day: "))
fan_units = (fan_power * fan_hours * 30) / 1000

# Light
print("\nLight")
light_power = 10
light_hours = float(input("Light is used for how many hours/day: "))
light_units = (light_power * light_hours * 30) / 1000

# TV
print("\nTV")
tv_power = 120
tv_hours = float(input("TV is used for how many hours/day: "))
tv_units = (tv_power * tv_hours * 30) / 1000


# ==============================
# TOTAL CONSUMPTION
# ==============================

total_units = ac_units + fan_units + light_units + tv_units

# Electricity bill
bill = total_units * rate


# ==============================
# ENERGY REPORT
# ==============================

print()
print("====================================")
print("          ENERGY REPORT")
print("====================================")

print("AC:", round(ac_units, 2), "kWh/month")
print("Fan:", round(fan_units, 2), "kWh/month")
print("Light:", round(light_units, 2), "kWh/month")
print("TV:", round(tv_units, 2), "kWh/month")

print("------------------------------------")

print("Total Energy:", round(total_units, 2), "kWh/month")
print("Estimated Bill: ₹", round(bill, 2))


# ==============================
# SMART RECOMMENDATION SYSTEM
# ==============================

print()
print("====================================")
print("       🤖 SMART RECOMMENDATION")
print("====================================")

# Store appliance data
appliances = {
    "AC": ac_units,
    "Fan": fan_units,
    "Light": light_units,
    "TV": tv_units
}

# Find highest-consuming appliance
highest_appliance = max(appliances, key=appliances.get)
highest_consumption = appliances[highest_appliance]

# Calculate percentage contribution
percentage = (highest_consumption / total_units) * 100


print()
print("⚠️ HIGHEST ENERGY CONSUMPTION")
print("------------------------------------")
print(highest_appliance, "is consuming the most energy.")
print("Consumption:", round(highest_consumption, 2), "kWh/month")
print("Share of total consumption:", round(percentage, 1), "%")


# ==============================
# SMART SAVING SUGGESTIONS
# ==============================

print()
print("💡 HOW TO REDUCE IT")
print("------------------------------------")

if highest_appliance == "AC":

    print("• Set the AC temperature around 24–26°C.")
    print("• Reduce AC usage by 1 hour/day.")
    print("• Keep doors and windows closed while AC is running.")
    
    saving = (ac_power * 1 * 30) / 1000

elif highest_appliance == "Fan":

    print("• Turn off the fan when leaving the room.")
    print("• Use the fan only when required.")
    print("• Use natural ventilation whenever possible.")
    
    saving = (fan_power * 1 * 30) / 1000

elif highest_appliance == "Light":

    print("• Switch off lights when leaving a room.")
    print("• Use natural daylight whenever possible.")
    print("• Replace old bulbs with energy-efficient LED bulbs.")
    
    saving = (light_power * 1 * 30) / 1000

else:

    print("• Turn off the TV instead of leaving it on standby.")
    print("• Reduce unnecessary screen time.")
    print("• Use the TV's energy-saving mode.")
    
    saving = (tv_power * 1 * 30) / 1000


# ==============================
# POTENTIAL SAVING
# ==============================

print()
print("💰 POTENTIAL SAVING")
print("------------------------------------")

saving_money = saving * rate

print("If you reduce", highest_appliance, "usage by 1 hour/day:")
print("Energy saved:", round(saving, 2), "kWh/month")
print("Money saved: ₹", round(saving_money, 2), "/month")


# ==============================
# OVERALL ENERGY STATUS
# ==============================

print()
print("====================================")
print("          ENERGY STATUS")
print("====================================")

if total_units > 300:
    print("🔴 HIGH ENERGY CONSUMPTION")
    print("Your household should take immediate steps")
    print("to reduce unnecessary electricity usage.")

elif total_units > 150:
    print("🟡 MODERATE ENERGY CONSUMPTION")
    print("Your consumption is moderate.")
    print("Small changes can reduce your electricity bill.")

else:
    print("🟢 LOW ENERGY CONSUMPTION")
    print("Great! Your energy usage is relatively efficient.")


print()
print("====================================")
print("🌱 USE ENERGY RESPONSIBLY!")
print("SDG 7: Affordable and Clean Energy")
print("====================================")
