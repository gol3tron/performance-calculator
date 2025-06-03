import math

import numpy as np
import scipy as sp

import tables_172S as tb


def get_safety_margin_modifier(safety_margin: float) -> float:
    """
    Compute the appropriate modifier for takeoff roll given user defined safety margin as a percentage.
    Return a modifier float value.
    """
    modifer = 1 + safety_margin / 100
    return modifer


def get_normal_takeoff_modifier(is_normal_takeoff: bool) -> float:
    """
    Compute the appropriate modifier to short field takeoff performance when using
    a normal takeoff procedure (flaps 0 deg, 55 knots rotation speed)

    - Increase ground roll about 10% if flaps set to 0 degrees
    - Increase ground roll by ?? for rotation at 55 knots
    """
    if is_normal_takeoff:
        modifier = 1.1
    else:
        modifier = 1

    return modifier


def get_runway_slope_modifier(slope: float) -> float:
    """
    Compute the appropriate modifier to takeoff roll given a runway slope as a percent grade.

    Return a float modifier value.

    TODO: Build this out! https://www.boldmethod.com/learn-to-fly/performance/runway-surface-and-slope/
    """
    modifier = 1

    return modifier


def get_wind_runway_modifier(
    runway_heading: float, wind_speed: float, wind_direction: float
) -> float:
    """
    Compute the multiplier for ground roll based on wind direction and speed given runway heading.
    - Decrease distances 10% for each 9 knots headwind
    - Increase distances by 10% for each 2 knots tailwind
    """
    wind_runway_difference = (runway_heading - wind_direction) % 360
    deg_to_rad_conversion = math.pi / 180
    wind_component = wind_speed * math.cos(
        deg_to_rad_conversion * wind_runway_difference
    )

    if wind_component > 0:  # headwind
        modifier = 1 - wind_component * (0.1 / 9)
    elif wind_component < 0:  # tailwind
        modifier = 1 + wind_component * (0.1 / 2)
    else:  # no wind
        modifier = 1

    return modifier


def get_grass_runway_modifier(is_grass: bool) -> float:
    """
    For operation on a dry grass runway, increase distances by 15% of the "ground roll" figure.
    See https://www.boldmethod.com/learn-to-fly/performance/runway-surface-and-slope/
    Return a modifier value of 1.15 if is_grass is True.
    """
    if is_grass:
        return 1.15
    else:
        return 1


def get_pressure_altitude(altimiter: float, true_altitude: float) -> float:
    """
    Compute the pressure altitude based on altimeter setting and true altitude.

    Return a pressure altitude (feet MSL) as a float value.
    """
    pressure_altitude = (29.92 - altimiter) * 1000 + true_altitude
    return pressure_altitude


def get_ground_roll_sfto(
    pressure_altitude: float,
    weight: float,
    temperature: float,
    runway_heading: float,
    wind_direction: float,
    wind_speed: float,
    is_grass: bool,
) -> float:
    """
    Compute the ground roll for short field takeoff in feet based on weight, pressure altitude and temperature.

    Return ground roll (feet) as a float value.
    """

    # Compute ground_roll
    points = (tb.weight_index, tb.temperature_index, tb.pressure_altitude_index)
    point = np.array([weight, temperature, pressure_altitude])
    ground_roll = sp.interpolate.interpn(points, tb.sfto_ground_roll, point)[0]

    wind_modifier = get_wind_runway_modifier(runway_heading, wind_speed, wind_direction)
    grass_modifier = get_grass_runway_modifier(is_grass)

    ground_roll *= wind_modifier * grass_modifier

    return ground_roll


def get_dist_50ft_sfto(
    pressure_altitude: float,
    weight: float,
    temperature: float,
    runway_heading: float,
    wind_direction: float,
    wind_speed: float,
    is_grass: bool,
) -> float:
    """
    Compute the distance (in feet) at 50 ft height for short field takeoff based on weight, pressure altitude and temperature.

    Return dist_50ft as a float value.
    """

    # Compute ground_roll
    points = (tb.weight_index, tb.temperature_index, tb.pressure_altitude_index)
    point = np.array([weight, temperature, pressure_altitude])
    dist_50ft = sp.interpolate.interpn(points, tb.sfto_dist_50_feet, point)[0]

    wind_modifier = get_wind_runway_modifier(runway_heading, wind_speed, wind_direction)
    grass_modifier = get_grass_runway_modifier(is_grass)

    dist_50ft *= wind_modifier * grass_modifier

    return dist_50ft


def get_lift_off_speed(weight: float) -> float:
    """
    Compute the lift off speed in knots for a short field takeoff.

    Return a float value for lift_off_speed.
    """

    # Compute lift_off_speed
    lift_off_speed = np.interp(
        np.array(weight), tb.weight_index[::-1], tb.lift_off_index[::-1]
    )

    return lift_off_speed


def get_speed_at_50ft(weight: float) -> float:
    """
    Compute the speed at 50 ft height in knots for a short field takeoff.

    Return a float value for speed_at_50ft.
    """

    # Compute lift_off_speed
    speed_at_50ft = np.interp(
        np.array(weight), tb.weight_index[::-1], tb.speed_at_50_feet_index[::-1]
    )

    return speed_at_50ft


def include_wind(
    distance: float, runway_heading: float, wind_direction: float, wind_speed: float
) -> float:
    """
    Recompute a takeoff/landing distance to include the effects of wind (knots).

    Returns a new distance in feet as float.
    """
    new_distance = distance

    return new_distance


def get_true_airspeed(
    indicated_airspeed: float, pressure_altitude: float, temperature_celsius: float
) -> float:
    """
    Calculate true airspeed from indicated airspeed, pressure altitude, and temperature.
    
    Args:
        indicated_airspeed: Indicated airspeed in knots
        pressure_altitude: Pressure altitude in feet
        temperature_celsius: Temperature in degrees Celsius
    
    Returns:
        True airspeed in knots
    """
    # Standard atmosphere at sea level
    standard_temp_kelvin = 288.15  # 15°C in Kelvin
    temp_kelvin = temperature_celsius + 273.15
    
    # Temperature ratio
    temp_ratio = temp_kelvin / standard_temp_kelvin
    
    # Pressure ratio (simplified for altitude)
    # Using standard lapse rate of 1.98°C per 1000 ft
    pressure_ratio = (1 - (pressure_altitude * 6.5e-6)) ** 5.2561
    
    # Density ratio
    density_ratio = pressure_ratio / temp_ratio
    
    # True airspeed calculation
    true_airspeed = indicated_airspeed / math.sqrt(density_ratio)
    
    return true_airspeed


def get_ground_speed(
    true_airspeed: float, 
    aircraft_heading: float, 
    wind_direction: float, 
    wind_speed: float
) -> float:
    """
    Calculate ground speed from true airspeed and wind conditions.
    
    Args:
        true_airspeed: True airspeed in knots
        aircraft_heading: Aircraft magnetic heading in degrees
        wind_direction: Wind direction in degrees (direction wind is coming from)
        wind_speed: Wind speed in knots
    
    Returns:
        Ground speed in knots
    """
    # Convert to radians
    deg_to_rad = math.pi / 180
    
    # Calculate relative wind angle (wind direction relative to aircraft heading)
    # Wind direction is where wind is coming FROM
    relative_wind_angle = (wind_direction - aircraft_heading) % 360
    
    # Calculate wind components
    # Positive component means headwind (reduces ground speed)
    headwind_component = wind_speed * math.cos(deg_to_rad * relative_wind_angle)
    
    # Ground speed = TAS - headwind component (headwind reduces ground speed)
    ground_speed = true_airspeed - headwind_component
    
    return max(0, ground_speed)  # Ensure non-negative ground speed


def interpolate_parameter(
    start_altitude: float,
    end_altitude: float,
    current_altitude: float,
    start_value: float,
    end_value: float
) -> float:
    """
    Linearly interpolate a parameter between two altitudes.
    
    Args:
        start_altitude: Starting altitude in feet
        end_altitude: Ending altitude in feet  
        current_altitude: Current altitude for interpolation in feet
        start_value: Parameter value at starting altitude
        end_value: Parameter value at ending altitude
    
    Returns:
        Interpolated parameter value
    """
    if start_altitude == end_altitude:
        return start_value
    
    # Linear interpolation
    ratio = (current_altitude - start_altitude) / (end_altitude - start_altitude)
    interpolated_value = start_value + ratio * (end_value - start_value)
    
    return interpolated_value


def calculate_climb_gradient(
    start_altitude: float,
    end_altitude: float,
    start_climb_rate: float,
    end_climb_rate: float,
    start_indicated_airspeed: float,
    start_temp: float,
    end_temp: float,
    start_wind_dir: float,
    start_wind_speed: float,
    end_wind_dir: float,
    end_wind_speed: float,
    start_heading: float,
    end_heading: float,
    altimeter_setting: float
) -> tuple[float, float, float]:
    """
    Calculate climb performance including max true airspeed, max ground speed, 
    and minimum climb gradient.
    
    Returns:
        Tuple of (max_true_airspeed, max_ground_speed, min_climb_gradient_ft_per_nm)
    """
    altitude_change = end_altitude - start_altitude
    if altitude_change <= 0:
        return 0.0, 0.0, 0.0
    
    # Sample points throughout the climb (every 500 feet)
    sample_interval = 500
    sample_altitudes = []
    current_alt = start_altitude
    while current_alt <= end_altitude:
        sample_altitudes.append(current_alt)
        current_alt += sample_interval
    
    # Ensure we include the end altitude
    if sample_altitudes[-1] != end_altitude:
        sample_altitudes.append(end_altitude)
    
    max_true_airspeed = 0.0
    max_ground_speed = 0.0
    total_time = 0.0
    total_distance = 0.0
    
    # Calculate performance at each sample point
    for i, altitude in enumerate(sample_altitudes[:-1]):
        next_altitude = sample_altitudes[i + 1]
        segment_altitude_change = next_altitude - altitude
        
        # Interpolate parameters for this segment
        avg_altitude = (altitude + next_altitude) / 2
        
        # Interpolate climb rate
        climb_rate = interpolate_parameter(
            start_altitude, end_altitude, avg_altitude, start_climb_rate, end_climb_rate
        )
        
        # Interpolate temperature  
        temp = interpolate_parameter(
            start_altitude, end_altitude, avg_altitude, start_temp, end_temp
        )
        
        # Interpolate wind conditions
        wind_dir = interpolate_parameter(
            start_altitude, end_altitude, avg_altitude, start_wind_dir, end_wind_dir
        )
        wind_speed = interpolate_parameter(
            start_altitude, end_altitude, avg_altitude, start_wind_speed, end_wind_speed
        )
        
        # Interpolate heading
        # Handle magnetic heading interpolation (circular)
        heading_diff = (end_heading - start_heading) % 360
        if heading_diff > 180:
            heading_diff -= 360
        heading = (start_heading + interpolate_parameter(
            start_altitude, end_altitude, avg_altitude, 0, heading_diff
        )) % 360
        
        # Calculate pressure altitude for this segment
        pressure_altitude = get_pressure_altitude(altimeter_setting, avg_altitude)
        
        # Calculate true airspeed
        true_airspeed = get_true_airspeed(start_indicated_airspeed, pressure_altitude, temp)
        max_true_airspeed = max(max_true_airspeed, true_airspeed)
        
        # Calculate ground speed
        ground_speed = get_ground_speed(true_airspeed, heading, wind_dir, wind_speed)
        max_ground_speed = max(max_ground_speed, ground_speed)
        
        # Calculate time and distance for this segment
        if climb_rate > 0:
            segment_time = segment_altitude_change / climb_rate  # minutes
            segment_distance = (ground_speed / 60) * segment_time  # nautical miles
            
            total_time += segment_time
            total_distance += segment_distance
    
    # Calculate minimum climb gradient in ft/nm
    min_climb_gradient = altitude_change / total_distance if total_distance > 0 else 0.0
    
    return max_true_airspeed, max_ground_speed, min_climb_gradient
