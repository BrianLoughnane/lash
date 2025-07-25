---
title: "Emissions"
updated: "Unknown"
---

# Emissions

#### Emissions

Updated over 2 weeks ago

##### Emissions allow you to view annual emissions, create custom emissions factors, and use our library of standard factors for disclosure

Emissions allows you to view annual building emissions, create custom emissions factors, and use our library of 500+ standard factors to facilitate emissions reporting for your entire organization and its value chain.

To access Emissions, go to Apps on the left side menu, then Emissions.

**Building Emissions**

This page displays total emissions and emissions factors for all buildings.

- Filter to select the emission scope, point type, building, or group of buildings for which you want to view emissions or assign factors.
- Change the period to reflect the time range over which these factors should apply.
- Change the calendarization method.
- Change the unit you wish to display the data.
- Click on a building name, to expand the table to see a list of points within that building.
- Select one or more buildings or points using the checkboxes on the left of the table.

**Scope 1, 2, & 3 Emissions**

Aggregate Scope 1, 2, 3, and Total Emissions for your building or portfolio to view in Emissions and Dashboards.

Standard factors are assigned a default Scope and Reporting category that can be used to group and visualize data for emissions reporting.

**Assign or edit an emission factor**

Many data points will have default emission factors assigned.

Click the drop-down arrow to the right of a building or point to edit or assign an individual factor. To edit, add, or remove emission factors:

With your building(s) or point(s) selected, an Actions menu will appear. Go to Actions, then select:
- Edit factor overwrites existing assignments
- Add factor adds the selected factor configuration
- Remove factor removes the selected factor configuration

**Batch actions**: Select multiple buildings or points of the same point type to perform batch actions.

**Add to emissions total**

All active points and buildings can be assigned emission factors in Emissions but only points with Add to emissions total enabled will be included in emissions totals shown in Dashboards.

**Use the 'Add to emissions total' setting to calculate portfolio emissions**

This setting can be enabled on the Point Profile. If Add to emissions total is set to:
- Yes - Emissions for the selected point are included in the totals displayed in Dashboards
- No - The selected point will not be included in emissions totals

---

#### Standard Factors

Updated over 3 months ago

##### Emission factor libraries provided by Atrius

Atrius uses standard factors if no custom factors are provided.

**Standard emissions factors are sourced from:**
- U.S Environmental Protection Agency (EPA) GHG Hub
- EPA Supply Chain (USEEIO)
- Market-based electricity (Green-e)
- UK Department for Energy Security and Net Zero (UK DEFRA)
- Ministry for the Environment, New Zealand (MfE (NZ))
- National Government of Australia (NGA) & NGERS
- International Energy Agency (IEA)

Standard factors are assigned automatically when data for a corresponding point type is uploaded. You can visit the Emissions app's Standard Factors page, to review the lists of factors available, each corresponding to the point type they support.

**Emission factors assignments are forward-populating**

For your convenience, any custom emission factors or standard emission factors that are assigned to a building will continue to apply to the building in subsequent years—unless and until you have assigned new, updated factors to the building.

**Default emission factors**

Building default factors will be assigned to your data points automatically if there is a factor available for the given point type.

View and configure which default factors are set in Organization settings.

**Default emission factor assignment logic**

*Annual assignments*: We use industry best practices to determine which emission factor inventory year is assigned to the given data year.

*Regional assignments*: If a point type has multiple emission factors available in the selected default emission factor categories, the emission factor will be assigned according to the following default ranking:

- U.S. buildings: eGRID subregion, NERC, U.S. average
- Non-U.S. buildings (North America): Canada (CAN)
- Non-U.S. buildings (UK and Europe): IEA, UK DEFRA, EPA
- Non-U.S. buildings (Australia): Top priority: NGA
- Non-U.S. buildings (New Zealand): Top priority: MfE

**What is Greenhouse Gas Protocol?**

According to GHG Protocol, it is an established global framework that measures greenhouse gas (GHG) emissions spanning private and public sector operations, value chains and mitigation actions.

---

#### Custom Factors

Updated over a year ago

##### Create and manage custom emission factors for your organization

Create and manage custom emission factors for your organization.

**Create a custom factor**

Select the 'Add a factor' button.

Enter data for the following fields:
- Title: Enter a title.
- Point type: Select the appropriate point type or resource.
- Scope: Select the scope of which to classify the emissions.
- Reporting category: Select the reporting category of which to classify the emissions.
- Period: Select the time range over which the factors should apply.
- Unit: Select the unit for this point type or resource.
- CO2e: Choose to automatically calculate CO2e based on the inputs for other GHGs or enter a custom value.
- GHGs: Enter a value, expressed in the appropriate unit, for one or more greenhouse gases: CO2, CH4, N2O, NOx, SO2.
- Default factor: Select whether to use this custom factor as the default emission factor for all buildings.

**Edit a custom factor**

Custom factors can be edited individually, by selecting the carat to the right of the factor or in batch, by selecting multiple factors, navigating to the Actions dropdown, then Edit factor(s).

If editing, the emission scope or reporting category, select the checkbox for Update scope and reporting category for all existing assignments? to apply the change where the factor is assigned.

---

#### Step-by-step reporting

Updated over 3 months ago

##### How to use Atrius Sustainability for carbon accounting and emissions reporting

**Step 1: Upload your resource use data**

Use the data from your existing integrations or create manual points and bill points using the Batch Point Creation Apps.

If you're planning on using the default emission factors that we provide, make sure to check our list of Standard Factors, which correspond directly to point types.

Next use the Batch Data Upload apps for point data or bill point data to upload your resource use data.

**Step 2: Configure your data points**

Atrius Sustainability uses the Add to emissions total setting to aggregate portfolio-level emissions data throughout the platform.

Filters in the Points and Bills tables allow you to see which points have this setting enabled or disabled.

**Step 3: Ensure your data quality**

Use the Data Quality app to see a high level overview of your data. Identify and fills gaps or analyze your percent completeness, before moving onto the next step.

**Step 4: Validate and assign emission factors**

Once all your points have been configured, navigate to the Emissions app to ensure your points have the desired emission factors assigned and are grouped according to your desired emission scope and scope categories.

In the Emissions app's Building Emissions tab, select the year you'd like to report on, and toggle the table to 'Factors' to see what emission factors and emission scopes have been assigned to each building.

To update an emission factor, scope, or scope category follow the steps outlined here. You may also choose to create a custom factor if you have a specific emission factor you'd like to use that isn't covered by our Standard Factors.

**Step 5: Aggregate and report**

After you've confirmed that your emission factors are assigned and your points are classified according to your desired emission scopes and scope categories, you are ready to report!

On the Emissions App's Building Emissions tab, toggle to 'Totals', select your reporting year, and filter by emission scope or scope category to calculate your totals according to the parameters in your filter.

You can also use Dashboards to create custom emissions reporting summaries, that can be shared, downloaded as CSVs, and quickly duplicated for your next reporting year.

**Audit-friendly data**

Whenever you're using data for emissions reporting, make sure to download a CSV copy of the Emissions table, or your dashboard to capture a summary of your data and emissions factors at that point in time, and upload it to the Files app.

---

#### Reporting

Updated over 4 months ago

##### Atrius Sustainability enables users to aggregate and report on data according to global frameworks and local requirements

**Voluntary Reporting**

*CDP*: The Carbon Disclosure Project (CDP) is a non-profit organization that promotes the measurement and disclosure of environmental data, helping companies, investors, and governments track carbon emissions, climate risks, and sustainability efforts.

Environmental Performance - Climate Change:
- Scope 1, 2, and 3 Emissions: Sections 7.6 - 7.12
- Emissions breakdown: Sections 7.15 - 7.23.1
- Energy-related activities: Sections 7.29 - 7.52

*GRESB*: The GRESB Real Estate Assessment is an investor-driven ESG benchmark and reporting framework for real estate companies and investors, evaluating sustainability performance across regions and property types.

GRESB Real Estate Assessment Annual total breakdown by building/tenant:
- Consumption: Fuels, Heating & cooling, Electricity, Water, Waste
- GHG emissions: Scope 2 location-based, Scope 2 market-based, Scope 3
- GHG offsets purchased

*SASB*: The Sustainability Accounting Standards Board (SASB) is a non-profit organization that provides industry-specific sustainability accounting standards to help companies manage and report on ESG issues material to their business.

- Energy consumption
- Water consumption
- Waste consumption
- Emissions production
- Diversion calculations

*GRI*: The Global Reporting Initiative (GRI) is an international organization that offers a widely used framework for sustainability reporting, covering ESG topics such as climate change, human rights, labor practices, and supply chain sustainability.

Disclosures include:
- 301-1 Materials used by weight or volume
- 301-2 Recycled input materials used
- 301-3 Reclaimed products and their packaging materials
- 302-1 Energy consumption within the organization
- 302-2 Energy consumption outside of the organization
- 302-3 Energy intensity
- 302-4 Reduction of energy consumption
- 302-5 Reductions in energy requirements of products and services
- 303-5 Water consumption
- 305-1 Direct (Scope 1) GHG emissions
- 305-2 Energy indirect (Scope 2) GHG emissions
- 305-3 Other indirect (Scope 3) GHG emissions
- 305-4 GHG emissions intensity
- 305-5 Reduction of GHG emissions
- 305-6 Emissions of ozone-depleting substances (ODS)
- 305-7 Nitrogen oxides (NOx), sulfur oxides (SOx), and other significant air emissions [PARTIAL]
- 306-3 Waste generated
- 306-4 Waste diverted from disposal
- 306-5 Waste directed to disposal

*EPA's Energy Star Portfolio Manager*: Portfolio Manager is an online resource management tool that allows users to benchmark energy use for various building types, and is widely used, with nearly 25% of U.S. commercial buildings actively participating.

- Connect ESPM properties and meters to Atrius
- Set up automated reporting of monthly Atrius resource consumption data to ESPM

**Mandatory Reporting**

*CSRD*: The Corporate Sustainability Reporting Directive (CSRD) is a European Union regulation requiring large companies to disclose detailed information on their environmental, social, and governance (ESG) practices.

- ESRS E1-5 and E1-6 Climate Change
- ESRS E2-4 Pollutants [PARTIAL]
- ESRS E3-4 Water
- ESRS E5-5 Waste

*NABERS*: NABERS (National Australian Built Environment Rating System) is a government initiative that measures the environmental performance of buildings in areas such as energy efficiency, water usage, waste management, and indoor environment quality.

---
