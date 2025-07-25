---
title: "Forecasts"
updated: "Unknown"
---

# Forecasts

##### Forecasts are ongoing data sets that reflect expected consumption based on a building's profile and historic usage

Forecasts are ongoing data sets that reflect expected consumption based on a building's profile and historic usage.

In the Alerts app, you can configure different conditions that will trigger an email notification—including when a forecasted value has been exceeded by a certain amount.

**Demand forecast alerts**

The demand forecast at any given time is the average demand for the same day and time of the week over the last 4 weeks, depending on the resolution of the point (15-minute, hourly, daily). If demand for the current period exceeds the forecast by the specified percentage at any time, then the alert will be triggered.

In the alert configuration form:
- Condition: Select 'Rate exceeds forecast by' or 'Production exceeds forecast by'.
- %: Enter a percent value.

*Example*: If the current time is Monday at 9:00 AM and the selected point has a 15-minute resolution, the demand forecast would be the average of demand for the last four Mondays from 9:00-9:15 AM.

**Daily use forecast alerts**

The daily forecast on a given day is the average daily consumption for the same day of the week over the last 4 weeks. If daily consumption exceeds the forecast by the specified percentage at any time, then the alert will be triggered.

In the alert configuration form:
- Condition: Select 'Total daily consumption exceeds forecast by' or 'Total daily production exceeds forecast by'.
- %: Enter a percent value.

*Example*: If today is Monday, the daily use forecast would be the average of daily consumption for the last four Mondays.

**Monthly use forecast alerts**

The monthly forecast for a given month is the average monthly consumption for the same month over the last 4 years. If monthly consumption exceeds the forecast by the specified percentage at any time, then the alert will be triggered.

In the alert configuration form:
- Condition: Select 'Total monthly consumption exceeds forecast by' or 'Total monthly production exceeds forecast by'.
- %: Enter a percent value.

*Example*: If the current month is August 2019, the monthly use forecast would be the average of monthly consumption for August 2015, 2016, 2017, and 2018.

**Trend Analysis forecasts**

Forecasts can be viewed in Trend Analysis via the "compared to" dropdown menu:
- **Hourly (or 15-minute) forecasts**: The forecast for each time interval is the average usage for the same day and time of the week over the last 4 weeks.
- **Daily forecasts**: The forecast for each day is the average usage for the same day of the week over the last 4 weeks.
- **Monthly forecasts**: The forecast for each month is the average usage for the same month over the last 4 years.

Note that Trend Analysis "interpolates" values to render a smooth curve between points.

---
