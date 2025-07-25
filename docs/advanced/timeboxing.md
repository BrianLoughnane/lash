---
title: "Timeboxing"
updated: "Unknown"
---

# Timeboxing

##### Timeboxing is a method for creating pragmatic comparisons between different time periods of the same data series

Timeboxing is a method for creating pragmatic comparisons between different time periods of the same data series by aligning the main period and comparison period as closely as possible.

**How timeboxing works**

For high-resolution interval data, alignment between the main period and comparison period comes easily: If data are stored at 15-minute intervals, then both periods have enough readings to achieve alignment in any graph with 15-minute resolution or greater.

To achieve a similar outcome for month-resolution bill points, Atrius takes a bill point's month-resolution data and evenly distributes—or prorates—daily cost and consumption over each day of the bill period, creating an approximate day-resolution data set.

Since bills can span two or more months, any partially included months will have only partial charges for that month. Furthermore, utility bills may still be unreceived, even after the applicable bill month has elapsed, leaving no current charges for the month.

In other words, to make time-based comparisons of equal length, timeboxing prevents the comparison period end date from extending beyond the main period end date.

Timeboxed main period and comparison period data are automatically applied to all portfolio-scope, building-scope, and tenant-scope cards.

**Example**

A user creates a Building Trends card with the following selections:
- Resource = Electricity
- Period = This month
- Overlay = Same period previous year
- Callouts = Total this period, Total same period previous year, Difference

Here is the output:
- The graph will display all available data.
- The "Total this period" callout (X) will display all available data, up to the present day and hour.
- The "Total same period previous year" callout (Y) will display all available data, up to the day and hour as it corresponds to the previous year.
- The "Difference" callout (Z) will display the percent difference between the main period and comparison period.

**Special case: Bill itemizations**

Bill itemizations, including peak demand, do not disaggregate from month-resolution to day-resolution data in percent difference calculations. Because bill itemizations use bill objects, not time series data, the percent difference calculation will work correctly without disaggregation.

---
