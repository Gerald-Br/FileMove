import os, shutil

endings = ["txt", "pdf", "mp3", "exe", "zip", "7z"] #compatible file-types. Can be extended very easily
newFolder = [r"\Txt Folder", r"\pdf Folder", r"\mp3 Folder", r"\exe Folder", r"\zip Folder", "/7z Folder"]
filelist = os.listdir("E:/Chrome Downloads/") #Puts all of the Files in the Download Folder in a list.

while len(filelist) > 50:
    for x in range(len(filelist)):
        for i in range(len(endings)):
            if filelist[x].endswith(endings[i]):
                newpath = r"E:/Chrome Downloads/" + newFolder[i] #creates the new Path of the new Folder if it's not yet created
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                shutil.move(str("E:/Chrome Downloads/" + filelist[x]), str(newpath + "/" + str(filelist[x]))) #moves the File in the Downloads folder in the coresponding sub-Folder