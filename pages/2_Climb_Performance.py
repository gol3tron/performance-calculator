import streamlit as st

import performance_172S as pf

st.set_page_config(
    page_title="Climb Performance",
    page_icon="🛫",
)

st.title("Climb Performance")
st.sidebar.header("Climb Performance")

# Create tabs for different climb calculations
tab1, tab2 = st.tabs(["Climb Gradients", "Climb Performance (Coming Soon)"])

with tab1:
    st.markdown("""
    ## Climb Gradients Calculator
    
    Calculate climb performance including maximum true airspeed, maximum ground speed, 
    and minimum climb gradient based on varying conditions throughout the climb.
    """)
    
    # Create two columns for input parameters
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Altitude & Airspeed")
        
        # Altimeter setting
        altimeter_setting = st.slider(
            "Altimeter setting (in Hg):", 28.00, 31.00, 29.92, 0.01
        )
        
        # Starting altitude
        start_altitude = st.number_input(
            "Starting altitude (ft MSL):", min_value=0, max_value=15000, value=2000, step=100
        )
        
        # Ending altitude  
        end_altitude = st.number_input(
            "Ending altitude (ft MSL):", min_value=0, max_value=15000, value=5000, step=100
        )
        
        # Planned indicated airspeed
        indicated_airspeed = st.slider(
            "Planned indicated airspeed (knots):", 60, 120, 79
        )
        
        st.subheader("Climb Rates")
        
        # Climb rates
        start_climb_rate = st.slider(
            "Rate of climb at starting altitude (ft/min):", 100, 1000, 700, 10
        )
        
        end_climb_rate = st.slider(
            "Rate of climb at ending altitude (ft/min):", 50, 800, 500, 10
        )
    
    with col2:
        st.subheader("Wind Conditions")
        
        # Wind at starting altitude
        start_wind_dir = st.slider(
            "Wind direction at starting altitude (magnetic):", 1, 360, 270
        )
        
        start_wind_speed = st.slider(
            "Wind speed at starting altitude (knots):", 0, 50, 10
        )
        
        # Wind at ending altitude
        end_wind_dir = st.slider(
            "Wind direction at ending altitude (magnetic):", 1, 360, 270
        )
        
        end_wind_speed = st.slider(
            "Wind speed at ending altitude (knots):", 0, 50, 15
        )
        
        st.subheader("Aircraft Heading & Temperature")
        
        # Magnetic headings
        start_heading = st.slider(
            "Magnetic heading at starting altitude:", 1, 360, 90
        )
        
        end_heading = st.slider(
            "Magnetic heading at ending altitude:", 1, 360, 90
        )
        
        # Temperatures
        start_temp = st.slider(
            "Temperature at starting altitude (°C):", -20, 40, 15
        )
        
        end_temp = st.slider(
            "Temperature at ending altitude (°C):", -20, 40, 5
        )
    
    # Validation
    if end_altitude <= start_altitude:
        st.error("Ending altitude must be higher than starting altitude.")
    else:
        # Calculate button
        if st.button("Calculate Climb Gradients", type="primary"):
            try:
                max_tas, max_gs, min_gradient = pf.calculate_climb_gradient(
                    start_altitude,
                    end_altitude, 
                    start_climb_rate,
                    end_climb_rate,
                    indicated_airspeed,
                    start_temp,
                    end_temp,
                    start_wind_dir,
                    start_wind_speed,
                    end_wind_dir,
                    end_wind_speed,
                    start_heading,
                    end_heading,
                    altimeter_setting
                )
                
                # Display results
                st.success("Climb Gradient Calculations Complete!")
                
                # Create three columns for results
                res_col1, res_col2, res_col3 = st.columns(3)
                
                with res_col1:
                    st.metric(
                        "Maximum True Airspeed",
                        f"{max_tas:.1f} knots",
                        help="Highest true airspeed during the climb"
                    )
                
                with res_col2:
                    st.metric(
                        "Maximum Ground Speed", 
                        f"{max_gs:.1f} knots",
                        help="Highest ground speed during the climb"
                    )
                
                with res_col3:
                    st.metric(
                        "Minimum Climb Gradient",
                        f"{min_gradient:.0f} ft/nm",
                        help="Minimum climb gradient over the entire climb"
                    )
                
                # Additional information
                altitude_change = end_altitude - start_altitude
                st.info(f"Climbing {altitude_change:,} feet from {start_altitude:,} to {end_altitude:,} feet MSL")
                
            except Exception as e:
                st.error(f"Calculation error: {str(e)}")
    
    # Information about calculations
    with st.expander("How are these calculations performed?"):
        st.markdown("""
        ### Calculation Methods
        
        This calculator performs the following steps:
        
        1. **Interpolates** all parameters (climb rate, temperature, wind, heading) between starting and ending altitudes
        2. **Samples** the climb at 500-foot intervals to account for changing conditions
        3. **Calculates** true airspeed from indicated airspeed using:
           - Pressure altitude (from altimeter setting and true altitude)
           - Temperature corrections for air density
        4. **Determines** ground speed by applying wind components to true airspeed
        5. **Computes** climb gradient as altitude change divided by ground distance traveled
        
        ### Important Notes
        
        - All calculations assume constant indicated airspeed throughout the climb
        - Wind components are calculated based on the difference between aircraft heading and wind direction
        - Temperature and wind conditions are linearly interpolated between starting and ending altitudes
        - These calculations are for planning purposes only and not a substitute for pilot judgment
        - Add appropriate safety margins for actual flight planning
        """)

with tab2:
    st.markdown("""
    ## Additional Climb Performance Calculator
    
    This section will include additional climb performance calculations such as:
    
    * Time to climb to desired altitude
    * Fuel consumption during climb  
    * Distance traveled during climb
    * Best rate of climb (Vy) speeds at various altitudes
    * Best angle of climb (Vx) speeds
    
    ### Stay tuned for updates!
    """)
    
    # Coming soon image or placeholder
    st.info("🚧 This feature is under development and will be available soon! 🚧")

# Footer
st.markdown("---")
st.markdown("© 2025 - Aircraft Performance Calculator")
