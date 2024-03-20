import numpy as np
import scipy as sp

import tables_172S as tb


def get_pressure_altitude(altimiter: float, true_altitude: float) -> float:
    """
    Computer the pressure altitude based on altimeter setting and true altitude.

    Return a pressure altitude (feet MSL) as a float value.
    """
    pressure_altitude = (29.92 - altimiter) * 1000 + true_altitude
    return pressure_altitude


def get_ground_roll_sfto(
    pressure_altitude: float, weight: float, temperature: float
) -> float:
    """
    Compute the ground roll for short field takeoff in feet based on weight, pressure altitude and temperature.

    Return ground roll (feet) as a float value.
    """

    # Compute ground_roll
    points = (tb.weight_index, tb.temperature_index, tb.pressure_altitude_index)
    point = np.array([weight, temperature, pressure_altitude])
    ground_roll = sp.interpolate.interpn(points, tb.sfto_ground_roll, point)[0]

    return ground_roll


def get_dist_50ft_sfto(
    pressure_altitude: float, weight: float, temperature: float
) -> float:
    """
    Compute the distance (in feet) at 50 ft height for short field takeoff based on weight, pressure altitude and temperature.

    Return dist_50ft as a float value.
    """

    # Compute ground_roll
    points = (tb.weight_index, tb.temperature_index, tb.pressure_altitude_index)
    point = np.array([weight, temperature, pressure_altitude])
    dist_50ft = sp.interpolate.interpn(points, tb.sfto_dist_50_feet, point)[0]

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
