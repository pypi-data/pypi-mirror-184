from doup.analyzer import ImageNameAnalyzer


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

    def getNextImageName(self, nextTag) -> str:
        return self.repository + ":" + nextTag
