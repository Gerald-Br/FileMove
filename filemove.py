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
newFolder = ["txt Folder", "pdf Folder", "mp3 Folder", "exe Folder", "zip Folder"]

def on_created(event): #prints the Name/Path of the new File and creates a Folder for it if it doesn't yet exist
    print(f"Hey, {event.src_path} has been created!")
    if str(event.src_path).endswith("txt"):
        newpath = r"E:\Chrome Downloads\Txt Files"
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        shutil.move(str(event.src_path), str(newpath +r"\Textdokument 1.txt"))

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


