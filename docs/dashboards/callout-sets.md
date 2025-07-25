---
title: "Callout sets"
updated: "over 3 months ago"
---

# Callout sets

##### Callout sets display a summary of information found in a graph, or a set of related statistics that helps contextualize a graph, in cards

Callout sets display a summary of information found in a graph, or a set of related statistics that helps contextualize a graph, in cards.

In cards, select the Callouts field to change the callout set.

Callouts are driven, in part, by the selections you make for each card. For example, if you choose to divide by 'Area', then the values in the callouts will be normalized by area. Callouts are also flexible enough to provide options that don't rely on the other selections you make for each card.

**Choose the right callout set for the job**

Callouts are designed to be flexible by nature. But not all callout sets are the right choice for every data type and metric. For example, a graph of electricity demand with 'Total, Min, Max' as the callout set will sum the interval demand readings for 'Total'. Instead, choose a callout set that averages the interval demand, like 'Average, Min, Max'.

**General callouts**

Available callout sets include:
- None: Hides callouts below the graph.
- Total, Max: Sum of X and maximum value over the main period.
- Total, Min, Max: Sum of X, minimum value, and maximum value over the main period.
- Total, Peak demand: Sum of X and maximum 15-minute resolution peak demand value over the main period.
- Total this period, Total previous period, Difference: Sum of X over the main period and comparison period.
- Total this period, Total same period previous year, Difference: Sum of X over the main period and previous year comparison period.
- Total this period, Average temperature: Sum of X and average temperature over the main period.
- Total this period, Heating degree days: Sum of X and sum of HDD over the main period.
- Total this period, Cooling degree days: Sum of X and sum of CDD over the main period.
- Total, Total [Baseline], Difference: Sum of X and sum of the selected baseline over the main period.
- Average, Min, Max: Average of X, minimum value, and maximum value over the main period.
- Average, Peak demand: Average of X and maximum 15-minute resolution peak demand value over the main period.
- Average this period, Average previous period, Difference: Average of X over the main period and comparison period.
- Average this period, Average same period previous year, Difference: Average of X over the main period and previous year comparison period.
- Average this period, Average temperature: Average of X and average temperature over the main period.
- Average this period, Heating degree days: Average of X and sum of HDD over the main period.
- Average this period, Cooling degree days: Average of X and sum of CDD over the main period.
- Average, Average [Baseline], Difference: Average of X and average of the selected baseline over the main period.
- Min, Max: Minimum value and maximum value over the main period.
- Peak demand: Maximum 15-minute resolution peak demand value over the main period.

**Advanced callout adjustments**

Callout adjustments provide users with fine-grained control of how totals, averages, and percent differences are calculated, and help determine how data gaps are handled.

**Average callouts when dividing by a trended point**

In Building Trends and Building Year-over-Year Trends cards, average callouts for bar charts are computed using the following method, which is more accurate if there are any missing data during the period:

Average = Total main point over selected period / Total trended point over selected period

On the other hand, average callouts for table charts are computed by taking an average of the individual rows in the table:

Average = Sum of rows in table / Number of rows in table

**Work orders callouts**

Available work orders callout sets include:
- Work tasks cost, Work tasks: Cost and quantity of all work tasks.
- Parts cost, Labor cost, Other costs: Component costs of work tasks.
- Parts cost, Labor cost: Component costs of work tasks.
- Parts cost, Parts work tasks: Parts cost and quantity of work tasks.
- Labor cost, Labor work tasks: Labor cost and quantity of work tasks.

---
