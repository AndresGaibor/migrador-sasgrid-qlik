<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/concompletion · versión 8.0 -->
# cOnCompletion

Last updated: 9/30/2026

Adds custom process when the original message exchange is
complete.

This component provides a simplified way to handle actions that should
occur after one or multiple sub-Routes complete their processing and makes it easier to manage
final result handling, such as auditing, logging, or cleanup operations, without requiring
additional custom logic or interceptors.

For more information, see the Apache camel
documentation <https://camel.apache.org/components/latest/>.

Information noteNote: This
component is available only if you have installed the R2026-01 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## cOnCompletion Standard properties

These properties are used to configure cOnCompletion running in the
Standard Job framework.

The cOnCompletion component belongs to the Exception Handling family.

## Basic settings

| Properties | Description |
| --- | --- |
| always | Select this option to trigger the completion task after the original message exchange is complete. |
| failure only | Select this option to trigger the completion task only if the original message exchange fails. |
| use original message | Select this checkbox to use the message in the original Route. |
| Mode | * After Consumer: cOnCompletion runs after the   original message exchange is done. * Before Consumer: cOnCompletion runs before the   original message exchange is done. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cOnCompletion is a start component of a sub-route. |
| Connections | * Row / Route: Select this link to pass   on all the messages to the next component. * Trigger / When: Select the   When link and click the   Component view.  In the Type list, select the type of language you   will use to declare your condition.  In the Condition field, type in the condition that   will be used to filter the messages.  All the messages that do not match this condition are dropped by default. |
| Limitation | To keep the original sub-routes untouched, cOnCompletion only be used in a separate sub-route. |
