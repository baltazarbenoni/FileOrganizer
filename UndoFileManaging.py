from pathlib import Path
import shutil
import os

class FileType:
    def __init__(self, int, names, destination):
        self.int = int
        self.names = names
        self.destination = destination

class Main:

    h = Path.home()
    destination = Path(h / "Downloads")

#TARGET DIRECTORIES
    source = Path(h / "Desktop" / "FileManager" /"OrganizedDownloads") 
    srcAudio = Path(source / "Audio")
    srcText = Path(source / "Text")
    srcImages = Path(source / "Images")
    srcPrograms = Path(source / "Programs")
    srcMisc = Path(source / "Misc")
    sources = [srcAudio, srcText, srcImages, srcPrograms, srcMisc]

    def returnFiles(self, source):
        contents = os.listdir(source)
        if(contents.count == 0):
            print("The folder is empty! Folder: " + source)
            return
        else:
            for x in contents:
                filePath = Path(source / x)
                #CHECK IF ITEM IS A FILE, IF NOT, PASS ON.
                if (os.path.isfile(filePath) == False):
                    print("Item " + x + "with path " + source + " is not a file. It will not be moved.")
                else:
                    shutil.move(filePath, self.destination)
                    print("Item has been moved: " + x)

    def unorganize(self):
        for x in self.sources:
            self.returnFiles(x)


key = input("Type \'y\' if you want to return files to Downloads. Press any other key to quit.\n\n") 
if(key == "y"):
    instance = Main()
    instance.unorganize()
    print("Files returned to Downloads!\n")
else:
    print("Okay, see you another time.\n")


 
