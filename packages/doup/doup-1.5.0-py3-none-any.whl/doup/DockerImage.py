from doup.services import OutputService


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

    namespace = ""
    repository = ""
    version = ""

    def __init__(self, versionString: str, tag: str, filename: str):
        self.versionString = versionString.strip()
        self.filename = filename
        self.tag = tag

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

    def update(self, nextVersion: str, dry_run: bool, show_all: bool):
        if nextVersion == self.version and show_all:
            OutputService.notifyUser(self, nextVersion, dry_run)

        if nextVersion != self.version:
            OutputService.notifyUser(self, nextVersion, dry_run)
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
