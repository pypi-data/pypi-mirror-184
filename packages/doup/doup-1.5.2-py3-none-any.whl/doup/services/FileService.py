def replaceString(filename: str, oldValue: str, newValue: str) -> bool:
    file = open(filename, "rt")
    data = file.read()
    data = data.replace(oldValue, newValue)
    file.close()

    file = open(filename, "wt")
    file.write(data)
    file.close()

    return True
