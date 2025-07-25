---
title: "Arcadia Bills"
updated: "over 3 months ago"
---

# Arcadia Bills

#### 👍 This article will help you:

* Understand best practices for the Arcadia Bills integration
* Troubleshoot the Arcadia Bills integration

To view your Arcadia Bills points, select Bills on the left navigation bar and filter by Integration > Arcadia Bills. You can also go to Settings on the left navigation bar, select Integrations, then select Arcadia Bills.

#### Overview

Arcadia is an energy data company that enables the integration and automation of utility invoice and smart meter data. The Arcadia Bills integration is used to display cadenced invoice data for electricity, natural gas, water, sewer, and sanitation from over 10,000 utility providers.

#### Data Flow Responsibilities

Maintaining accurate and current data in Atrius is an ongoing process, requiring periodic attention and revision by the customer. Below outlines the responsibilities of both the customer and Atrius to ensure good data quality is achieved.

Customer: The customer must periodically review their bill points to ensure the bill point profile is configured correctly and the data manager values are accurate, current, and well-organized. If an issue is identified, please follow the troubleshooting steps outlined below.

Atrius: After the customer has followed the outlined troubleshooting steps, and if no resolution is achieved, Atrius will work with Arcadia to repair the identified bill point data quality issues in the platform.

#### Data Delivery Expectations

The below table outlines our service-level agreement for Arcadia bill data delivery from the time the bill is posted by the provider:

| Delivery Type | Definition | SLA (business days) |
| --- | --- | --- |
| Recurring delivery | Regular cadenced delivery of data for enrolled accounts | 7 days |
| New account: top-of-stack bill | Delivery of the most recent bill available for a newly enrolled account | 10 days |
| New account: historical data delivery | Delivery of the historical data (if available) for a newly enrolled account | 15 days |

Atrius processes the bill data we receive from Arcadia on a nightly basis. Please allow 1 additional business day for bill data to appear in Atrius. Bill data is often delivered earlier than the SLA states. All SLAs are subject to change due to a delay in the provider issuing a bill, a data extraction issue, or blocked access.

#### Troubleshooting Outdated Arcadia Accounts

An Outdated status indicates that the bill point has not received a new utility bill within the Offline threshold configured on the bill point profile. Recommended offline threshold for Arcadia bill points is 60 days.

---
