import streamlit as st

import performance_172S as pf

st.markdown("# Takeoff Performance")
st.sidebar.markdown("# Takeoff Performance")


"""
## Cessna 172S
### Define weather/aircraft parameters
"""

# Define temperature
user_temperature = st.slider("Temperature (degC):", 0, 40)

# Define airport elevation
user_elevation = st.slider("Airport Elevation (ft MSL):", -500, 10000)

# Define altimeter setting
user_altimeter = st.slider("Altimeter setting (in Hg):", 28.00, 31.00)

# Define aircraft weight
user_weight = st.slider("Aircraft takeoff weight (pounds):", 2200, 2550)

# Define runway direction
user_runway = st.slider("Runway heading (degrees):", 1, 360)

# Define wind direction
user_wind_direction = st.slider("Wind direction (degrees):", 1, 360)

# Define wind speed
user_wind_speed = st.slider("Wind speed (knots):", 0, 40)

# Define runway surface
user_surface = st.radio(
    "Select a runway surface material:", ("Dry pavement", "Dry grass")
)
if user_surface == "Dry grass":
    user_surface_is_grass = True
else:
    user_surface_is_grass = False

pressure_altitude = pf.get_pressure_altitude(user_altimeter, user_elevation)
st.write(f"Pressure altitude is {round(pressure_altitude)} feet.")


def calc_ground_roll():
    """
    Use user input to calculate required ground roll for short field takeoff.
    """
    user_ground_roll = pf.get_ground_roll_sfto(
        pressure_altitude,
        user_weight,
        user_temperature,
        user_runway,
        user_wind_direction,
        user_wind_speed,
        user_surface_is_grass,
    )
    st.success(f"Predicted ground roll of {round(user_ground_roll)} feet.")


if st.button("Get ground roll"):
    calc_ground_roll()


def calc_dist_50ft():
    """
    Use user input to calculate required distance to clear 50 ft for short field takeoff.
    """
    user_ground_roll = pf.get_dist_50ft_sfto(
        pressure_altitude,
        user_weight,
        user_temperature,
        user_runway,
        user_wind_direction,
        user_wind_speed,
        user_surface_is_grass,
    )
    st.success(f"Predicted {round(user_ground_roll)} feet to clear 50 ft obstacle.")


if st.button("Get distance to clear 50 ft obstacle"):
    calc_dist_50ft()
