---
title: "Total Energy Calculations"
updated: "Unknown"
---

# Total Energy Calculations

##### Total energy, or all energy sources consumed by a building, enables a complete assessment of energy-related costs and emissions

Total energy, or all energy sources consumed by a building, enables a complete assessment of energy-related costs and emissions.

**'Whole building' scope**

Total energy calculations only take into account points and bill points in which the scope is set to Whole building. Points with scopes of Sub-point or Hidden will be ignored.

To change Point scope or Bill point scope, go to the Point Profile or Bill Point Profile.

*Note: when manually creating a Total Energy calculated point or bill point, ensure that the scope is set to sub-meter or sub-bill. Otherwise, all automatically occurring calculations of Total Energy will double count.*

**Total energy point types**

All Whole building points are converted to the appropriate unit and summed to determine total energy. By default, the following point types are included in the total energy calculation, if available:

- Cooling
- Electricity
- Energy
- Heating
- Natural gas

To specify which combination of point types represents total energy for your organization, go to Settings > Organization Settings. On the Profile tab, select the 'Set total energy point types' button. Electricity and natural gas cannot be deselected.

**Total energy in cards**

To create a card that displays total energy for a building, building group, or all buildings, go to Dashboards. Create a portfolio-scope or building-scope card, then select a Point type of 'Total energy'.

When Metric is set to 'Cost' for points, the cost is derived from consumption values using the Utility Prices engine. However, for bill points, the cost is taken directly from the bill.

*Note: If a building has both a Whole building point and a Whole building bill point for the selected point, the point will be used.*

---
