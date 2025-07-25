---
title: "Reading types"
updated: "over a year ago"
---

# Reading types

Reading type is the format in which points record and report data. An accurate reading type is required for correctly processing data being sent to Atrius.

#### 👍 This article will help you:

* Understand the different ways electricity, gas, water, and other points can record data
* Determine what a point's reading type is by looking at product documentation provided by the meter or device manufacturer, or examining data that it produces
* Maximize data quality by selecting more accurate reading types

Atrius supports five reading types:

* Totalizer
* Interval demand
* Interval consumption
* Instantaneous measurement
* Bi-directional totalizer

Before proceeding, make sure you have a solid understanding of kilowatts (kW) versus kilowatt-hours (kWh). If you need a refresher, see Understand kW vs. kWh.

🚧 **Reading type may affect data quality**

Sometimes you have a choice of reading types when exporting data from a point. If so, obtain data using one of the reading types in the 100% accurate list below:

100% accurate reading types:

* Totalizer
* Interval demand
* Interval consumption
* Bi-directional totalizer

Less-than-100% accurate reading types:

* Instantaneous measurement

#### Totalizer

Points with a totalizer reading type, also known as an accumulator reading type, behave the same way that car odometers do: they only go up and they generally report the total amount consumed since they were installed. Car odometers report total miles ever driven, and points with a totalizer reading type report total kWh of electricity ever consumed, or total gallons of water ever consumed, etc. Some totalizer points may "turn over" periodically, meaning that they reset to 0, then start counting up again.

---
