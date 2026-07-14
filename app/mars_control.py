import streamlit as st
import random
import csv 
scenarios = [
    {
        "title": "Oxygen Leak",
        "icon": "🫁",
        "message": "Oxygen levels are dropping by 2% every minute.",
        "oxygen": 72,
        "power": 91,
        "temperature": -63
    },
    {
        "title": "🌪️ Dust Storm",
        "message": "A severe dust storm is approaching the habitat.",
        "oxygen": 95,
        "power": 60,
        "temperature": -80
    },
    {
        "title": "⚡ Power Failure",
        "message": "Battery Bank 2 has failed.",
        "oxygen": 88,
        "power": 42,
        "temperature": -55
    }
]

mission = random.choice(scenarios)
# Page title
st.title("🚀 Mars Mission Control Dashboard")

# Mission Information
st.header("Mission Status")

st.write("Mission Day: 42")
st.write("Location: Mars Habitat Alpha")
st.write("Crew Members: 4 Astronauts")

# System Monitoring
st.header("Life Support Systems")

oxygen = mission["oxygen"]
power = mission["power"]
temperature = mission["temperature"]

st.metric("🫁 Oxygen Level", f"{oxygen}%")
st.metric("🔋 Power Level", f"{power}%")
st.metric("🌡️ Outside Temperature", f"{temperature}°C")


# Emergency Alert
st.header("🚨 Emergency Alert")

st.subheader(f'{mission["icon"]} {mission["title"]}')

st.warning(mission["message"])

# Crew Decision
st.header("Crew Decision")

choice = st.radio(
    "What action should the crew take?",
    [
        "Ignore warning",
        "Activate backup oxygen",
        "Evacuate habitat",
        "Wait for instructions from Earth"
    ]
)

st.header("🤖 AI Mission Advisor")

if st.button("Ask AI"):

    if mission["title"] == "Oxygen Leak":
        st.info("""
### AI Recommendation

✔ Activate backup oxygen

Reason:
Oxygen levels are decreasing rapidly.
Activating backup oxygen will stabilize the habitat while diagnostics begin.
""")

    elif mission["title"] == "🌪️ Dust Storm":
        st.info("""
### AI Recommendation

✔ Cancel EVA

Reason:
The approaching dust storm will reduce visibility and power generation.
""")

    elif mission["title"] == "⚡ Power Failure":
        st.info("""
### AI Recommendation

✔ Switch to backup batteries

Reason:
Preserve power for life-support systems until repairs are completed.
""")
if st.button("Submit Decision"):

    with open("data/results.csv", "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            mission["title"],
            choice
        ])

    st.success("Decision saved successfully!")