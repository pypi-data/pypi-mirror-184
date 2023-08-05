import argparse
import os

from doup.analyzer import DockertagAnalyzer
from doup.crawler import DirectoryCrawler, DockerhubCrawler


def getArgs():
    currentPath = os.getcwd()
    parser = argparse.ArgumentParser(
        description="doup is a tool to find and update Docker-Image-Strings in project files."
    )
    parser.add_argument(
        "-p",
        "--path",
        type=str,
        default=currentPath,
        help="search for Docker-Image-Strings in a specific path",
    )
    parser.add_argument(
        "-d",
        "--dry-run",
        action="store_true",
        help="print the Docker-Image-Strings but dont update any files",
    )

    parser.add_argument(
        "-s",
        "--show-all",
        action="store_true",
        help="show all Docker-Image-Strings, even when no new version is published",
    )

    args = parser.parse_args()

    return args


# -----------------------------------------------------------------------------


def main():
    args = getArgs()

    path = args.path
    dry_run = args.dry_run
    show_all = args.show_all

    dockerImages = DirectoryCrawler.getDockerImagesInPath(path)
    for dockerImage in dockerImages:
        digest = DockerhubCrawler.getDigestOfTag(dockerImage, "amd64")
        allTagsToDigest = DockerhubCrawler.getAllTagsToDigest(dockerImage, digest)
        nextVersion = DockertagAnalyzer.getLongestTag(allTagsToDigest)

        dockerImage.update(nextVersion, dry_run, show_all)
