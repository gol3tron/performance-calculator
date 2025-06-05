import streamlit as st

st.set_page_config(
    page_title="Aircraft Performance Calculator",
    page_icon="✈️",
    layout="wide"
)

st.title("Aircraft Performance Calculator")
st.sidebar.header("Home")

st.markdown("""
## Welcome to the Aircraft Performance Calculator

This application helps pilots calculate various performance metrics for general aviation aircraft.
Currently focused on the Cessna 172S, this tool provides data-driven calculations for:

### Available Calculators:

- **Takeoff Performance**: Calculate ground roll and distance to clear a 50ft obstacle based on 
  weight, temperature, elevation, wind, and runway conditions.
  
- **Climb Performance**: Calculate climb gradients with interpolated conditions throughout the climb,
  including maximum true airspeed, maximum ground speed, and minimum climb gradient in ft/nm.

- **Cruise Performance**: *(Coming soon)* Calculate fuel flow and speed at various power settings.

### How to Use:

1. Select a calculator from the sidebar menu
2. Enter the required parameters
3. View the calculated results

### Data Sources:

All calculations are based on official Cessna 172S Pilot Operating Handbook data, with interpolation
used for values between published data points.

### Important Notes:

This application is intended for **educational and planning purposes only**. Always refer to the 
official aircraft documentation for flight planning, and include appropriate safety margins for actual operations.
""")

# Footer
st.markdown("---")
st.markdown("© 2025 - Aircraft Performance Calculator - Created by gol3tron")
