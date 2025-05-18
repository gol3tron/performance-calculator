import streamlit as st

import performance_172S as pf

st.set_page_config(
    page_title="Takeoff Performance",
    page_icon="🛫",
)

st.title("Takeoff Performance")
st.sidebar.header("Takeoff Performance")

st.markdown("""
## Cessna 172S Takeoff Performance Calculator

Calculate the takeoff ground roll and distance to clear a 50-foot obstacle for your Cessna 172S
based on current conditions and aircraft weight.
""")

# Define two columns for input parameters
col1, col2 = st.columns(2)

with col1:
    # Define temperature
    user_temperature = st.slider("Temperature (°C):", 0, 40)

    # Define airport elevation
    user_elevation = st.slider("Airport Elevation (ft MSL):", -500, 10000)

    # Define altimeter setting
    user_altimeter = st.slider(
        "Altimeter setting (in Hg):", 28.00, 31.00, 29.92)

    # Define aircraft weight
    user_weight = st.slider("Aircraft takeoff weight (lbs):", 2200, 2550, 2400)

with col2:
    # Define runway direction
    user_runway = st.slider("Runway heading (degrees):", 1, 360, 360)

    # Define wind direction
    user_wind_direction = st.slider("Wind direction (degrees):", 1, 360, 360)

    # Define wind speed
    user_wind_speed = st.slider("Wind speed (knots):", 0, 40, 0)

    # Define runway surface
    user_surface = st.radio(
        "Runway surface:", ("Dry pavement", "Dry grass")
    )
    user_surface_is_grass = (user_surface == "Dry grass")

# Calculate pressure altitude
pressure_altitude = pf.get_pressure_altitude(user_altimeter, user_elevation)
st.info(f"Pressure altitude is {round(pressure_altitude)} feet.")

# Create two columns for the buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("Calculate Ground Roll", type="primary"):
        user_ground_roll = pf.get_ground_roll_sfto(
            pressure_altitude,
            user_weight,
            user_temperature,
            user_runway,
            user_wind_direction,
            user_wind_speed,
            user_surface_is_grass,
        )
        st.success(
            f"Predicted ground roll of **{round(user_ground_roll)}** feet.")

with col2:
    if st.button("Calculate Distance to Clear 50 ft Obstacle", type="primary"):
        user_dist_50ft = pf.get_dist_50ft_sfto(
            pressure_altitude,
            user_weight,
            user_temperature,
            user_runway,
            user_wind_direction,
            user_wind_speed,
            user_surface_is_grass,
        )
        st.success(
            f"Predicted **{round(user_dist_50ft)}** feet to clear 50 ft obstacle.")

# Information about calculations
with st.expander("How are these calculations performed?"):
    st.markdown("""
    ### Calculation Methods
    
    These calculations are based on data from the Cessna 172S Pilot's Operating Handbook. The application:
    
    1. **Interpolates** between known data points for weight, temperature, and pressure altitude
    2. **Applies adjustments** for:
       - Wind component (headwind or tailwind)
       - Runway surface (paved or grass)
    
    ### Important Notes
    
    - Short field takeoff procedures assume proper technique (flaps 10°, rotation at Vr)
    - Add appropriate safety margins to these numbers for actual flight planning
    - These calculations are for planning purposes only and not a substitute for pilot judgment
    """)

# Footer
st.markdown("---")
st.markdown("© 2025 - Aircraft Performance Calculator")
