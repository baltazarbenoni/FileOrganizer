from pathlib import Path
import shutil
import zipfile
import os
import zlib


class Main:

#INITIALIZE PROGRAM
#
#ACTIVATE ORGANIZER
    activation = False
    def activation(self):
        self.activation = not self.activation

#GET THE ACTIONS THE USER WANTS TO ACCOMPLISH
    def getMode(self):

        clear = lambda: os.system('cls') 
        instructions = "If you want the program to go through the \'Downloads\'-folder and organize the files, type \'or\'. If you want to zip some file, just write the file path.\n"
        mode = input("Enter the mode you wish to use. Write \'ins\' for instructions\n")

        if(mode == "ins"):
            clear()
            print(instructions)
            self.getMode()
        elif(mode == "or"):
            clear()
            self.organizefiles()
        else:
            clear()
            self.operate(mode)

#DOWNLOADS FOLDER ORGANIZING

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

#RUN ZIP OPERATIONS
    def operate(self, file):
        path = Path(file)
        a = self.checkfile(path)

        if(a):
            self.assignFile(file)
        else:
            print("File not valid! Try again!")
            self.getMode()
            return
#CHECK FILE
    def checkfile(self, file):
        path = Path(file)
        a = file.exists
        #b = os.path.isfile(path)
        b = True
        print("Object exists: ")
        print(a)
        print("Object is file: ")
        print(b)
        return a and b 


#FIND OUT IF FILE IS ALREADY ZIP. IF YES, UNPACK, OTHERWISE PACK
    def assignFile(self, file):
        iszip = zipfile.is_zipfile(file)
        if(iszip):
            self.extract(file)
        else:
            self.pack(file)
    
#FUNCTIONS TO EXECUTE BASED ON FILE TYPE
    def pack(self, file): 
        home = Path.home()
        filepath = Path(file)
        ziplocation = Path(home / "Desktop/ZippedFiles")

        if(ziplocation.exists() == False):
            Path(ziplocation).mkdir
        
        ending = "z"
        zipname = Path(file)
        #zipname = file + ending 

        zip = zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED)
        zip.write(file, arcname=file)
        shutil.move(Path(filepath.parent / zip.filename), ziplocation)

    def extract(self, file):
        zip = zipfile.ZipFile(file, "r") 
        zip.extractall(Path.home())

#INIT APP
print("Welcome to your file manager!")
print("")
print("What would you like to do?")
instance = Main()
instance.getMode()


