import json

import requests

from doup import DockerImage
from doup.analyzer import StringAnalyzer


# ----------------------------------------------------------------------------
# https://github.com/docker/hub-feedback/issues/1253
class DockerVersionUpdater:

    dry_run = False
    only_updates = False

    def __init__(self, dry_run: bool, only_updates: bool):
        self.dry_run = dry_run
        self.only_updates = only_updates

    def updateDockerVersion(self, dockerImage: DockerImage.DockerImage):
        digest = self.getTagDigest(dockerImage, "amd64")
        tags = self.getTagsToDigest(dockerImage, digest)
        nextVersion = self.getLatestVersion(dockerImage, tags)

        dockerImage.update(nextVersion, self.dry_run, self.only_updates)

    def getTagDigest(self, dockerImage: DockerImage.DockerImage, architecture: str):
        url = (
            "https://hub.docker.com/v2/repositories/"
            + dockerImage.namespace
            + "/"
            + dockerImage.repository
            + "/tags/"
            + dockerImage.tag
        )

        response = requests.get(url)
        bar = json.loads(response.text)
        images = bar["images"]

        digest = ""
        for image in images:
            if image["architecture"] == architecture:
                digest = image["digest"]

        return digest

    def getTagsToDigest(self, dockerImage: DockerImage.DockerImage, digest: str):
        url = (
            "https://hub.docker.com/v2/repositories/"
            + dockerImage.namespace
            + "/"
            + dockerImage.repository
            + "/tags/?page_size=1000"
        )

        response = json.loads(requests.get(url).text)
        tags = []
        for result in response["results"]:
            for image in result["images"]:
                if image["digest"] == digest:
                    tags.append(result["name"])
        return tags

    def getLatestVersion(self, dockerImage, tags: list):
        tagsToRemove = []
        for tag in tags:
            if not StringAnalyzer.hasNumbers(tag):
                tagsToRemove.append(tag)

        for tag in tagsToRemove:
            tags.remove(tag)

        latestVersion = StringAnalyzer.getLongest(tags)
        return latestVersion
