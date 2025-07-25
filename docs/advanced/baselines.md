---
title: "Baselines"
updated: "over 5 months ago"
---

# Baselines

##### Baselines are ongoing data sets that reflect predicted consumption based on historic usage and external variables

Baselines are ongoing data sets that reflect predicted consumption based on historic usage and external variables.

**Methodology**

Atrius allows you to build baseline models to predict resource use. A baseline is a statistical model—a function that predicts a target value based on independent variables. In our case, the target value is resource use, and the independent variables often include weather data, occupancy data, and calendar inputs.

Once you create a baseline, Atrius will "run" the baseline continually, updating predictions as new weather data or other inputs become available. While baselines are highly configurable, Atrius provides intelligent defaults, so that you can produce a useful baseline without having to understand the configuration options.

**Seed period**

To create a baseline you must select a seed period. The data between the selected start and end dates comprise the training set, and are used to estimate the coefficients of the model. Atrius will produce baseline readings—predicted resource consumption—beginning at the end of the seed period.

**Variable selection**

You can choose from a menu of variables to include in the model. Variable selection determines what effects will be accounted for by the baseline. For instance, including temperature will allow your baseline to capture temperature responsiveness of energy demand.

Baselines can be created manually by selecting each variable individually. Alternatively, they can also be created automatically: Atrius will select the variables that lead to the most accurate model. Because of this, a long seed period is essential for the model to select the most useful variables.

Atrius currently supports over a dozen variables, including some transformations on basic variables to capture non-linear effects and interactions. Available variables include:

- Heating Degree Days (HDD): Daily calculation of amount by which average daily temperature falls below 65°F
- Cooling Degree Days (CDD): Daily calculation of amount by which average daily temperature exceeds 65°F
- Temperature: Hourly temperature in Fahrenheit
- Temperature above/below 65 degrees: Hourly calculations with various transformations including squared values
- Humidity: Hourly relative humidity percentage
- Heat index: Index combining temperature and relative humidity
- Occupancy: If the building has an occupancy point, this can be selected for the baseline model
- Weekend vs. weekday: Binary flag representing weekend or weekday
- Day of week: Categorical variable representing day of week
- Month: Categorical variable representing month of the year
- Hour: Categorical variable representing hour of the day

**Algorithms**

Baseline models are implemented as generalized linear models. Currently supported variants include:
- Ordinary Least Squares: Finds the "line of best fit" between regression variables and resource use data

---
