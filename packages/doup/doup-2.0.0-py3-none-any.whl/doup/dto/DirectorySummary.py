from doup.dto.DockerImage import DockerImage


class DirectorySummary:
    dockerImages: list[DockerImage] = []
    numberOfFiles: int

    def __init__(self, dockerImages: list[DockerImage], numberOfFiles: int):
        self.dockerImages = dockerImages
        self.numberOfFiles = numberOfFiles
