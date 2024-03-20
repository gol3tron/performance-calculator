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
