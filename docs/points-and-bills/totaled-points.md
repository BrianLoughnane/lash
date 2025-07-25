---
title: "Totaled points"
updated: "Unknown"
---

# Totaled points

Totaled points and bill points make it easy to aggregate data across multiple points and bill points in Atrius.

Updated over a month ago

👍 This article will help you:

* Create Totaled points and bill points to aggregate point and bill point data
* Understand how to update point and bill point scopes using Add to building totals
* Troubleshoot common issues

#### Overview

Totaled Points are a new type of point object designed to simplify and automate the creation of whole building resource totals. They reduce the manual overhead required during onboarding and ongoing maintenance by efficiently summing up resource-level data within buildings.

1. Low-touch aggregation: Totaled Points immediately sum all points or bill points where Add to building totals is enabled for a given resource within a building.
2. Scope-locked: They always represent Whole Building scope and are not editable.
3. No custom logic: Unlike Calculated Points, Totaled Points do not allow custom formulas, only basic aggregation.

#### Create a Totaled Point

Totaled points are automatically created when Add to building totals is enabled for two or more points of a given resource with a building, and will be assigned a scope of Whole building.

Totaled points and bill points support different input point types. Totaled points are created from points only, while Totaled bill points are created from bill points or points.

Totaled points share the following characteristics with Calculated points:

* Edit fields:
  
  + Point name
  + Point short name
  + Atrius ID
  + Display unit
  + Description
* Assign tags
* Reference in calculated points
* View input point readings

#### Enable or disable Add to building totals

Add to building totals setting is primarily found on the Point profile.

* Yes - Include in the Whole building total
* No - Do not include in the Whole building total

The setting can also be found in:

* Batch point/bill point creation - Add to building totals column in upload CSV
* Points/Bills - batch actions allow users to select multiple points to Add to building totals
* Point/Bill point discovery - When connecting points directly from integrations pages, enable Add to building totals.

**Behavior**

If one point or bill point of a given resource in a building has Add to building totals enabled, the point's scope will automatically update to Whole building, making this single point representative of the whole building resource total.

When a second point (or more) has Add to building totals enabled:

* A new Totaled point is generated to aggregate the input points and represent the whole building resource total
* The scope of the Totaled point is set to Whole building
* The scope of the input points is updated to Sub-point

If, subsequently, points are removed from the Totaled point, leaving only a single point with Add to building totals = Yes, then the Totaled point will remain, with only the single point in it. At this stage, a user may choose to delete the Totaled point, in which case the single sub-point with Add to building totals = Yes will become the Whole building point.

---
