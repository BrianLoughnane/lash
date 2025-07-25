---
title: "Data Management"
updated: "Unknown"
---

# Data Management

#### Files

Updated over a year ago

##### The Files app allows you to upload and export shared files among your team

The Files app allows you to upload and export shared files among your team.

To access the Files app go to Apps on the left side menu, then Files.

**Files locations**

Files can be found in several distinct locations in Atrius:

*Files app*: When files are uploaded directly via the Files app, they are immediately accessible by all users at your organization.

*Buildings > Files*: The Files tab for individual buildings supports file storage specifically for each building.

*Tenants > Leases*: The Leases tab for individual tenants supports lease file storage specifically for each tenant.

*Assets > Files*: The Files tab for individual assets supports file storage specifically for each asset.

*Projects > Files*: The Files tab for individual projects supports file storage specifically for each project.

*Bills > Statements > Files*: The Files tab for individual statements supports file storage specifically for each statement.

**Add a new folder or file**

In the Files app or a Files tab, select the 'Add a folder' button.

To upload a file, drag and drop the file into the "upload" region, denoted by a gray box, or select 'Upload a file' to browse your computer for the file(s).

**File type support**

A wide variety of file types are permitted to be uploaded, including:
- Comma Separated Values (.csv)
- JPEG (.jpg, .jpeg)
- GIF (.gif)
- Microsoft Excel (.xls, .xlsx)
- Microsoft PowerPoint (.ppt, .pptx)
- Microsoft Word (.doc, .docx)
- PDF (.pdf)
- Plain Text (.txt)
- PNG (.png)
- Tagged Image File (.tif, .tiff)
- ZIP (.zip)

**File size**

The maximum supported file size for any file type is 2GB.

---

#### Mobile Data Entry

Updated over a year ago

##### Mobile Data Entry provides an easy way to manually enter interval readings while you are out in the field

Mobile Data Entry provides an easy way to manually enter interval readings while you are out in the field. Only a mobile device is required.

To access Mobile Data Entry, go to Apps in the side menu at left, then Mobile Data Entry. Alternately, type m.buildingos.com into the web browser on your mobile device.

**Add a manual reading**

Select a building. If you have access to only a single building, then the buildings list will be skipped.

Select a point. All manual points with reading types of totalizer or interval consumption that are associated with the building will display in the list.

Select the form field to input a numerical reading. The grey number displayed in the field is the most recent manual reading for that point, for reference.

**Check for reading multipliers**

Certain meters require that you multiply the reading by a "multiplier". For example, a meter may show "X300," indicating that the number on the face of the meter should be multiplied by 300 before being entered in the field.

If the meter or device has a photo, then it will display here. If the meter or device has a description, then a question mark icon will appear at the bottom right of the photo.

If a Validation threshold has been configured for the point, then your manual reading will be checked against it. New readings in excess of this threshold will trigger a warning message.

**Troubleshooting**
- Incorrect readings must be deleted in Atrius. Navigate to the point in Atrius, then to Data Manager.
- Readings must be at least one hour apart.
- Mobile Data Entry requires Internet connectivity to submit readings.

---

#### Data Quality

Updated over 3 months ago

##### The Data Quality App provides views of the integrity of data across your portfolio

The Data Quality App provides views of the integrity of data across your portfolio, helping you to determine overall data completeness, discover spikes and flatlines that are automatically detected by Atrius, and quickly identify data issues or anomalies.

To access Data Quality, go to Apps in the side menu at left, then Data Quality.

**Overview**

The Overview tab provides a portfolio-wide summary of all your organization's data in Atrius, including percent online/current, average completeness, gaps, spikes, flatlines, and statuses.

Use Filter and All time to update the callouts and tables on each page. You can filter by Point, Type (i.e., Resource), Scope, Integration, Status, Building, Building Group, or Utility Provider.

**Using the period filter ("All time")**

The following fields update when changing the period filter:
- Completeness
- Gaps
- Spikes
- Flatlines

The following fields do NOT update when changing the period filter:
- Percent online/current shows the proportion of all points and bill points that are online/current
- Status shows if a point or bill point is online/current, offline/outdated, or flatlined at this moment
- Outdated bill points shows how many bill points are not current at this moment

**Completeness**

The Completeness tab shows how much data exists for each point. Completeness is calculated as (Time Elapsed - Missing Data) / Time Elapsed * 100.

**Gaps**

Gaps are date ranges where no reading exists on a given point or bill point. A gap has to have a minimum duration of 1 day in order to appear in the gaps lists.

**Filling gaps**
- To fill point gaps, add manual readings via the point Data Manager, or use the Batch Point Data Upload tool.
- To fill bill point gaps, add manual readings via the bill point Data Manager.

---

#### Exporting data

Updated over 11 months ago

##### Atrius makes it easy to export your data in CSV format for external analysis

Atrius makes it easy to export your data in CSV format for external analysis.

There are five main places where you can export data:
- Buildings
- Points & Bills
- Data Manager
- Baselines
- Cards
- Exports app
- Emissions

**Buildings**

Go to Buildings on the left side menu. Switch to the table view at the top right of the page. Select one or more buildings using the checkboxes on the left side of the table. Then, go to Actions > Export building details.

**Points & Bills**

*Export data*: Go to Points or Bills on the left side menu. Select one or more points or bill points using the checkboxes on the left side of the table. Then, go to Actions > Export data.

*Exporting currencies*: If exporting cost data for points, the currency of the assigned pricing schedules are used in the export.

*Exporting data across multiple timezones*: All data will be exported in the local timezone of the building for each selected point.

*Export metadata*: To export metadata for your points and bill points, go to Actions > Export point details or Export bill point details.

**Data Manager**

Go to a point or bill point's Data Manager tab. Then, go to Actions > Export data.

**Baselines**

Go to a point or bill point's Baselines tab. Select the dropdown menu on the right side of the table for any baseline, then select 'View baseline data'.

**Cards**

Go to a dashboard, and select Actions > Download CSV. The downloaded ZIP file will consist of one CSV file per card.

**Exports**

Go to Apps on the left side menu, then select Exports. Select from the following options:
- Export portfolio data
- Export point data
- Export bill data

**Emissions**

Go to Apps on the left side menu, then select Emissions. Select 'Download table' at the top right of the table.

---
