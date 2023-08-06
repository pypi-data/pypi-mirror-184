import argparse
import os

from doup.crawler import DirectoryCrawler, DockerhubCrawler
from doup.dto.DirectorySummary import DirectorySummary
from doup.services import FileService, OutputService


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

    directorySummary: DirectorySummary = DirectoryCrawler.getImageNamesInPath(path)
    for dockerImage in directorySummary.dockerImages:
        nextTag = DockerhubCrawler.getLatestTag(
            dockerImage.repository, dockerImage.tagToFollow, "amd64"
        )

        if nextTag == dockerImage.currentTag and show_all:
            OutputService.notifyUser(dockerImage, nextTag, dry_run)

        if nextTag != dockerImage.currentTag:
            OutputService.notifyUser(dockerImage, nextTag, dry_run)
            if not dry_run:
                nextImageName = dockerImage.getNextImageName(nextTag)
                FileService.replaceString(
                    dockerImage.filename, dockerImage.imageName, nextImageName
                )

    OutputService.printSummary(directorySummary)
