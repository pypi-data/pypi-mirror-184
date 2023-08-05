import re


def hasMajorVersionUpdate(currentVersion: str, nextVersion: str):
    hasMajorVersionUpdate = False
    currentMajorVersion = getMajorVersionNumber(currentVersion)
    nextMajorVersion = getMajorVersionNumber(nextVersion)

    if nextMajorVersion != currentMajorVersion:
        hasMajorVersionUpdate = True

    return hasMajorVersionUpdate


def getMajorVersionNumber(version: str):
    match = re.search("\\d+\\.\\d+\\.\\d+", version)
    versionNumber = ""
    majorVersion = ""
    if match:
        versionNumber = match.group(0)

    match = re.search("\\d+", versionNumber)
    if match:
        majorVersion = match.group(0)

    return majorVersion
