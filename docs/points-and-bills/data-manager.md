---
title: "Data Manager"
updated: "over a year ago"
---

# Data Manager

#### 👍 This article will help you:

* Understand data resolutions & calendarization
* View a reading and drill down into statistics
* Discover spikes, flatlines, and missing data

To see the complete data record for a point or bill point, go to Points or Bills on the left side menu. Next, select a point or bill point, then go to the Data Manager tab. Alternately, you may go to a building to find the points or bill points belonging to that building, then select the point or bill point.

#### Resolutions & Calendarization

Source shows data readings as they have been received from your data source. This data has not been processed by Atrius. Use this table view to help troubleshoot whether a data problem occurs before or after Atrius has performed any data processing, or to verify that data has been re-uploaded to replace earlier data sets.

To view data over different time intervals, select a resolution: Minute, Quarter-hour, Hour, Day, Week, Month, Year.

The highest resolution available will depend on the reporting interval of your data source. For instance, "Minute, Quarter-hour, Hour, Day, Week, Month, Year" will display for points, while "Day, Month, Year" will display for bill points.

For Manual Point integrations, a 'Manual' view option will also appear.

For bill point data at "Month" and "Year" resolutions, a calendarization dropdown menu will appear. Atrius offers five calendarization options to more accurately represent month-to-month and year-to-year cost and consumption, regardless of the various start and end dates found on your bills.

| Calendarization method | Description |
| --- | --- |
| Prorated months | Allocates data on a month-by-month basis by evenly distributing cost and consumption over each day of the bill period |
| Calendar months | Allocates data to the month in which the majority of days occur over the bill period |
| Bill point start dates | Allocates data to the month in which the first point reading occurs |
| Bill point end dates | Allocates data to the month in which the last point reading occurs |
| Statement dates | Allocates data to the month in which the "issued date" of the statement invoice occurs |

#### Readings & Statistics

The Data Manager tab shows you all the information relevant to your point or bill point reading, and depending on which is selected, you'll see different default columns. Select any reading row to view more advanced statistics and reading details.

For bill points, you can also view the PDF version of your bill by selecting the "View bill" button in each row. This allows you to easily compare the data displayed in the Data Manager with the bill itself. If you find that any of the values displayed in Atrius do not match the bill itself, or you have any questions regarding statistics or bill itemizations, please reach out to Atrius Customer Support.

#### Adding a Reading

To manually add a reading, select the green "Add a reading" button and fill out the required information.

For Bill points, you can add a bill PDF to your manual reading, by clicking the drop-down menu on the right side of the table, then selecting "Attach bill". To remove, use the same drop-down menu and select "Remove bill".

#### Notes

To add a note to a reading or gap, open the drop down menu and select "Add a note" for any reading or gap in the Source view. Use notes to help explain data anomalies, or flag readings for investigation.

Notes can be added in the following places:

* In the Data Manager tab on the "Source" resolution view.
* In the Data Quality app, while in the Gaps tab on the "Data Manager" view.
* In the Batch Bill Data Upload app, after clicking "Upload data", and selecting 'Download CSV'. In the downloaded file, you can add notes in the Notes column.

Notes appear as blue bubble icons, with the number of notes for a given reading or gap contained in the bubble.

#### Gaps, Spikes, & Flatlines

If a data record contains gaps, spikes, or flatlines, these events are displayed alongside the readings in Data Manager for any time resolution.

Gaps periods are labeled with "Gap", a start and end period, and a duration. Each row is highlighted in red.

Spikes are labeled with "Removed spike". Each row is highlighted in purple.

Flatlines are labeled with "Flatline". Each row is highlighted in orange.

Both spikes and flatlines are shown with Deltas and Weights of zero, and with Storage and Consumption values of "none", since these values have been removed from your data set.

---
