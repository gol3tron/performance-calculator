import streamlit as st

import performance_172S as pf

st.write(
    """
         # Short Field Takeoff Performance Calculator
         ## Cessna 172S
         ### Adam Goler CFI/I, PhD
         #### adam@abcflight.school
         """
)
st.write("---")

st.write(
    """
        ### Define weather/aircraft parameters
        """
)

# Define temperature
user_temperature = st.slider("Temperature (degC):", 0, 40)

# Define airport elevation
user_elevation = st.slider("Airport Elevation (ft MSL):", -500, 10000)

# Define altimeter setting
user_altimeter = st.slider("Altimeter setting (in Hg):", 28.00, 31.00)

# Define aircraft weight
user_weight = st.slider("Aircraft takeoff weight (pounds):", 2200, 2550)

st.write("Calculate ground roll:")

pressure_altitude = pf.get_pressure_altitude(user_altimeter, user_elevation)
ground_roll = 0


def calc_ground_roll():
    ground_roll = pf.get_ground_roll_sfto(
        pressure_altitude, user_weight, user_temperature
    )
    st.success(f"Predicted ground roll of {ground_roll}")


if st.button("Get ground roll!"):
    calc_ground_roll()
