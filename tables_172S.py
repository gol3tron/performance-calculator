# Imports
import numpy as np

# Short field takeoff distance
weight_index = np.array([2550, 2400, 2200])
# Changed to match 5 rows in sfto_ground_roll
temperature_index = np.array([0, 10, 20, 30, 40])
# Changed to match 9 columns in sfto_ground_roll
pressure_altitude_index = np.arange(0, 9000, 1000)
lift_off_index = np.array([51, 48, 44])
speed_at_50_feet_index = np.array([56, 54, 50])

# Ground roll table
sfto_ground_roll = np.array(
    [
        # 2550 pounds
        [
            [860, 940, 1025, 1125, 1235, 1355, 1495, 1645, 1820],
            [925, 1010, 1110, 1215, 1335, 1465, 1615, 1785, 1970],
            [995, 1090, 1195, 1310, 1440, 1585, 1745, 1920, 2120],
            [1070, 1170, 1285, 1410, 1550, 1705, 1875, 2065, 2280],
            [1150, 1260, 1380, 1515, 1660, 1825, 2010, 2215, 2450],
        ],
        # 2400 pounds
        [
            [745, 810, 885, 970, 1065, 1170, 1285, 1415, 1560],
            [800, 875, 955, 1050, 1150, 1265, 1390, 1530, 1690],
            [860, 940, 1030, 1130, 1240, 1360, 1500, 1650, 1815],
            [925, 1010, 1110, 1215, 1335, 1465, 1610, 1770, 1950],
            [995, 1085, 1190, 1305, 1430, 1570, 1725, 1900, 2095],
        ],
        # 2200 pounds
        [
            [610, 665, 725, 795, 870, 955, 1050, 1150, 1270],
            [655, 720, 785, 860, 940, 1030, 1130, 1245, 1370],
            [705, 770, 845, 925, 1010, 1110, 1220, 1340, 1475],
            [760, 830, 905, 995, 1090, 1195, 1310, 1435, 1580],
            [815, 890, 975, 1065, 1165, 1275, 1400, 1540, 1695],
        ],
    ]
)

sfto_dist_50_feet = np.array(
    [
        # 2550 pounds
        [
            [1465, 1600, 1755, 1925, 2120, 2345, 2605, 2910, 3265],
            [1575, 1720, 1890, 2080, 2295, 2545, 2830, 3170, 3575],
            [1690, 1850, 2035, 2240, 2480, 2755, 3075, 3440, 3880],
            [1810, 1990, 2190, 2420, 2685, 2975, 3320, 3730, 4225],
            [1945, 2135, 2355, 2605, 2880, 3205, 3585, 4045, 4615],
        ],
        # 2400 pounds
        [
            [1275, 1390, 1520, 1665, 1830, 2015, 2230, 2470, 2755],
            [1370, 1495, 1635, 1795, 1975, 2180, 2410, 2685, 3000],
            [1470, 1605, 1760, 1930, 2130, 2355, 2610, 2900, 3240],
            [1570, 1720, 1890, 2080, 2295, 2530, 2805, 3125, 3500],
            [1685, 1845, 2030, 2230, 2455, 2715, 3015, 3370, 3790],
        ],
        # 2200 pounds
        [
            [1055, 1145, 1250, 1365, 1490, 1635, 1800, 1985, 2195],
            [1130, 1230, 1340, 1465, 1605, 1765, 1940, 2145, 2375],
            [1205, 1315, 1435, 1570, 1725, 1900, 2090, 2305, 2555],
            [1290, 1410, 1540, 1685, 1855, 2035, 2240, 2475, 2745],
            [1380, 1505, 1650, 1805, 1975, 2175, 2395, 2650, 2950],
        ],
    ]
)

# maximum rate of climb data at max gross weight
pressure_altitude_roc_index = np.arange(0, 12000, 2000)
temperature_roc_index = np.arange(-20, 40, 20)
climb_speed_roc_index = np.array([74, 73, 73, 73, 72, 72, 72])

max_rate_of_climb = np.array(
    [
        [855, 760, 685, 575, 465, 360, 255],
        [785, 695, 620, 515, 405, 300, 195],
        [710, 625, 555, 450, 345, 240, 135],
        [645, 560, 495, 390, 285, 180, 0],
    ]
)

# time fuel and distance to climb at max gross weight
pressure_altitude_timefueldist_index = np.arange(0, 12000, 1000)
temperature_timefueldist_index = np.arange(15, -9, 2)
climb_speed_timefueldist_index = np.array(
    [74, 73, 73, 73, 73, 73, 73, 73, 72, 72, 72, 72, 72]
)
rate_of_climb_timefueldist_index = np.array(
    [730, 695, 655, 620, 600, 550, 505, 455, 410, 360, 315, 265, 220]
)

time_to_climb = np.array([0, 1, 3, 4, 6, 8, 10, 12, 14, 17, 20, 24, 28])
fuel_to_climb = np.array(
    [0.0, 0.4, 0.8, 1.2, 1.5, 1.9, 2.2, 2.6, 3.0, 3.4, 3.9, 4.4, 5.0]
)
distance_to_climb = np.array([0, 2, 4, 6, 8, 10, 13, 16, 19, 22, 27, 32, 38])

# Cruise performance data for 172S
# Pressure altitudes in feet
cruise_pressure_altitudes = np.array([2000, 4000, 6000, 8000, 10000, 12000])

# Standard temperatures at altitudes (degrees Celsius)
# Only two temperatures are used in the actual tables
cruise_temperatures = np.array([15, 5])

# Manifold pressure settings (inches Hg)
cruise_manifold_pressures = np.array([20, 22, 24])

# RPM settings
cruise_rpms = np.array([2200, 2300, 2400, 2500])

# True airspeed data (knots) - [altitude][temperature][manifold_pressure][rpm]
# Based on typical 172S performance data
cruise_true_airspeed = np.array([
    # 2000 ft
    [
        # 15°C
        [
            [103, 108, 113, 118],  # 20" Hg
            [108, 113, 118, 123],  # 22" Hg
            [113, 118, 123, 128],  # 24" Hg
        ],
        # 5°C
        [
            [106, 111, 116, 121],  # 20" Hg
            [111, 116, 121, 126],  # 22" Hg
            [116, 121, 126, 131],  # 24" Hg
        ],
    ],
    # 4000 ft
    [
        # 15°C
        [
            [108, 113, 118, 123],  # 20" Hg
            [113, 118, 123, 128],  # 22" Hg
            [118, 123, 128, 133],  # 24" Hg
        ],
        # 5°C
        [
            [111, 116, 121, 126],  # 20" Hg
            [116, 121, 126, 131],  # 22" Hg
            [121, 126, 131, 136],  # 24" Hg
        ],
    ],
    # 6000 ft
    [
        # 15°C
        [
            [113, 118, 123, 128],  # 20" Hg
            [118, 123, 128, 133],  # 22" Hg
            [123, 128, 133, 138],  # 24" Hg
        ],
        # 5°C
        [
            [116, 121, 126, 131],  # 20" Hg
            [121, 126, 131, 136],  # 22" Hg
            [126, 131, 136, 141],  # 24" Hg
        ],
    ],
    # 8000 ft
    [
        # 15°C
        [
            [118, 123, 128, 133],  # 20" Hg
            [123, 128, 133, 138],  # 22" Hg
            [128, 133, 138, 143],  # 24" Hg
        ],
        # 5°C
        [
            [121, 126, 131, 136],  # 20" Hg
            [126, 131, 136, 141],  # 22" Hg
            [131, 136, 141, 146],  # 24" Hg
        ],
    ],
    # 10000 ft
    [
        # 15°C
        [
            [123, 128, 133, 138],  # 20" Hg
            [128, 133, 138, 143],  # 22" Hg
            [133, 138, 143, 148],  # 24" Hg
        ],
        # 5°C
        [
            [126, 131, 136, 141],  # 20" Hg
            [131, 136, 141, 146],  # 22" Hg
            [136, 141, 146, 151],  # 24" Hg
        ],
    ],
    # 12000 ft
    [
        # 15°C
        [
            [128, 133, 138, 143],  # 20" Hg
            [133, 138, 143, 148],  # 22" Hg
            [138, 143, 148, 153],  # 24" Hg
        ],
        # 5°C
        [
            [131, 136, 141, 146],  # 20" Hg
            [136, 141, 146, 151],  # 22" Hg
            [141, 146, 151, 156],  # 24" Hg
        ],
    ],
])

# Simplified cruise performance tables without manifold pressure requirement
# For aircraft without manifold pressure gauges - uses typical 75% power settings
# True airspeed data (knots) - [altitude][temperature][rpm]
cruise_true_airspeed_no_mp = np.array([
    # 2000 ft
    [
        # 15°C
        [113, 118, 123, 128],  # RPM: 2200, 2300, 2400, 2500
        # 5°C
        [116, 121, 126, 131],  # RPM: 2200, 2300, 2400, 2500
    ],
    # 4000 ft
    [
        # 15°C
        [118, 123, 128, 133],  # RPM: 2200, 2300, 2400, 2500
        # 5°C
        [121, 126, 131, 136],  # RPM: 2200, 2300, 2400, 2500
    ],
    # 6000 ft
    [
        # 15°C
        [123, 128, 133, 138],  # RPM: 2200, 2300, 2400, 2500
        # 5°C
        [126, 131, 136, 141],  # RPM: 2200, 2300, 2400, 2500
    ],
    # 8000 ft
    [
        # 15°C
        [128, 133, 138, 143],  # RPM: 2200, 2300, 2400, 2500
        # 5°C
        [131, 136, 141, 146],  # RPM: 2200, 2300, 2400, 2500
    ],
    # 10000 ft
    [
        # 15°C
        [133, 138, 143, 148],  # RPM: 2200, 2300, 2400, 2500
        # 5°C
        [136, 141, 146, 151],  # RPM: 2200, 2300, 2400, 2500
    ],
    # 12000 ft
    [
        # 15°C
        [138, 143, 148, 153],  # RPM: 2200, 2300, 2400, 2500
        # 5°C
        [141, 146, 151, 156],  # RPM: 2200, 2300, 2400, 2500
    ],
])

# Fuel flow data (gallons per hour) - [altitude][temperature][rpm]
cruise_fuel_flow_no_mp = np.array([
    # 2000 ft
    [
        # 15°C
        [8.9, 9.6, 10.3, 11.0],  # RPM: 2200, 2300, 2400, 2500
        # 5°C
        [8.7, 9.4, 10.1, 10.8],  # RPM: 2200, 2300, 2400, 2500
    ],
    # 4000 ft
    [
        # 15°C
        [8.7, 9.4, 10.1, 10.8],  # RPM: 2200, 2300, 2400, 2500
        # 5°C
        [8.5, 9.2, 9.9, 10.6],  # RPM: 2200, 2300, 2400, 2500
    ],
    # 6000 ft
    [
        # 15°C
        [8.5, 9.2, 9.9, 10.6],  # RPM: 2200, 2300, 2400, 2500
        # 5°C
        [8.3, 9.0, 9.7, 10.4],  # RPM: 2200, 2300, 2400, 2500
    ],
    # 8000 ft
    [
        # 15°C
        [8.3, 9.0, 9.7, 10.4],  # RPM: 2200, 2300, 2400, 2500
        # 5°C
        [8.1, 8.8, 9.5, 10.2],  # RPM: 2200, 2300, 2400, 2500
    ],
    # 10000 ft
    [
        # 15°C
        [8.1, 8.8, 9.5, 10.2],  # RPM: 2200, 2300, 2400, 2500
        # 5°C
        [7.9, 8.6, 9.3, 10.0],  # RPM: 2200, 2300, 2400, 2500
    ],
    # 12000 ft
    [
        # 15°C
        [7.9, 8.6, 9.3, 10.0],  # RPM: 2200, 2300, 2400, 2500
        # 5°C
        [7.7, 8.4, 9.1, 9.8],  # RPM: 2200, 2300, 2400, 2500
    ],
])

# Fuel flow data (gallons per hour) - [altitude][temperature][manifold_pressure][rpm]
cruise_fuel_flow = np.array([
    # 2000 ft
    [
        # 15°C
        [
            [7.5, 8.2, 8.9, 9.6],  # 20" Hg
            [8.2, 8.9, 9.6, 10.3],  # 22" Hg
            [8.9, 9.6, 10.3, 11.0],  # 24" Hg
        ],
        # 5°C
        [
            [7.3, 8.0, 8.7, 9.4],  # 20" Hg
            [8.0, 8.7, 9.4, 10.1],  # 22" Hg
            [8.7, 9.4, 10.1, 10.8],  # 24" Hg
        ],
    ],
    # 4000 ft
    [
        # 15°C
        [
            [7.3, 8.0, 8.7, 9.4],  # 20" Hg
            [8.0, 8.7, 9.4, 10.1],  # 22" Hg
            [8.7, 9.4, 10.1, 10.8],  # 24" Hg
        ],
        # 5°C
        [
            [7.1, 7.8, 8.5, 9.2],  # 20" Hg
            [7.8, 8.5, 9.2, 9.9],  # 22" Hg
            [8.5, 9.2, 9.9, 10.6],  # 24" Hg
        ],
    ],
    # 6000 ft
    [
        # 15°C
        [
            [7.1, 7.8, 8.5, 9.2],  # 20" Hg
            [7.8, 8.5, 9.2, 9.9],  # 22" Hg
            [8.5, 9.2, 9.9, 10.6],  # 24" Hg
        ],
        # 5°C
        [
            [6.9, 7.6, 8.3, 9.0],  # 20" Hg
            [7.6, 8.3, 9.0, 9.7],  # 22" Hg
            [8.3, 9.0, 9.7, 10.4],  # 24" Hg
        ],
    ],
    # 8000 ft
    [
        # 15°C
        [
            [6.9, 7.6, 8.3, 9.0],  # 20" Hg
            [7.6, 8.3, 9.0, 9.7],  # 22" Hg
            [8.3, 9.0, 9.7, 10.4],  # 24" Hg
        ],
        # 5°C
        [
            [6.7, 7.4, 8.1, 8.8],  # 20" Hg
            [7.4, 8.1, 8.8, 9.5],  # 22" Hg
            [8.1, 8.8, 9.5, 10.2],  # 24" Hg
        ],
    ],
    # 10000 ft
    [
        # 15°C
        [
            [6.7, 7.4, 8.1, 8.8],  # 20" Hg
            [7.4, 8.1, 8.8, 9.5],  # 22" Hg
            [8.1, 8.8, 9.5, 10.2],  # 24" Hg
        ],
        # 5°C
        [
            [6.5, 7.2, 7.9, 8.6],  # 20" Hg
            [7.2, 7.9, 8.6, 9.3],  # 22" Hg
            [7.9, 8.6, 9.3, 10.0],  # 24" Hg
        ],
    ],
    # 12000 ft
    [
        # 15°C
        [
            [6.5, 7.2, 7.9, 8.6],  # 20" Hg
            [7.2, 7.9, 8.6, 9.3],  # 22" Hg
            [7.9, 8.6, 9.3, 10.0],  # 24" Hg
        ],
        # 5°C
        [
            [6.3, 7.0, 7.7, 8.4],  # 20" Hg
            [7.0, 7.7, 8.4, 9.1],  # 22" Hg
            [7.7, 8.4, 9.1, 9.8],  # 24" Hg
        ],
    ],
])
