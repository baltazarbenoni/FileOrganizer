from pathlib import Path
import shutil
import zipfile
import os.path
import zlib

class Main:

#INITIALIZE PROGRAM
    intro = "Welcome to your file manager! What would you like to do?"
    instructions = "If you want the program to go through the \'Downloads\'-folder and organize the files, type \'or\'. If you want to zip some file, just write the file path."

#GET THE ACTIONS THE USER WANTS TO ACCOMPLISH
    def getMode(self): 
        mode = input("Enter the mode you wish to use. Write \'ins\' for instructions")

        if(mode == "ins"):
            print(self.instructions)
        elif(mode == "or"):
            Downloads.organizefiles()
        else:
            Zipper.operate(mode)

#INIT APP
    print(intro)
    getMode()

class Downloads:

    h = Path.home()

    source = Path(h / "Downloads")

    destination = Path(h / "OrganizedDownloads") 
    destAudio = Path(destination / "Audio")
    destText = Path(destination / "Text")
    destImages = Path(destination / "Images")
    destPrograms = Path(destination / "Programs")
    destMisc = Path(destination / "Misc")

    audiotypes = "wav", "mp3", "acc"
    imagetypes = "png, jpg"
    programs = "exe"
    texttypes = "txt", "docx", "odt", "pdf"

    def organizefiles(self):
        contents = os.listdir(self.source)
        print(contents)

    def getFileType(self):
        return 1

    def assignLocation(self):

        if(self.getFileType() == 1):
            self.move(self.destAudio)

class Zipper:

#RUN ZIP OPERATIONS
    def operate(self, file):
        file = Path(file)
        if(self.checkfile(file) == True):
            self.assignFile(file)
        else:
            Main.getMode()
            return
#CHECK FILE
    def checkfile(file):
        return file.exists and os.path.isfile(file)

#FIND OUT IF FILE IS ALREADY ZIP. IF YES, UNPACK, OTHERWISE PACK
    def assignFile(self, file):
        iszip = zipfile.is_zipfile(file)
        if(iszip):
            self.extract(file)
        else:
            self.pack(file)
    
#FUNCTIONS TO EXECUTE BASED ON FILE TYPE
    def pack(file): 
        home = Path.home()
        filepath = Path(file)
        ziplocation = Path(home / "Desktop/ZippedFiles")

        if(ziplocation.exists() == False):
            Path(ziplocation).mkdir
        
        ending = ".zip"
        zipname = file + ending 

        zip = zipfile.ZipFile(zipname, "w", zipfile.ZIP_DEFLATED)
        zip.write(file)
        shutil.move(Path(filepath.parent / zip.filename), ziplocation)

    def extract(file):
        zip = zipfile.ZipFile(file, "r") 
        zip.extractall(Path.home())


