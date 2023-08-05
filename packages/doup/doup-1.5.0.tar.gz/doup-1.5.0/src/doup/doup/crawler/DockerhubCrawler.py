import json

import requests

from doup.DockerImage import DockerImage


def getDigestOfTag(dockerImage: DockerImage, architecture: str):
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


def getAllTagsToDigest(dockerImage: DockerImage, digest: str):
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
