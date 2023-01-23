class FileSystem:
    def CurrentDirectory(filename: str) -> str:
        filename = filename.strip("\\")
        for i in range(-1, -len(filename), -1):
            if filename[i] == "\\":
                return filename[:i] + "\\"
        raise Exception("No directory found")