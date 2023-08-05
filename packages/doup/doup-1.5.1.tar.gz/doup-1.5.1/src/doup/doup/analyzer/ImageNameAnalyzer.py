def getNamespace(imageName: str):
    namespaceAndRepo = imageName.split(":")[0].split("/")
    namespace = ""

    if len(namespaceAndRepo) == 2:
        namespace = namespaceAndRepo[0]
    else:
        namespace = "library"

    return namespace.strip()


def getRepository(imageName: str) -> str:
    stringArray = imageName.split(":")[0].split("/")

    if len(stringArray) == 2:
        repository = stringArray[0] + "/" + stringArray[1]
    else:
        repository = "library/" + stringArray[0]

    return repository.strip()


def getTag(imageName: str) -> str:
    return imageName.split(":")[1].strip()
