import time
from os import mkdir


class FileSystem:
    def timeStampDir(self):
        return time.time()

    def getTimeStamp(self):
        return time.time()

    def create_directory(self, dir):
        return mkdir(str(dir), 0o777)
