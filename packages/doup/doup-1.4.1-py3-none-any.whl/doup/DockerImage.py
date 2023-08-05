import os

from termcolor import colored

from doup.analyzer import VersionAnalyzer


def getVersion(versionString: str):
    return versionString.split(":")[1].strip()


def getNamespace(versionString: str):
    namespaceAndRepo = versionString.split(":")[0].split("/")
    namespace = ""

    if len(namespaceAndRepo) == 2:
        namespace = namespaceAndRepo[0]
    else:
        namespace = "library"

    return namespace.strip()


def getRepository(versionString: str):
    namespaceAndRepo = versionString.split(":")[0].split("/")
    repo = ""

    if len(namespaceAndRepo) == 2:
        repo = namespaceAndRepo[1]
    else:
        repo = namespaceAndRepo[0]

    return repo.strip()


# ----------------------------------------------------------------------------


class DockerImage:
    versionString = ""
    filename = ""
    tag = ""
    group = ""

    namespace = ""
    repository = ""
    version = ""

    def __init__(self, versionString: str, tag: str, group: str, filename: str):
        self.versionString = versionString.strip()
        self.filename = filename
        self.tag = tag
        self.group = group

        self.namespace = getNamespace(versionString)
        self.version = getVersion(versionString)
        self.repository = getRepository(versionString)

    def getVersionString(self, newVersion: str):
        versionString = ""

        if self.namespace == "library":
            versionString = self.repository + ":" + newVersion
        else:
            versionString = self.namespace + "/" + self.repository + ":" + newVersion

        return versionString

    def update(self, nextVersion: str, dry_run: bool, only_updates: bool):
        if nextVersion == self.version and not only_updates:
            self.printStatus(nextVersion, dry_run, only_updates)

        if nextVersion != self.version:
            self.printStatus(nextVersion, dry_run, only_updates)
            if not dry_run:
                file = open(self.filename, "rt")
                data = file.read()
                data = data.replace(
                    self.versionString, self.getVersionString(nextVersion)
                )
                file.close()

                file = open(self.filename, "wt")
                file.write(data)
                file.close()

    def printStatus(self, nextVersion, only_updates, dry_run):
        self.printSeperator()
        self.printFilename()
        self.printTag()
        self.printCurrentVersion()
        self.printNextVersion(nextVersion, dry_run)
        self.printMajorVersionWarning(nextVersion)

    def printSeperator(self):
        print(
            "-----------------------------------------------------------------------------"
        )

    def printFilename(self):
        print("file: " + os.path.relpath(self.filename))

    def printTag(self):
        tag = self.namespace + "/" + self.repository + ":" + self.tag
        print("tag: " + colored(tag, "yellow"))

    def printCurrentVersion(self):
        print("current: " + colored(self.version, "green"))

    def printNextVersion(self, nextVersion: str, dry_run: bool):
        dry_run_suffix = " (dry run)" if dry_run else ""
        color = "red"
        if nextVersion == self.version:
            color = "green"

        print("next: " + colored(nextVersion + dry_run_suffix, color))

    def printMajorVersionWarning(self, nextVersion: str):
        notification = "!!! MAJOR VERSION UPDATE DETECTED !!!"
        if nextVersion != self.version:
            majorUpdateNotification = VersionAnalyzer.hasMajorVersionUpdate(
                self.version, nextVersion
            )
            if majorUpdateNotification:
                print(colored(notification, "red"))
