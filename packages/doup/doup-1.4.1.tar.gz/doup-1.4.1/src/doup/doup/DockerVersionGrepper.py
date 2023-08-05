import glob
import re

from doup import DockerImage
from doup.analyzer import StringAnalyzer


class DockerVersionGrepper:
    path = ""
    groupToUpdate = None

    def __init__(self, path: str, groupToUpdate: str):
        self.path = path
        self.groupToUpdate = groupToUpdate

    def getDockerImagesInPath(self):
        files = glob.iglob(self.path + "/**/*", recursive=True)
        dockerImages = []
        for file in files:
            dockerImages.extend(self.getDockerImagesInFile(file))

        return dockerImages

    def getDockerImagesInFile(self, filepath: str):
        dockerImages = []

        try:
            with open(filepath, "r") as currentFile:
                previousLine = ""
                for line in currentFile:
                    dockerImage = self.getDockerImage(filepath, line, previousLine)
                    previousLine = line

                    if dockerImage:
                        dockerImages.append(dockerImage)
        except UnicodeDecodeError:
            pass
        except IsADirectoryError:
            pass

        return dockerImages

    def getDockerImage(self, filepath: str, line: str, previousLine: str):
        version = self.getVersionString(line)
        tag = self.getDockerImagetag(previousLine)
        group = self.getGroup(previousLine)
        isPartOfGroup = not self.groupToUpdate or (
            self.groupToUpdate and self.groupToUpdate == group
        )

        if version and tag and isPartOfGroup:
            return DockerImage.DockerImage(version, tag, group, filepath)

        return None

    def getVersionString(self, string: str):
        pattern = "\\s[\\w\\-]+[/\\w\\-]+:[\\w\\-\\.]+$"
        isMatch = re.search(pattern, string)
        version = ""

        if isMatch:
            matchGroup = isMatch.group()
            if self.isValidDockerImage(matchGroup):
                version = matchGroup

        return version

    def isValidDockerImage(self, matchGroup: str):
        containsLetters = StringAnalyzer.hasLetters(matchGroup)
        containsNumbers = StringAnalyzer.hasNumbers(matchGroup)

        if containsNumbers and containsLetters and len(matchGroup) < 60:
            return True

        return False

    def getDockerImagetag(self, line: str):
        pattern = "doup:.*"
        isMatch = re.search(pattern, line)
        tag = ""

        if isMatch:
            tag = isMatch.group().split(":")[1]

        return tag

    def getGroup(self, line: str):
        pattern = "doup:.*"
        isMatch = re.search(pattern, line)
        group = ""

        if isMatch:
            groups = isMatch.group().split(":")
            if len(groups) == 3:
                group = groups[2]

        return group
