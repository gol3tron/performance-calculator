import streamlit as st
import pandas as pd
import performance_172S as pf
import tables_172S as tb

st.set_page_config(
    page_title="Cruise Performance",
    page_icon="✈️",
)

st.title("Cruise Performance")
st.sidebar.header("Cruise Performance")

st.markdown("""
## Cruise Performance Calculator

Calculate cruise performance including true airspeed, fuel flow, and endurance 
based on your aircraft's power settings and flight conditions.
""")

# Create tabs for different input methods
tab1, tab2 = st.tabs(["Built-in Data", "Custom Performance Data"])

with tab1:
    st.subheader("Using Built-in Cessna 172S Data")
    
    # Create two columns for inputs
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Flight Conditions")
        
        # Altitude input
        cruise_altitude = st.number_input(
            "Cruise altitude (ft MSL):",
            min_value=0,
            max_value=15000,
            value=4000,
            step=100,
            help="Enter your desired cruise altitude in feet MSL"
        )
        
        # Temperature mode toggle
        temp_mode = st.radio(
            "Temperature input mode:",
            ["True temperature (°C)", "ISA deviation (°C)"],
            help="Choose between absolute temperature or deviation from standard atmosphere"
        )
        
        # Temperature input based on mode
        if temp_mode == "True temperature (°C)":
            outside_air_temp = st.slider(
                "Outside air temperature (°C):",
                min_value=-40,
                max_value=40,
                value=15,
                help="Predicted outside air temperature at cruise altitude"
            )
        else:
            # ISA deviation mode
            isa_deviation = st.slider(
                "ISA deviation (°C):",
                min_value=-30,
                max_value=30,
                value=0,
                help="Temperature difference from standard atmosphere (positive = warmer than standard)"
            )
            # Calculate ISA standard temperature at altitude
            isa_standard_temp = 15 - (1.98 * cruise_altitude / 1000)
            outside_air_temp = isa_standard_temp + isa_deviation
            st.info(f"ℹ️ ISA standard temperature at {cruise_altitude} ft: {isa_standard_temp:.1f}°C")
            st.info(f"ℹ️ Actual temperature: {outside_air_temp:.1f}°C")
        
        # Altimeter setting
        altimeter_setting = st.number_input(
            "Altimeter setting (inHg):",
            min_value=28.00,
            max_value=31.00,
            value=29.92,
            step=0.01,
            format="%.2f",
            help="Current altimeter setting"
        )
        
        st.subheader("Power Settings")
        
        # Manifold pressure toggle
        use_manifold_pressure = st.checkbox(
            "Aircraft has manifold pressure gauge",
            value=True,
            help="Uncheck this if your aircraft does not have a manifold pressure gauge (e.g., fixed-pitch propeller aircraft)"
        )
        
        # Conditional manifold pressure input
        if use_manifold_pressure:
            manifold_pressure = st.slider(
                "Manifold pressure (inHg):",
                min_value=18.0,
                max_value=25.0,
                value=22.0,
                step=0.1,
                help="Desired manifold pressure setting"
            )
        else:
            manifold_pressure = None
            st.info("ℹ️ Performance will be calculated based on RPM, altitude, and temperature only.")
        
        # RPM
        rpm = st.slider(
            "Engine RPM:",
            min_value=2000,
            max_value=2700,
            value=2400,
            step=50,
            help="Desired engine RPM"
        )
    
    with col2:
        st.subheader("Fuel Planning")
        
        # Total fuel
        total_fuel = st.number_input(
            "Total usable fuel (gallons):",
            min_value=0.0,
            max_value=100.0,
            value=50.0,
            step=1.0,
            help="Total usable fuel available at departure"
        )
        
        # Reserve fuel method
        reserve_method = st.radio(
            "Reserve fuel method:",
            ["Fuel quantity (gallons)", "Time (hours)"],
            help="Choose how to specify fuel reserves"
        )
        
        if reserve_method == "Fuel quantity (gallons)":
            reserve_fuel = st.number_input(
                "Reserve fuel (gallons):",
                min_value=0.0,
                max_value=50.0,
                value=10.0,
                step=1.0,
                help="Fuel to keep in reserve"
            )
            reserve_hours = 0.0
        else:
            reserve_hours = st.number_input(
                "Reserve time (hours):",
                min_value=0.0,
                max_value=3.0,
                value=0.5,
                step=0.1,
                help="Time to keep as reserve"
            )
            reserve_fuel = 0.0
    
    # Calculate button
    if st.button("Calculate Cruise Performance", type="primary"):
        try:
            # Calculate cruise performance
            true_airspeed, fuel_flow = pf.calculate_cruise_performance(
                cruise_altitude,
                outside_air_temp,
                rpm,
                altimeter_setting,
                manifold_pressure
            )
            
            # Calculate endurance
            total_endurance, usable_endurance = pf.calculate_endurance(
                total_fuel,
                reserve_fuel,
                fuel_flow,
                reserve_hours
            )
            
            # Display results
            st.success("✈️ Cruise Performance Calculated!")
            
            # Create results columns
            res_col1, res_col2, res_col3 = st.columns(3)
            
            with res_col1:
                st.metric(
                    "True Airspeed",
                    f"{true_airspeed:.1f} knots",
                    help="True airspeed at the specified power setting and conditions"
                )
            
            with res_col2:
                st.metric(
                    "Fuel Flow",
                    f"{fuel_flow:.1f} GPH",
                    help="Fuel burn rate in gallons per hour"
                )
            
            with res_col3:
                st.metric(
                    "Usable Endurance",
                    f"{usable_endurance:.1f} hours",
                    help="Flight time available excluding reserves"
                )
            
            # Additional details
            st.subheader("Additional Details")
            
            detail_col1, detail_col2 = st.columns(2)
            
            with detail_col1:
                st.write(f"**Total Endurance:** {total_endurance:.1f} hours")
                st.write(f"**Range (approximate):** {(true_airspeed * usable_endurance):.0f} nautical miles")
                st.write(f"**Pressure Altitude:** {pf.get_pressure_altitude(altimeter_setting, cruise_altitude):.0f} feet")
            
            with detail_col2:
                st.write(f"**Fuel at Destination:** {(total_fuel - fuel_flow * usable_endurance):.1f} gallons")
                if reserve_method == "Fuel quantity (gallons)":
                    st.write(f"**Reserve Fuel:** {reserve_fuel:.1f} gallons")
                else:
                    st.write(f"**Reserve Time:** {reserve_hours:.1f} hours")
                st.write(f"**Fuel per NM:** {(fuel_flow / true_airspeed):.2f} gallons/NM")
            
        except Exception as e:
            st.error(f"Calculation error: {str(e)}")
            st.error("Please check your input values and try again.")

with tab2:
    st.subheader("Custom Performance Data Entry")
    
    st.markdown("""
    Enter your aircraft's performance data from the Pilot's Operating Handbook.
    This allows you to use data specific to your aircraft and configuration.
    """)
    
    # Performance data table entry
    st.subheader("Performance Chart Data")
    
    # Create a simple data entry form
    with st.expander("📊 Enter Performance Data", expanded=True):
        st.markdown("**Note:** This is a simplified data entry. Enter base performance values:")
        
        data_col1, data_col2 = st.columns(2)
        
        with data_col1:
            base_altitude = st.number_input(
                "Reference altitude (ft):",
                min_value=0,
                max_value=15000,
                value=2000,
                step=100
            )
            
            base_temperature = st.number_input(
                "Reference temperature (°C):",
                min_value=-40,
                max_value=40,
                value=15
            )
            
            # Manifold pressure toggle for custom data
            custom_use_mp = st.checkbox(
                "Include manifold pressure in custom data",
                value=True,
                key="custom_mp_toggle",
                help="Uncheck if your aircraft performance data doesn't include manifold pressure"
            )
            
            if custom_use_mp:
                base_mp = st.number_input(
                    "Reference manifold pressure (inHg):",
                    min_value=18.0,
                    max_value=25.0,
                    value=22.0,
                    step=0.1
                )
            else:
                base_mp = None
                st.info("ℹ️ Custom performance data will be based on RPM only.")
        
        with data_col2:
            base_rpm = st.number_input(
                "Reference RPM:",
                min_value=2000,
                max_value=2700,
                value=2400,
                step=50
            )
            
            base_tas = st.number_input(
                "True airspeed (knots):",
                min_value=80.0,
                max_value=200.0,
                value=120.0,
                step=1.0
            )
            
            base_fuel_flow = st.number_input(
                "Fuel flow (GPH):",
                min_value=5.0,
                max_value=20.0,
                value=8.5,
                step=0.1
            )
    
    # Flight conditions for custom data
    st.subheader("Flight Conditions")
    
    custom_col1, custom_col2 = st.columns(2)
    
    with custom_col1:
        custom_altitude = st.number_input(
            "Desired cruise altitude (ft MSL):",
            min_value=0,
            max_value=15000,
            value=4000,
            step=100,
            key="custom_altitude"
        )
        
        # Temperature mode toggle for custom data
        custom_temp_mode = st.radio(
            "Temperature input mode:",
            ["True temperature (°C)", "ISA deviation (°C)"],
            key="custom_temp_mode",
            help="Choose between absolute temperature or deviation from standard atmosphere"
        )
        
        # Temperature input based on mode
        if custom_temp_mode == "True temperature (°C)":
            custom_temp = st.slider(
                "Outside air temperature (°C):",
                min_value=-40,
                max_value=40,
                value=15,
                key="custom_temp"
            )
        else:
            # ISA deviation mode
            custom_isa_deviation = st.slider(
                "ISA deviation (°C):",
                min_value=-30,
                max_value=30,
                value=0,
                key="custom_isa_deviation",
                help="Temperature difference from standard atmosphere (positive = warmer than standard)"
            )
            # Calculate ISA standard temperature at altitude
            custom_isa_standard_temp = 15 - (1.98 * custom_altitude / 1000)
            custom_temp = custom_isa_standard_temp + custom_isa_deviation
            st.info(f"ℹ️ ISA standard temperature at {custom_altitude} ft: {custom_isa_standard_temp:.1f}°C")
            st.info(f"ℹ️ Actual temperature: {custom_temp:.1f}°C")
        
        custom_altimeter = st.number_input(
            "Altimeter setting (inHg):",
            min_value=28.00,
            max_value=31.00,
            value=29.92,
            step=0.01,
            format="%.2f",
            key="custom_altimeter"
        )
    
    with custom_col2:
        # Conditional manifold pressure input for custom calculations
        if custom_use_mp:
            custom_mp = st.slider(
                "Desired manifold pressure (inHg):",
                min_value=18.0,
                max_value=25.0,
                value=22.0,
                step=0.1,
                key="custom_mp"
            )
        else:
            custom_mp = None
            st.info("ℹ️ Calculation will use RPM only for power setting.")
        
        custom_rpm = st.slider(
            "Desired RPM:",
            min_value=2000,
            max_value=2700,
            value=2400,
            step=50,
            key="custom_rpm"
        )
    
    # Fuel planning for custom data
    st.subheader("Fuel Planning")
    
    fuel_col1, fuel_col2 = st.columns(2)
    
    with fuel_col1:
        custom_total_fuel = st.number_input(
            "Total usable fuel (gallons):",
            min_value=0.0,
            max_value=100.0,
            value=50.0,
            step=1.0,
            key="custom_total_fuel"
        )
    
    with fuel_col2:
        custom_reserve_fuel = st.number_input(
            "Reserve fuel (gallons):",
            min_value=0.0,
            max_value=50.0,
            value=10.0,
            step=1.0,
            key="custom_reserve_fuel"
        )
    
    # Calculate with custom data
    if st.button("Calculate with Custom Data", type="primary"):
        try:
            # Prepare user data
            user_data = {
                'base_altitude': base_altitude,
                'base_temperature': base_temperature,
                'base_mp': base_mp,
                'base_rpm': base_rpm,
                'base_tas': base_tas,
                'base_fuel_flow': base_fuel_flow
            }
            
            # Calculate performance
            custom_tas, custom_fuel_flow = pf.calculate_cruise_performance(
                custom_altitude,
                custom_temp,
                custom_rpm,
                custom_altimeter,
                custom_mp,
                user_data
            )
            
            # Calculate endurance
            custom_total_endurance, custom_usable_endurance = pf.calculate_endurance(
                custom_total_fuel,
                custom_reserve_fuel,
                custom_fuel_flow
            )
            
            # Display results
            st.success("✈️ Custom Performance Calculated!")
            
            # Results
            custom_res_col1, custom_res_col2, custom_res_col3 = st.columns(3)
            
            with custom_res_col1:
                st.metric(
                    "True Airspeed",
                    f"{custom_tas:.1f} knots"
                )
            
            with custom_res_col2:
                st.metric(
                    "Fuel Flow",
                    f"{custom_fuel_flow:.1f} GPH"
                )
            
            with custom_res_col3:
                st.metric(
                    "Usable Endurance",
                    f"{custom_usable_endurance:.1f} hours"
                )
            
            st.info(f"**Total Endurance:** {custom_total_endurance:.1f} hours | "
                   f"**Approximate Range:** {(custom_tas * custom_usable_endurance):.0f} NM")
            
        except Exception as e:
            st.error(f"Calculation error: {str(e)}")

# Information section
with st.expander("📚 How are these calculations performed?"):
    st.markdown("""
    ### Calculation Methods
    
    This calculator performs the following steps:
    
    1. **Pressure Altitude Correction**: Adjusts indicated altitude using altimeter setting
    2. **Performance Interpolation**: Uses built-in performance tables or user data to determine:
       - True airspeed based on power setting, altitude, and temperature
       - Fuel flow based on the same parameters
    3. **Endurance Calculation**: Determines total flight time based on:
       - Total usable fuel available
       - Calculated fuel flow rate
       - Specified fuel reserves
    
    ### Aircraft Compatibility
    
    This calculator supports two types of aircraft:
    
    **With Manifold Pressure Gauge:**
    - Uses manifold pressure, RPM, altitude, and temperature for calculations
    - Provides more precise power setting control
    - Typical for variable-pitch propeller aircraft
    
    **Without Manifold Pressure Gauge:**
    - Uses only RPM, altitude, and temperature for calculations
    - Simpler power setting based on RPM only
    - Typical for fixed-pitch propeller aircraft
    
    ### Built-in Data
    
    The built-in performance data is based on typical Cessna 172S performance:
    - **With MP:** Altitudes (2,000-12,000 ft), temperatures, manifold pressures (20-24 inHg), RPM (2200-2500)
    - **Without MP:** Altitudes (2,000-12,000 ft), temperatures, RPM (2200-2500) at typical 75% power settings
    
    ### Important Notes
    
    - These calculations are for **planning purposes only**
    - Always refer to your aircraft's official documentation
    - Include appropriate safety margins for actual flight operations
    - Weather conditions, aircraft configuration, and pilot technique affect actual performance
    - Consider winds aloft when calculating range and endurance
    """)

# Footer
st.markdown("---")
st.markdown("© 2025 - Aircraft Performance Calculator")
