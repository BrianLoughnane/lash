---
title: "Atrius CSV"
updated: "over a month ago"
---

# Atrius CSV

#### 👍 This article will help you:

* Understand formatting requirements and data flow
* Troubleshoot your Atrius CSV integration

To view your current Atrius CSV integration details and status, go to Settings on the left side menu, select Integrations, then select Atrius CSV.

#### Overview

Many building systems are capable of trending data to a CSV file, which can then be pushed via sFTP or HTTPS to Atrius on a recurring basis. A Visual Basic script can be provided for use with standard Windows-based servers. In conjunction with the Microsoft Task Scheduler, this script is designed to scrape CSV files from a specified local directory and transmit them in the body of an HTTP request. Customer Support will supply sFTP credentials for integrations that do not support direct HTTPS data transmission.

#### Troubleshooting

Review common troubleshooting steps that may restore communication between an offline CSV integration and Atrius.

**If all Atrius CSV points are offline**
* Reboot the dedicated server that is generating the CSV data file(s).
* Verify that port 80 outbound is enabled to push data out over HTTP. In some instances, you will need to confirm port 443 outbound is also enabled for HTTPS (SSL) depending on your organization's security requirements.
* Verify any scheduled tasks that either generate or deliver the CSV data file from your organization to Atrius.
* Verify and/or correct any recent formatting changes to the CSV data file. This can include changes to the Timestamp or Header formatting and/or changes to the Point ID Names.

Point IDs in your CSV file must match the existing Point IDs in Atrius. Go to Integrations to view current Atrius CSV integration details. If you require assistance with changing these Point IDs, please contact Customer Support.

**If only a partial list of Atrius CSV points are offline**
* Ensure that individual Point IDs and Point Values exist within your CSV data file. For example, if your CSV file includes text ("none"), null values ("null"), or blank values (" "), Customer Support will interpret the data as offline.
* Verify that the individual metering hardware/devices are reporting expected values.

**If any Atrius CSV points are flatlined**
* Verify that the individual metering hardware/devices are reporting expected values.

---
