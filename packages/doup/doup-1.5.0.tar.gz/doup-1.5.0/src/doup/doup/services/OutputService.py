import os

from termcolor import colored

from doup.analyzer import DockertagAnalyzer


def notifyUser(dockerImage, nextVersion: str, dry_run: bool):
    printSeperator()
    printFilename(dockerImage.filename)
    printTag(
        dockerImage.namespace + "/" + dockerImage.repository + "/" + dockerImage.tag
    )
    printCurrentVersion(dockerImage.version)
    printNextVersion(dockerImage.version, nextVersion, dry_run)
    printMajorVersionWarning(dockerImage.version, nextVersion)


def printSeperator():
    print(
        "-----------------------------------------------------------------------------"
    )


def printFilename(filename: str):
    print("file: " + os.path.relpath(filename))


def printTag(tag: str):
    print("tag: " + colored(tag, "yellow"))


def printCurrentVersion(version: str):
    print("current: " + colored(version, "green"))


def printNextVersion(version: str, nextVersion: str, dry_run: bool):
    dry_run_suffix = " (dry run)" if dry_run else ""
    color = "red"
    if nextVersion == version:
        color = "green"

    print("next: " + colored(nextVersion + dry_run_suffix, color))


def printMajorVersionWarning(currentVersion: str, nextVersion: str):
    notification = "!!! MAJOR VERSION UPDATE DETECTED !!!"
    if nextVersion != currentVersion:
        majorUpdateNotification = DockertagAnalyzer.hasMajorVersionUpdate(
            currentVersion, nextVersion
        )
        if majorUpdateNotification:
            print(colored(notification, "red"))
