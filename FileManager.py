from pathlib import Path
import shutil
import os
import re
from enum import Enum

class FileType:
    def __init__(self, int, names, destination):
        self.int = int
        self.names = names
        self.destination = destination

class Main:

#DOWNLOADS FOLDER ORGANIZING
#ENUMS FOR FILE TYPES
    class Type(Enum):
        AUDIO = 0
        IMAGE = 1
        TEXT = 2
        PROGRAM = 3
        MISC = 4

    h = Path.home()
    source = Path(h / "Downloads")

#TARGET DIRECTORIES
    destination = Path(h / "Desktop" / "FileManager" /"OrganizedDownloads") 
    destAudio = Path(destination / "Audio")
    destText = Path(destination / "Text")
    destImages = Path(destination / "Images")
    destPrograms = Path(destination / "Programs")
    destMisc = Path(destination / "Misc")

#FILE ENDINGS TO LOOK FOR
    audiotypes = ["wav", "mp3"]
    imagetypes = ["png", "jpg"]
    programs = "exe"
    texttypes = ["txt", "docx", "odt", "pdf"]

#CREATE INSTANCES OF FILE TYPE OBJETS
    audioFile = FileType(Type.AUDIO, audiotypes, destAudio)
    imageFile = FileType(Type.IMAGE, imagetypes, destImages)
    textFile = FileType(Type.TEXT, texttypes, destText)
    programs = FileType(Type.PROGRAM, programs, destPrograms)
    misc = FileType(Type.MISC, "", destMisc)

#ADD ALL INSTANCES TO AN ARRAY.
    fileTypes = [audioFile, imageFile, textFile, programs, misc]

#FUNCTION TO GET CONTENTS OF THE SPECIFIED FOLDER AND GO THROUGH THE FILES.
    def organizefiles(self):
        contents = os.listdir(self.source)
        print(contents)
        if(contents.count == 0):
            print("The folder is empty!")
            return
        else:
            for x in contents:
                #CHECK IF ITEM IS A FILE, IF NOT, PASS ON.
                if (os.path.isfile(Path(self.source / x)) == False):
                    print("Item " + x + " is not a file. It will not be moved.")
                    continue
                #CHECK THE FILE TYPE AND MOVE IT ACCORDINGLY
                print("Moving file : " + x)
                self.checkFile(x)
            print("\'Downloads\' is now organized!")
    
    def checkFile(self, item):
        #CHECK EACH FILETYPE AGAINST THIS ITEM
        for ftype in self.fileTypes:

            #CHECK EACH POSSIBLE NAME ENDING OF THE FILE TYPE AGAINST THIS ITEM.
            names = ftype.names
            for x in names:
                regex = "(" + x + ")$"
                result = re.search(regex, item)

                #IF FOUND, MOVE FILE 
                if(result != None):

                    #CHECK THERE IS NO DUPLICATE IN THE DESTINATION
                    path = Path(ftype.destination / item)
                    if(path.exists()):
                        #os.remove(path)
                        print("cant move file " + item)
                        continue
                    
                    #CHECK THE FILE TO MOVE EXISTS 
                    file_to_move = Path(self.source / item)
                    if(file_to_move.exists() == False):
                        continue

                    #FILE EXISTS, NO CONFLICTS WITH DESTINATION --> MOVE FILE
                    self.moveFile(item, ftype.destination)
                    print(item + " has been moved")
                    return

        #TYPE NOT FOUND, MOVE TO MISC
        self.moveFile(item, self.misc.destination)

    def moveFile(self, item, destination):
        shutil.move(Path( self.source / item), destination)

#INIT APP
print("Welcome to your file manager!")
instance = Main()
key = input("Type \'or\' to organize the \'Downloads\'-folder.\n\n")
if(key == 'or'):
    instance.organizefiles()



