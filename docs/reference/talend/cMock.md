<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-testing/cmock · versión 8.0 -->
# cMock

Last updated: 9/30/2026

Simulates message generation and message endpoints for testing Routes and
mediation rules.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cMock Standard properties

These properties are used to configure cMock running in the Standard Job framework.

The Standard
cMock component belongs to the Testing family.

## Basic settings

| Properties | Description |
| --- | --- |
| Validate message count | Select this check box to test that the correct number of messages are received on each endpoint. Specify the expected message number in the expected number field. |
| Header / Validate message header | Select this check box to test that the correct message header is received on each endpoint. |
| Header / Use File | This option appears when the Validate message header check box is selected. Select this option to specify the expected message header from a file and type in the name and path of the file between double quotes in the File name field. |
| Header / Use Inline Table | This option appears when the Validate message header check box is selected. Select this option to specify the expected message header from the table. Add as many rows as needed and enter the name and value of the header in the table. |
| Body / Validate message bodies | Select this check box to test that the correct message bodies are received on each endpoint. |
| Body / Use File | This option appears when the Validate message bodies check box is selected. Select this option to specify the expected message bodies from a file and type in the name and path of the file between double quotes in the File name field. |
| Body / Use Inline Table | This option appears when the Validate message bodies check box is selected. Select this option to specify the expected message bodies from the table. Add as many rows as needed and enter the message bodies in the table. |
| Simulate | This option appears when the cMock is used as a message producer. Select this check box to simulate the message generation, and select the cProcessor component to produce the message in the Use existing cProcessor list. |
| Wait time (in millis) | This option appears when the cMock is used to check the test output result. Specify the time in milliseconds that the cMock waits for the result to come. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cMock can be a start, middle or end component in a Route. |
| Limitation | The cMock component is designed for testing Routes. It is not recommended to use the cMock in message routing. When you add cMock to a Route, each exchange sent to it will be stored (to allow for later validation) in memory until explicitly reset or the JVM is restarted. If you are sending high volume and/or large messages, this may cause excessive memory use. For more information about how to test Routes, see [Testing Routes using test cases](/talend/r/en-US/8.0/studio-user-guide/testing-routes-using-test-cases). |
