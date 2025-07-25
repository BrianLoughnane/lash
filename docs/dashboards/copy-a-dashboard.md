---
title: "Copy a dashboard"
updated: "over a year ago"
---

# Copy a dashboard

##### Copy dashboards—across your building portfolio—with ease

The 'Copy to' function allows users to create custom building dashboards, copy them to other buildings in the portfolio, and automatically update cards according to the specified buildings.

To access Dashboards, go to Dashboards on the left side menu, or Apps > Dashboards.

**Copying a dashboard**

Step 1: Create a dashboard

Step 2: Set your dashboard scope to 'Building'
- Actions > Dashboard settings > Scope: Building > Set building

Step 3: Copy to one or more buildings of your choice
- Select a single building or multiple buildings
- Enter a dashboard title: Use the text boxes to enter a custom title that includes the building name

**Use caution when copying**

Attempt to copy a single dashboard and validate before copying across multiple buildings.

Ensure the destination buildings you've selected have the appropriate data before copying.

Cards that do not contain attributes that link them to the specified building may not reflect changes in the copied dashboard versions. This includes: Stacked breakdown card, Multi-point trends card, Image card, Text card, HTML embed card, Project Profile card, Competitions card, and all Tenant cards.

**Exception handling**

After a dashboard has been copied, a green banner will appear at the top of the screen, with a link to the data processing job. Click the link to monitor the job status and identify any cards or fields that were unable to be copied.

**Copying behavior**

*Building cards*: If the building on the card matches the dashboard scope building, then the card will adopt the destination building when copied. If the building on the card does not match the dashboard scope building, then the card will be copied as is.

*Building group cards*: If a building group or type is selected on a card, then the dashboard scope building will be used to match the building group to its respective category. If the destination building does not have a building group under that category, the card will not be copied to the destination dashboard.

*Portfolio cards*: Portfolio cards will be copied as is between building dashboards in the same organization.

**Card fields behavior:**
- Data type: The matching data type will be used in the destination dashboard. If no matching data type exists, the card will not be copied.
- Point type: The matching point type will be used in the destination dashboard. If no matching point type exists, the card will not be copied.
- Point: Only Whole building points can be copied from building to building. Cards displaying sub-points will not be copied.
- Tags: Tags can be copied from building to building. If multiple tags are used, the destination building must have all tags, otherwise the card will not be copied.
- Metric: The matching metric will be used in the destination dashboard. If no matching metric exists, the card will not be copied.
- Overlay Divided by Normalization: Available overlays, divided by, and normalization options, will be checked for in the destination building. If they are not available, the card will be copied without this field.
- Unit Chart type Call outs: Fields will be copied as is.

**Use tags to copy sub-points**

Tags can be used to identify specific points or point groups across your building portfolio. They can be useful to identify specific types of points that you want copied from one dashboard to another, and can even include sub-points.

---
