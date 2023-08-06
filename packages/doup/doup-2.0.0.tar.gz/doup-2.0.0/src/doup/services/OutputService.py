import os

from termcolor import colored

from doup.analyzer import TagAnalyzer
from doup.dto.DirectorySummary import DirectorySummary


def printSummary(directorySummary: DirectorySummary):
    print("")
    print("Finished!")
    print(
        "Searched in "
        + colored(str(directorySummary.numberOfFiles), "yellow")
        + " files and found "
        + colored(str(len(directorySummary.dockerImages)), "yellow")
        + " managed docker images"
    )


def notifyUser(dockerImage, nextTag: str, dry_run: bool):
    printSeperator()
    printFilename(dockerImage.filename)
    printTag(dockerImage.repository + "/" + dockerImage.tagToFollow)
    printCurrentTag(dockerImage.currentTag)
    printNextTag(dockerImage.currentTag, nextTag, dry_run)
    printMajorVersionWarning(dockerImage.currentTag, nextTag)


def printSeperator():
    print(
        "-----------------------------------------------------------------------------"
    )


def printFilename(filename: str):
    print("file: " + os.path.relpath(filename))


def printTag(tag: str):
    print("tag: " + colored(tag, "yellow"))


def printCurrentTag(currentTag: str):
    print("current: " + colored(currentTag, "green"))


def printNextTag(currentTag: str, nextTag: str, dry_run: bool):
    dry_run_suffix = " (dry run)" if dry_run else ""
    color = "red"
    if nextTag == currentTag:
        color = "green"
        dry_run_suffix = ""

    print("next: " + colored(nextTag + dry_run_suffix, color))


def printMajorVersionWarning(currentTag: str, nextTag: str):
    notification = "!!! MAJOR VERSION UPDATE DETECTED !!!"
    if nextTag != currentTag:
        majorUpdateNotification = TagAnalyzer.hasMajorVersionUpdate(currentTag, nextTag)
        if majorUpdateNotification:
            print(colored(notification, "red"))
