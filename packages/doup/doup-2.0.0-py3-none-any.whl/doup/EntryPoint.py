import argparse

from doup.crawler import DirectoryCrawler, DockerhubCrawler
from doup.dto.DirectorySummary import DirectorySummary
from doup.services import FileService, OutputService


def getArgs():
    parser = argparse.ArgumentParser(
        prog="doup",
        description="a tool to find and update marked dockertags in project files.",
    )
    parser.add_argument("path", type=str, help="search for dockertags in this path")
    parser.add_argument(
        "-d",
        "--dry-run",
        action="store_true",
        help="show the status of dockertags but dont update files",
    )

    parser.add_argument(
        "-s",
        "--show-all",
        action="store_true",
        help="show all dockertags even when no new version is published",
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
