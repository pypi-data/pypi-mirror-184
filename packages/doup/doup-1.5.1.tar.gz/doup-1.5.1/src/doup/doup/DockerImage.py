from doup.analyzer import ImageNameAnalyzer
from doup.services import OutputService


class DockerImage:
    imageName = ""
    tagToFollow = ""
    repository = ""
    filename = ""
    currentTag = ""

    def __init__(self, imageName: str, tagToFollow: str, filename: str):
        self.imageName = imageName.strip()
        self.tagToFollow = tagToFollow
        self.filename = filename

        self.repository = ImageNameAnalyzer.getRepository(imageName)
        self.currentTag = ImageNameAnalyzer.getTag(imageName)

    def update(self, nextTag: str, dry_run: bool, show_all: bool):
        if nextTag == self.currentTag and show_all:
            OutputService.notifyUser(self, nextTag, dry_run)

        if nextTag != self.currentTag:
            OutputService.notifyUser(self, nextTag, dry_run)
            if not dry_run:
                file = open(self.filename, "rt")
                data = file.read()
                data = data.replace(self.imageName, self.getNextImageName(nextTag))
                file.close()

                file = open(self.filename, "wt")
                file.write(data)
                file.close()

    def getNextImageName(self, nextTag) -> str:
        return self.repository + ":" + nextTag
