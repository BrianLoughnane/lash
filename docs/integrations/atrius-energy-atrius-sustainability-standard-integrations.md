---
title: "Atrius Energy & Atrius Sustainability Standard Integrations"
updated: "Unknown"
---

# Atrius Energy & Atrius Sustainability Standard Integrations

Browse a list of our most common utility bill and meter integrations, both direct and from third party systems or devices.

Updated over a week ago

🚧 Integrations require varying levels of support to set up and maintain. Work with our Sales and onboarding teams to ensure the best fit for your buildings and goals.

#### Atrius Direct

**Atrius API**
* Requires a registered OAuth2.0 client app in Atrius. Users can GET, POST, PUT, PATCH, and DELETE a variety of attributes including meta data and point data.

**Atrius Bills**
* Post JSON or CSV files to bill points (cost and consumption).
* No authentication; less secure.

**Atrius CSV**
* Trended data pushed via HTTPS or sFTP on a recurring basis. A Visual Basic script can be provided for use with standard Windows-based servers. In conjunction with the Microsoft Task Scheduler, this script is designed to scrape CSV files from a specified local directory and transmit them in the body of an HTTP requestor. Atrius will supply sFTP credentials for integrations that do not support direct HTTPS data transmission.
* Requires outbound access via http (port 80) or https (port 443), depending on customer's security requirements.

**Atrius JSON**
* JSON gateways can be used to integrate with Apex devices via registered OAuth2.0 client.
* JSON gateways can also be used without authentication (less secure) for trended data pushed via HTTPS.

**Atrius Work Orders**
* Connects a customer's Work Order system to Atrius via an HTTP POST, authenticated via OAuth2.0.
* Atrius allows users to browse work order inventories, visualize work order cost and activity over time, and export work order information. Work orders cannot be created in Atrius.

**Manual Points**
* Manually add data via CSV using Atrius batch upload tools.

#### Building Automation Systems

**ALC WebCTRL**
* Requires an Energy Reports Data Connector add-on to WebCTRL with a network connection via outbound HTTPs POST.

**Distech Controls EC-Net Facilities**
* Allows posting of data via the Atrius secure API from a supported EC-Net Facilities system. Requires licensing and network configurations.

**Niagara N4**
* Allows posting of data via the Atrius secure API from a supported N4 driver. Requires licensing and network configurations.

#### Edge Devices

**Distech Controls Apex**
* Allows posting of data from an Apex device using a JSON gateway via a secure registered OAuth2.0 client.

**eGauge**
* Communicates to Atrius via direct upload of XML data to Atrius cloud servers with a network configuration that allows outbound HTTP POST.
* Requires outbound access via http (port 80) or https (port 443), depending on customer's security requirements.

#### Utilities & Bills

**Arcadia Bills**
* Arcadia is an Atrius partner providing utility bill cost and consumption data directly to Atrius from a library of over 10,000 utility providers.

**Arcadia Interval Data**
* Provides automated daily deliveries of prior-day interval meter readings for electricity, natural gas, and water usage from over 100 utility providers.

**Capturis (powered by Conservice)**
* Capturis is a bill pay provider that integrates directly with Atrius to send bill consumption and cost data via an sFTP transfer specific to each customer.

**Manual Bills**
* Manually add data via CSV using Atrius batch upload tools.

#### Energy Star

**Energy Star Portfolio Manager**
* Allows users to push bill and point consumption data from Atrius to their Energy Star account.
* Allows users to pull consumption data, Energy Star score, Site EUI, and Source EUI from Energy Star into Atrius.

---
