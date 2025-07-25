---
title: "Callout adjustments"
updated: "over 10 months ago"
---

# Callout adjustments

##### Callout adjustments provide users with fine-grained control of how totals, averages, and percent differences are calculated in cards

Callout adjustments provide users with fine-grained control of how totals, averages, and percent differences are calculated in cards, and help determine how data gaps are handled.

Callout adjustments only affect the callout values at the bottom of cards, not the data displayed in the graph.

**Where are callout adjustments available?**

Callout adjustments are available for the following cards with callout sets:
- Portfolio Trends: Total this period, Total previous period, Difference / Total this period, Total same period previous year, Difference
- Portfolio Year-over-Year Trends: Total year period 1, Total year period 2, Difference
- Building Trends: Total this period, Total previous period, Difference / Total this period, Total same period previous year, Difference / Total, Total Baseline, Difference / Average this period, Average previous period, Difference / Average this period, Average same period previous year, Difference / Average, Average Baseline, Difference
- Building Year-over-Year Trends: Total year period 1, Total year period 2, Difference
- Building Comparisons: Total this period, Total previous period, Difference / Total this period, Total same period previous year, Difference
- Building Readout: Total this period, Total previous period, Difference / Total this period, Total same period previous year, Difference / Total, Total Baseline, Difference

**How do callout adjustments work?**

The following selections are available for callout adjustments:

*Period start*
- At period start date: Start date will be determined by the start date of the main period.
- At first available data: Start date will be determined by the first hour, day, month, or year with data in the main period or comparison period.

*Period end*
- At period end date: End date will be determined by the end date of the main period.
- At last available data: End date will be determined by the last hour, day, month, or year with data in the main period or comparison period.
- At "now": End date will be determined by where now is in the main period.

*Period data gaps*
- Include missing segments: All available data in the main period and comparison period between Period start and Period end will be included.
- Exclude missing segments: Any missing segments in the main period or comparison period between Period start and Period end will be excluded.

*Adjustments method*
- Unidirectional: Any adjustments to the main period will be applied to corresponding segments of the comparison period.
- Bidirectional: Any adjustments to the main period will be applied to corresponding segments of the comparison period. In addition, any adjustments to the comparison period will be applied to corresponding segments of the main period.

**Special considerations for portfolio-scope cards**

Portfolio-scope cards, as well as building-scope cards that aggregate many points, do not apply any callout adjustments by default.

- If Period start = At first available data, then the card will detect the first month of complete data for all 'Whole building' points of the selected point type.
- If Period end = At last available data, then the card will detect the last month of complete data for all 'Whole building' points of the selected point type.
- If Period data gaps = Exclude missing segments, then any missing segments across all 'Whole building' points of the selected point type will be excluded.

---
