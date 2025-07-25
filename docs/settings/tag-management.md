---
title: "Tag Management"
updated: "Unknown"
---

# Tag Management

##### Assign tags to your points and bill points to group them for data aggregation and replication

Assign tags to your points and bill points to group them for data aggregation and replication.

**Overview**

Tag Management allows you to create and edit tags to assign to points and bill points. At this time, Atrius employs no formal rules for how tags can be used.

Tags are commonly used to describe building assets, in order to group assets within buildings and identify consistent assets across buildings.

Tags can be created in Tag Management, then assigned to any of your points and bills, and selected in cards to view data aggregations within your buildings and across your portfolio.

**Tag Dictionary and Types:**
- Tag Dictionary (reference): Select from a list of predefined tags or create a new custom tag:
  - Haystack: Haystack is a popular tagging system for describing building assets using semi-structured sets of tags.
  - Brick: Brick consists of an extensible dictionary of terms and concepts in and around buildings, a set of relationships for linking and composing concepts together.
  - Niagara: NHaystack is an open-source Niagara module that provides support for Project Haystack's RESTful protocol in Niagara stations.
  - Atrius (custom): Non-standard custom tag.
- Tag Type (reference): Marker tags do not have an associated value. String tags have an associated text value.

**Add a tag**

1. On the Tag Management page, select Add a tag in the upper right corner.
2. Select the appropriate options from the dropdown fields. At this time Tag Dictionary and Marker are only for reference.
3. Name your tag.
   - Tags only accept alphanumeric characters (letters and numbers) and the underscore symbol. Spaces are not accepted.

**Manage Tags**

Assign and remove tags via batch actions on the Points and Bills pages or on the point profile.

Filter by tags you've created on the Points and Bills pages, to view tagged points.

**Avoid double counting**

Be cautious tagging calculated points/calculated bill points or Whole building points/Whole building bill points with the same tag that is used for sub-points or sub-bills to ensure you aren't double counting when selecting these tag(s) in cards.

Note that when creating a card that displays "All data types," if you have a Whole building point and a Whole building bill point at the same building, with the same point type and the same tag, then only the Whole building point will be used to compute totals. This logic does not apply to cards with Metric = Emissions.

**Tags in Dashboards**

Tags can be selected in cards to visualize trends across tagged points.

Different cards display tagged data differently:
- Portfolio Trends/Portfolio Year-over-year: Select one or more tags assigned to any building in the portfolio, and the chart will return an intersection of the selected tags across the portfolio.
- Building Trends/Building Year-over-year/Building readout: Select one or more tags assigned to the selected building, and the chart will return an intersection of the selected tags.
- Portfolio Comparison/Building Comparison: Select one or more tags assigned to the selected category, building, building group, or type, and the chart will return an intersection of the selected tags.
- Stacked Breakdown: Select one or more tags assigned to the selected building, and the chart will return an intersection of the selected tags.

---
