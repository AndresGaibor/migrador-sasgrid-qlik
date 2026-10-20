<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/maprstreams/tmaprstreamscommit · versión 8.0 -->
# tMapRStreamsCommit

Last updated: 9/30/2026

Connects to a given tMapRStreamsInput to
perform a consumer offset commit.

tMapRStreamsCommit saves the current state of the
tMapRStreamsInput to which it is connected.Note
that the term 'commit' in this component means saving what messages are consumed by this
tMapRStreamsInput component at the moment of
committing.

## tMapRStreamsCommit Standard properties

These properties are used to configure tMapRStreamsCommit running in the Standard Job framework.

The Standard
tMapRStreamsCommit component belongs to the Internet family.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Commit offsets from | Select the tMapRStreamsInput component from which the consumed messages are committed. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to gather the processing metadata at the Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | Although tMapRStreamsCommit can be used as an end component in a subJob flow or can be called independently as its own subJob, it is typically used standalone to commit a batch of offsets in one go. If you need to commit offsets regularly, it is recommended to use the Auto-commit feature in tMapRStreamsInput. |
