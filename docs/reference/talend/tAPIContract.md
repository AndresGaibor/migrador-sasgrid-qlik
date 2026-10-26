<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/tapicontract · versión 8.0 -->
# tAPIContract

Last updated: 9/30/2026

Availability-note[Beta](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-beta)

Beta content

Loads and manages the API contract used as the source definition for API-first Data Services.

tAPIContract initializes a Data Services implementation from an OpenAPI contract so operations and response definitions can be configured from the same source.

## tAPIContract Standard properties

These properties are used to configure tAPIContract running in the Standard Job framework.

The Standard tAPIContract component belongs to the ESB family.

*This component is relevant only when used with one of the 
Talend
 solutions with ESB, as it should be used with the Service Repository node and the Data Service creation related wizard(s).*

## Basic settings

| Properties | Description |
| --- | --- |
| API definition | In Definition, select the REST API definition from the repository. Click Add to add the REST API definition to the component. |
| Method | Select the HTTP method filter for listed operations: All, GET, POST, PUT, PATCH, or DELETE. |
| Operation table | Displays operations from the selected definition with the columns Operation, Path, Operation ID, and Component. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Server port | Specifies the port used by the API service endpoint. |
| Servlet context path | Specifies the servlet context path used to expose the API service. |
| API base path | Specifies the base path prefix for API operations. |
| tStatCatcher Statistics | Select this checkbox to collect runtime metrics for this component. |

Availability-note[Beta](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-beta)

Beta content

## Security

tAPIContract maps the security schemes in the OpenAPI contract to runtime security profiles for the API-first service. The contract defines the required security; the runtime profile provides its implementation.

When you add or update an API definition, review the Operations and Security tabs in the Assign components to operations dialog.

| Area | Description |
| --- | --- |
| Contract security | Classifies operations as Security required, Explicitly public, Optional authentication, No security declared, or Invalid / unresolved. |
| Runtime implementation coverage | Shows whether security-required operations are Ready, Configuration required, or Unsupported. |

The supported mappings are:

| OpenAPI scheme | Compatible runtime profile |
| --- | --- |
| HTTP Basic | Basic Auth |
| HTTP Bearer, OpenID Connect, or OAuth 2.0 | JWT OIDC (Dynamic) or JWT Static |
| API key, mutual TLS, or another HTTP scheme | No runtime profile in this release |

For the complete workflow, including profile providers, defaults, saving behavior, and update outcomes, see [API First security](esb-rest-api-first-security "Review contract security and map supported OpenAPI security schemes to runtime profiles for an API-first service.").

## Usage

Use tAPIContract at the beginning of API-first Data Services
implementations to define the API contract and map its security schemes before configuring
operation request processing and responses with tAPIOperation and
tAPIOperationResponse.

A typical workflow is to import or update the OpenAPI contract, review the effective security for operations, create or select a compatible runtime profile, map the contract scheme to that profile, save the component assignments, generate the Job, and test the protected operation with the required authentication data.
