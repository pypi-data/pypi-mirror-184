import glob
import re

from doup import DockerImage
from doup.analyzer import StringAnalyzer


def getDockerImagesInPath(path: str):
    files = glob.iglob(path + "/**/*", recursive=True)
    dockerImages = []
    for file in files:
        dockerImages.extend(getDockerImagesInFile(file))

    return dockerImages


def getDockerImagesInFile(filepath: str):
    dockerImages = []

    try:
        with open(filepath, "r") as currentFile:
            previousLine = ""
            for line in currentFile:
                dockerImage = getDockerImage(filepath, line, previousLine)
                previousLine = line

                if dockerImage:
                    dockerImages.append(dockerImage)
    except UnicodeDecodeError:
        pass
    except IsADirectoryError:
        pass

    return dockerImages


def getDockerImage(filepath: str, line: str, previousLine: str):
    version = getVersionString(line)
    tag = getDockerImagetag(previousLine)

    if version and tag:
        return DockerImage.DockerImage(version, tag, filepath)

    return None


def getVersionString(string: str):
    pattern = "\\s[\\w\\-]+[/\\w\\-]+:[\\w\\-\\.]+$"
    isMatch = re.search(pattern, string)
    version = ""

    if isMatch:
        matchGroup = isMatch.group()
        if isValidDockerImage(matchGroup):
            version = matchGroup

    return version


def isValidDockerImage(matchGroup: str):
    containsLetters = StringAnalyzer.hasLetters(matchGroup)
    containsNumbers = StringAnalyzer.hasNumbers(matchGroup)

    if containsNumbers and containsLetters and len(matchGroup) < 60:
        return True

    return False


def getDockerImagetag(line: str):
    pattern = "doup:.*"
    isMatch = re.search(pattern, line)
    tag = ""

    if isMatch:
        tag = isMatch.group().split(":")[1]

    return tag
