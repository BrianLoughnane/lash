---
title: "Normalization"
updated: "Unknown"
---

# Normalization

##### Normalization is a method for removing abnormal variables from your consumption data

Normalization is a method for removing abnormal variables from your consumption data.

**What is normalization?**

*Normalization 101*

The "normalization" of data represents an estimate of consumption under typical conditions, with weather and/or occupancy effects removed. Normalization ultimately helps you accurately compare buildings across time and geography.

*Background*

Comparing building performance across time and geography can be problematic due to differing weather patterns from year to year and from city to city. These abnormal patterns interfere with an important energy management task: pinpointing the root cause of an increase or decrease in consumption. Common abnormalities include 1) extreme weather, and 2) increased vacancy.

**Why do normalization?**

The only way to directly compare buildings is to correct—or "normalize"—for weather and occupancy differences. Other major benefits include:

- **Apples-to-apples comparison**: View two years of data or two different buildings side-by-side.
- **Easily compare across time & geography**: Remove all abnormalities across geographies in order to correctly compare buildings which may be 3,000 miles apart.
- **Transparent calculations**: View all normalization calculations, showing each step of the process.
- **Real-time normalization**: Atrius normalizes data immediately after it is added to the system.

**Which data can be normalized?**

Data from both points and bill points can be normalized.

The following point types are supported:
- Cooling
- Electricity
- Heating
- Natural gas
- Water

Normalization calculations use source data (consumption or demand). Once normalized data can then be converted into cost or emissions.

**At least 2 years of data are required**

Normalization is available for point types with at least 2 years of monthly historical data. If higher than monthly resolution exists, then the monthly roll-ups will be used during calculations.

**Types of normalization**

Atrius supports normalization by weather and by occupied area.

- **Weather normalization**: Compare your building as if weather was "typical" across different years. Heating and cooling degree day effects are combined for a total weather effect during calculations.
- **Occupied area normalization**: Compare your building as if vacancy was exactly the same across years.

In addition to normalizing by weather or occupied area individually, Atrius can combine these effects to estimate consumption normalized by both weather and occupied area.

**Typical conditions**

Atrius uses the term "typical" to refer to weather or occupancy conditions used for normalization.

*Typical weather*

Typical weather data is a trailing average, calculated using at least five years of historical weather data. This is a rolling five- to ten-year historical average as time moves forward.

*Typical occupied area*

For typical occupied area, the total area of the building is used. As a result, your normalized data will be an estimate of consumption at 100% occupied area.

---
