# Imports
import numpy as np

# Short field takeoff distance
weight_index = np.array([2550, 2400, 2200])
temperature_index = np.array([0, 10, 20, 30, 40])
pressure_altitude_index = np.array([0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000])
lift_off_index = np.array([51, 48, 44])
speed_at_50_feet_index = np.array([56, 54, 50])

# Ground roll table
sfto_ground_roll = np.array([
    # 2550 pounds
    [
        [
            860,
            940,
            1025,
            1125,
            1235,
            1355,
            1495,
            1645,
            1820
        ],

        [
            925,
            1010,
            1110,
            1215,
            1335,
            1465,
            1615,
            1785,
            1970
        ],

        [
            995,
            1090,
            1195,
            1310,
            1440,
            1585,
            1745,
            1920,
            2120
        ],

        [
            1070,
            1170,
            1285,
            1410,
            1550,
            1705,
            1875,
            2065,
            2280
        ],

        [
            1150,
            1260,
            1380,
            1515,
            1660,
            1825,
            2010,
            2215,
            2450
        ]
    ], 
    # 2400 pounds
    [
        [

        ],

        [

        ],

        [

        ],

        [

        ],

        [

        ]
    ],
    # 2200 pounds
    [
        [

        ],

        [

        ],

        [

        ],

        [

        ],

        [

        ]
    ]
]
)
