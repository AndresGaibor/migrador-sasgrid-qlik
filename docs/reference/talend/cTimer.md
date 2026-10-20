<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-orchestration/ctimer · versión 8.0 -->
# cTimer

Last updated: 9/30/2026

Schedules message exchanges in a Route.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cTimer Standard properties

These properties are used to configure cTimer running in the Standard Job framework.

The Standard
cTimer component belongs to the Orchestration family.

## Basic settings

| Properties | Description |
| --- | --- |
| Period | Fill this field with an integer (in milliseconds) to generate message exchanges every period. |
| Repeat | Specifies a maximum limit of message exchange numbers. A value of zero or negative will generate message exchanges forever. |
| Delay | The number of milliseconds to wait before the first message exchange is generated. This option should not be used with the Set Schedule Time option. |
| Fixed Rate | Select this check box to generate message exchanges at regular intervals, separated by the specified period. |
| Daemon | Specify whether the thread associated with the timer endpoint runs as a daemon. |
| Set Schedule Time | Select this check box to specify the time that the first message exchange should be generated. In the Time field, enter the time using the pattern yyyy-MM-dd HH:mm:ss or yyyy-MM-dd'T'HH:mm:ss. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cTimer can only be used as a start component in a Route. |
| Limitation | n/a |
