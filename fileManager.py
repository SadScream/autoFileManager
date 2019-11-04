from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime
import os
import time


class Event(FileSystemEventHandler):
	def on_modified(self, event):
		for filename in os.listdir(trackingFolder):
			detectingFolders()
			default = os.path.join(trackingFolder, filename)
			new = default
			exists = False

			if any(_ in filename.split('.')[-1] for _ in extensionList["images"]):
				i = 0

				if filename not in os.listdir(destinations[i]):
					new = os.path.join(destinations[i], str(filename))
				else:
					exists = True
					new = processingFile(filename, destinations[i])

			elif any(_ in filename.split('.')[-1] for _ in extensionList["documents"]):
				i = 1

				if filename not in os.listdir(destinations[i]):
					new = os.path.join(destinations[i], filename)
				else:
					exists = True
					new = processingFile(filename, destinations[i])

			elif any(_ in filename.split('.')[-1] for _ in extensionList["audios"]):
				i = 2

				if filename not in os.listdir(destinations[i]):
					new = os.path.join(destinations[i], filename)
				else:
					exists = True
					new = processingFile(filename, destinations[i])

			elif any(_ in filename.split('.')[-1] for _ in extensionList["videos"]):
				i = 3

				if filename not in os.listdir(destinations[i]):
					new = os.path.join(destinations[i], filename)
				else:
					exists = True
					new = processingFile(filename, destinations[i])

			else:
				continue

			if new != default:
				if not exists:
					print(f"\nMOVING\n{default}\tto\t{new}")
				else:
					print(f"\nFILE EXISTS\n{default}\trenamed to\t{os.path.basename(new)}")
				os.rename(default, new)


def processingFile(filename, destination):
	filesList = [_ for _ in os.listdir(destination) if filename == _]

	pickedFileName = '.'.join(filename.split('.')[:-1])
	fileDigit = str(len(filesList))
	fileExtension = filename.split('.')[-1]

	fileName = f"{pickedFileName}_{fileDigit}.{fileExtension}"

	return os.path.join(destination, fileName)


def detectingFolders():
	for folder in folders:
		if not os.path.exists(os.path.join(disk, folder)):
			print(f"{os.path.join(disk, folder)} doesn't exist, creating..")
			os.makedirs(os.path.join(disk, folder))


trackingFolder = "D:\\Downloaded"
disk = "D:\\"
folders = ["_Pictures", "_Documents", "_Audios", "_Videos"] # order must to match with extensionList keys

extensionList = {
	"images": ['jpg', 'bmp', 'png', 'jpeg', 'gif'],
	"documents": ['docx', 'doc', 'pptx', 'pdf'],
	"audios": ['ogg', 'mp3'],
	"videos": ['mp4']
}


detectingFolders()


destinations = [os.path.join(disk, _) for _ in folders]

if __name__ == '__main__':
	event = Event()
	observer = Observer()
	observer.schedule(event, trackingFolder, recursive=True)
	observer.start()
	print(f"STARTED {datetime.now().strftime('%d-%m-%Y %H:%M')}")

	try:
		while True:
			time.sleep(10)
	except KeyboardInterrupt:
		observer.stop()

	observer.join()