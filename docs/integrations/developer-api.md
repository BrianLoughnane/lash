---
title: "Developer API"
updated: "over a month ago"
---

# Developer API

Manage and add new API clients for your organization. Administrator access is required.

#### 👍 This article will help you:

* Understand uses cases and prerequisites for the Developer API
* Configure and manage API clients
* Find complete API documentation

To access Developer API, go to Settings on the left side menu, then Developer API.

#### Overview

We anticipate the Developer API may be used by the following people: developers who build apps used by Atrius customers; customers who want access to their data; and students who host resource use reduction competitions.

Prerequisites:
* An Atrius user account with 'Administrator' access
* A registered OAuth2.0 client app in Atrius
* An authorization token created with your registered OAuth2.0 client

#### Add an API client

🚧 **Use a separate Atrius account for API client creation**

It is highly recommended that you do not use your personal Atrius user account for creating API clients. By creating an account specifically for use with the Developer API, you can ensure that the deactivation or deletion of a user account does not interfere with your API clients in the future.

To add an API client, select the 'Add an API client' button.

In the modal window, enter a client name and make the appropriate selections for your client, then select 'Save'. Your API client will appear in the main table, along with its Client ID and Client Secret.

| Field | Description |
| --- | --- |
| API client name | Enter a client name. |
| Client type | Select a client type: confidential or public. |
| Authorization grant | Select an authorization grant: authorization code, client credentials, implicit, resource owner password-based. Grant type determines how the server responds to system calls from your app. |
| Redirect URIs (optional) | Enter one or more URIs (one per line) to which Atrius will allow redirects. Redirect URIs are required for 'public' client types and 'authorization code' and 'implicit' grant types, but are optional for other configurations.  URIs that you provide are checked against the redirect\_uri sent by the client, and the request will be refused if not in the list. |
| Assigned user | Select an administrator user at your organization. |

#### Supported API functionality

The Developer API supports the following functionality. For more information, please view the full API documentation in Swagger.

| Feature | Function |
| --- | --- |
| Buildings | View a list of buildings View a list of building groups View a building image Create a building Update a building  Delete a building  Create a building group category  Create a building group View a list of building floors View a building floor Create a building floor Update a building floor Delete a building floor View air quality data for a building  View weather data for a building  View a tenant |
| Points | View a list of points View a point Create a point Update a point  View tags  Assign tags to points  Un-assign tags from points View data for a point View a list of bill points View a bill point Create a bill point Update a bill point View data for a bill point |
| Integrations | View a list of gateways View a gateway Post data to points or bills View a list of connectable points View a connectable point Update a connectable point Connect a point View a list of uptime notifications |
| Assets / Work Orders | View a list of assets View an asset Create an asset Update an asset Post work order data |
| Location Services | View a list of analytics points View an analytics point Create an analytics point Update an analytics point View readings for an analytics point Post data to an analytics point View a list of asset tags View an asset tag Create an asset tag Update an asset tag Post data to an asset tag View a list of asset tag categories View an asset tag category Update an asset tag category View a list of site controllers View a site controller Create a site controller Update a site controller |
| Dashboards / Storyboards | View a list of dashboard cards  View a card URL  View details of cards on a dashboard View a list of storyboards Create a storyboard chapter Update a storyboard chapter Delete a storyboard chapter View a storyboard logo Update a storyboard logo Delete a storyboard logo |
| File Library | View a list of files or folders View a file or folder Create a file or folder Update a file or folder Delete a file or folder |
| Organizations / Users | View a list of organizations View an organization Update organization settings View a list of users View a user |

---
