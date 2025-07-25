---
title: "Capturis"
updated: "over 2 weeks ago"
---

# Capturis

#### 👍 This article will help you:

* Understand the Capturis integration as it relates to Atrius
* Learn how the integration process works and what roles each party plays
* Know who to contact if issues arise

#### Overview

Capturis (powered by Conservice) is a utility bill expense management system that integrates directly with Atrius to deliver monthly utility bill data for customer accounts across multiple providers. The customer must have a direct contract and account with Capturis in order to integrate with Atrius. Each integration is unique to the customer and must be configured in collaboration with the Capturis team and the Atrius onboarding team.

Once authorized, Capturis pushes meter-level utility bill data to Atrius via a secure sFTP connection set up for each customer organization. Atrius provisions the FTP account, provides credentials, and configures an organization-specific data gateway for receiving the Capturis data feed.

#### Integration Process

To get started with Capturis:

1. Customer confirms they have a Capturis account and are ready to integrate with Atrius.
2. Atrius sets up an sFTP account for the customer, including:
   * Customer-specific directory and credentials
   * A unique Atrius Gateway URI
3. Customer shares the credentials with Capturis to configure the data push on their end.
4. Capturis maps and transmits monthly utility data, broken down by building, utility, and account.
5. In Atrius, the customer (with help from the Atrius onboarding or CSM team) uses the Bill point discovery process to connect bill points to buildings.
6. Capturis continues sending monthly bill data on a regular cadence (including bill corrections or updates to existing bill readings when applicable).

#### Troubleshooting

If any issues arise (e.g. missing accounts or data accuracy issues), it is the customer's responsibility to work directly with their Capturis contact or support team to correct the data and re-push to Atrius.

---
