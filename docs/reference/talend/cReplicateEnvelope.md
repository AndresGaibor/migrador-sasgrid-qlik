<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-qlik-replicate/creplicateenvelope · versión 8.0 -->
# cReplicateEnvelope

Last updated: 9/30/2026

Decode messages created by [Qlik Replicate](https://help.qlik.com/en-US/replicate/).

## cReplicateEnvelope Standard properties

These properties are used to configure cReplicateEnvelope running in
the Standard Route framework.

The Standard
cReplicateEnvelope component belongs to the Connectivity family.

## Basic settings

| Metadata Storage Key | Enter the ID of the metadata storage object. |
| Use Custom Metadata Storage Class | Specify your own implementation of metadata storage as needed. |
| Metadata Receive Timeout (ms) | Specify the timeout in milliseconds that the cReplicateEnvelope component keeps waiting for the metadata messages if data messages arrives before metadata. |
| Skip Metadata Messages | Select this check box to skip metadata messages if you want to process data messages only. |
| Skip Data Messages | Select this check box to skip data messages if you want to process metadata messages only. |

## Usage

| **Usage rule** | cReplicateEnvelope is used as a middle or end component in a Route. |
| Limitation | n/a |
