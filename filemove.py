import os, time, shutil
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensetive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensetive)

endings = ["txt", "pdf", "mp3", "exe", "zip"]
newFolder = [r"\Txt Folder", r"\pdf Folder", r"\mp3 Folder", r"\exe Folder", r"\zip Folder"]


filelist = os.listdir("E:/Chrome Downloads/")
for x in range(len(filelist)):
    for i in range(len(endings)):
        if filelist[x].endswith(endings[i]):
            newpath = r"E:/Chrome Downloads/" + newFolder[i]
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            shutil.move(str("E:/Chrome Downloads/" + filelist[x]), str(newpath + str(filelist[x])))


def on_created(event): #prints the Name/Path of the new File and creates a Folder for it if it doesn't yet exist
    print(f"Hey, {event.src_path} has been created!")
    time.sleep(3)
    basename = os.path.basename(str(event.src_path))
    for i in range(len(endings)):
        if str(event.src_path).endswith(endings[i]):
            newpath = r"E:\Chrome Downloads" + newFolder[i]
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            shutil.move(str(event.src_path), str(newpath + "/" + basename))

my_event_handler.on_created = on_created

path = "E:\Chrome Downloads"
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler,path,recursive = go_recursively)

my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()



