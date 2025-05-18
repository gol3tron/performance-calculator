# performance-calculator

Test project for aircraft performance calculator

## General rules to implement/test

- The approximate effect of nonstandard temperature is to increase time, fuel, and distance by 10% for each 10 degC above standard temps, due to lower rate of climb (172SPHBUS-00 pg 5-7)
- Estimating crosswind component (30 deg / 50% wind speed, 45 deg / 75% wind speed, 60 dec / ~100% wind speed)
- 10% weight increase = 20% takeoff/landing distance increase (NA plane)
- Takeoff ground roll increases about 10% for every 1000 feet of density altitude
- TOD planning divide altitude you need to lose by 300 for NM from target point
- ILS course width at threshold 1/2 dot deflection about 1/2 runway width

## Workflow proposed

- User defines aircraft type
- User inputs weather conditions / runway data (or we look it up?)
- User selects weight/balance configuration
- User receives performance calculations

## Information provided

- Takeoff and landing data
- Recommended abort/rotation speed
- Optimal rate of climb
- V speeds as weight changes during flight
- Cruise performance
- Approach configuration (speeds and descent rates for selected approach)
