<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/clog · versión 8.0 -->
# cLog

Last updated: 9/30/2026

Logs message exchanges in a Route.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cLog Standard properties

These properties are used to configure cLog running in the Standard Job framework.

The Standard
cLog component belongs to the Miscellaneous family.

## Basic settings

| Logging Category | Enter the name of the logging category to use. |
| Level | Select a logging level from DEBUG, ERROR, INFO, OFF, TRACE, or WARN. |
| Options / None (For default output log message only) | Select this option to take no action on the log message. |
| Options / Specifies a group size for throughput logging (For default output log message only) | Select this option to use throughput logging and specify a group size for the throughput logging.  Size: Enter an integer that specifies a group size for throughput logging. |
| Options / Group message stats by time interval (in millis) (For default output log message only) | Select this option to use throughput logging and group message statistics.  Interval: Specify the time interval (in milliseconds) by which the message statistics will be grouped.  Delay: Set the initial delay (in milliseconds) for message statistics. |
| Options / Format the log output (For default output log message only) | Select this option to format the output log message. Click [+] as many times as required to add arguments to the table. Then click the corresponding Value field and enter a value. See the site <http://camel.apache.org/log.html> for available options. |
| Options / Specify output log message | Select this option to specify the output log message instead of using the default output log message provided by the underlying logging mechanism.  Message: Use Simple language to construct a dynamic message which gets logged. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cLog is used as a middle or end component in a Route. |
| Limitation | n/a |

**Related concepts**  

* [Intercepting subRoutes from given component](cintercept-cfile-cprocessor-cstop-intercepting-subroutes-from-given-component)
