---
title: "Degree days"
updated: "Unknown"
---

# Degree days

##### Heating and cooling degree days are commonly used in calculations related to the energy consumption required to heat and/or cool buildings

Heating and cooling degree days are commonly used in calculations related to the energy consumption required to heat and/or cool buildings.

**Overview**

The energy use of building heating systems is more complicated than the energy use of TVs, computers, and other plug-load equipment because it varies based on the weather.

As you might expect, the colder the outside air temperature, the more energy it takes to heat a building. Likewise, the warmer the outside air, the more energy it takes to cool a building. Because outdoor weather is the single biggest driver of commercial building energy use, building operators need to easily understand the heating and cooling demand of their buildings.

**Definitions**

- **Heating degree days (HDD)**: A measure of how much (in degrees), and for how many days, the outside air temperature was below the heating balance point.
- **Cooling degree days (CDD)**: A measure of how much (in degrees), and for how many days, the outside air temperature was above the cooling balance point.
- **Balance point or base temperature**: The temperature below which a building needs heating, and above which a building needs cooling.

For example, if the average temperature yesterday was 70 °F and the heating balance point in your building is set to 65 °F, you would have cooled your building down by 5 degrees for the duration of a day. Therefore, the cooling demand was 5 CDD.

**Primary uses of HDD and CDD**

1. **Normalizing energy use** for the seasonal variability in weather. If you improve your building's efficiency, degree days help you discover the real effect of the improvements when comparing your upgraded performance to historical use.
2. **Comparing the energy use intensity** of buildings in different climate zones. Degree days are used to normalize and benchmark building performance across buildings that do not share the same climate.

**How are HDD and CDD used in Atrius?**

HDD and CDD are primarily used as a data visualization overlay on building consumption data and as a variable in regression analysis used to generated weather-normalized consumption baselines. They are found in:

- **Baselines**: Create weather-normalized baselines that can be used as an overlay or comparison in dashboards and apps.
- **Dashboards**: In several cards, select HDD, CDD, or an outdoor temperature overlay option to automatically remove weather variability.
- **Projects**: When you select a baseline seed period, implementation period, and associated buildings, Atrius automatically includes a wide range of weather variables, such as HDD and CDD.
- **Trend Analysis**: Display HDD, CDD, and outdoor temperature overlays for any building point.
- **Heat Map Analysis**: Display HDD, CDD, and outdoor temperature as a comparison layer to study the correlation between observed building scheduling and heating or cooling demand.

**Where do weather data come from?**

Weather data are essential for calculating degree days. Through a third-party partnership, Atrius makes high-resolution hourly weather data available for every building.

When you create a new building, Atrius automatically requests and compiles a 5-year historical record of weather data, and begins to collect ongoing hourly weather data. We use the weather station closest to your building's physical address, typically within 5 miles.

**Adjusting balance point temperature**

Atrius uses 65 °F as the balance point, or base temperature, to calculate heating and cooling degree days. To change the heating and cooling balance points for a building:
- Go to Buildings, then select a building.
- Select the building's Profile tab
- Under the Additional Details section, modify the Cooling balance point and Heating balance point fields.
- Select 'Save' at the bottom of the page.

---
