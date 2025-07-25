---
title: "Assets"
updated: "Unknown"
---

# Assets

#### Assets

Updated over a year ago

##### Assets allows you to browse asset inventories, visualize when assets have been purchased or installed, and create asset dashboards

Assets allows you to browse asset inventories, visualize when assets have been purchased or installed, and create asset dashboards that combine maintenance and energy data.

To access Assets, go to Apps on the left side menu, then Assets.

**Definitions**

Assets can be fixed (e.g., sink, ceiling fan) or portable (e.g., furniture, IT equipment), inside (e.g., overhead light fixture) or outside (e.g., parking lot light fixture).

Assets can have work orders associated with them. Work orders represent the maintenance and lifecycle costs of an asset.

**Add new assets**

Atrius provides a standard format for pushing assets data via a JSON API or CSV upload. You may also upload a single asset at a time.

- JSON API: Go to Settings > Developer API to learn more.
- Single or Batch CSV Upload: Go to Apps > Assets, then choose 'Add an asset' to add a single asset or multiple assets.

**Adding custom attributes to an asset**

You can add custom attributes, or fields, to asset profiles to store additional metadata.

**Graph & table filtering**

On the main Assets table, you can filter by:
- Building: Select one or more buildings for which assets are assigned.
- Category: Select one or more asset categories.
- Type: Select one or more asset types.
- Manufacturer: Select one or more manufacturers that produced the asset.
- Model: Select one or more asset models provided by the manufacturer.
- Status: Select one or more statuses of the asset.
- Period: Select a time period over which to view asset trends.

---

#### Asset Profile

Updated over a year ago

##### Update your assets' profiles to include important asset information and settings

Update your assets' profiles to include important asset information and settings.

To access Asset Profile, go to Apps on the left side menu, select Assets, select an asset, then select Profile from the tab menu.

**Adding custom attributes to an asset**

You can add custom attributes, or fields, to asset profiles to store additional metadata.

**Asset Details**
- Asset name: The asset's name.
- Asset category (optional): The highest level categorization of the asset.
- Asset type: The second-highest level categorization of the asset.
- Asset photo: The asset's profile photo. At least 500x500 pixels is recommended.
- Quantity (optional): The quantity of this asset.
- Manufacturer (optional): The asset's manufacturer.
- Model (optional): The asset's version name or number.
- Serial (optional): The asset's serial number.
- Rating (optional): The asset's primary metric.
- Rating unit: The rating metric's display unit.
- Description (optional): The asset's description or other notes.
- Default dashboard: The asset's default selected dashboard.
- Status: The asset's current status: Active or Retired.

**Location**
- Building (optional): The asset's building location.
- Space (optional): The asset's building space location.
- Asset tag (optional): The asset's associated asset tag.

**Warranty**
- Date installed (optional): The date when the asset had been installed.
- Warranty end date (optional): The date at which this asset is no longer covered by a warranty.
- Life expectancy (optional): The asset's life expectancy in years.
- Condition assessment (optional): The asset's condition assessment: Excellent, Good, Fair, Poor.

**Additional Details**
- Unit price (optional): The asset's total purchase price.
- Vendor asset ID (optional): Vendor asset ID is a unique identifier that links an asset from a third-party system integration to an asset in Atrius.

---

#### Work Orders

Updated over 11 months ago

##### Work Orders allows you to browse work order inventories, visualize work order cost and activity over time, and export work order information

Work Orders allows you to browse work order inventories, visualize work order cost and activity over time, and export work order information for further analysis.

To access Work Orders, go to Apps on the left side menu, then Work Orders.

**Definitions**

Work orders are requests for maintenance, repair, or installation of something in a building. A work order specifies what the problem is, where the problem is, how much the problem costs, and who it is assigned to.

Work tasks are the individual jobs and assignments necessary to complete an overall work order request.

Work task costs are cost line items for a given work task.

**Work orders graph & table filtering**

On the main Work Orders table, you can filter by:
- Building: Select one or more buildings for which work orders have been submitted.
- Space: Select one or more spaces for which work orders have been submitted.
- Tenant: Select one or more tenants for which work orders have been submitted.
- Problem Type: Select one or more problem types for which work orders have been categorized.
- Assignee: Select one or more assignees for whom work orders have been assigned.
- Status: Select one or more statuses in which work orders may be presently classified.
- Maintenance Type: Select whether work orders were reactive or preventive.
- Period: Select a time period over which to view work order trends.

**How period selection works**
- Work order costs are included in a given period selection if the 'Date charged' for the work task also occurs within the range of the period.
- Work order counts are included in a given period selection if the 'Date requested' for the work task also occurs within the range of the period.

---
