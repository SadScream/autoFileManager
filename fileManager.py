from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime
from time import sleep
import os
import psutil


class Event(FileSystemEventHandler):

	def on_created(self, event):
		print(f"\nFILE CREATED\t")
		sleep(1)
		self.on_moved(event)

	def on_moved(self, event):
		for filename in os.listdir(trackingFolder):
			detectingFolders()
			default = os.path.join(trackingFolder, filename)
			new = default
			exists = False

			# for proc in psutil.process_iter():
			# 	try:
			# 		filesList = proc.open_files()
			# 		if filesList:
			# 			for nt in filesList:
			# 				if "_Pic" in nt.path:
			# 					print(proc.pid,proc.name())
			# 					print("\t",nt.path)
			# 	except psutil.NoSuchProcess:
			# 		pass
			# 	except psutil.AccessDenied:
			# 		pass
			# return

			if any(_ in filename.split('.')[-1] for _ in extensionList["images"]):
				position = 0
			elif any(_ in filename.split('.')[-1] for _ in extensionList["documents"]):
				position = 1
			elif any(_ in filename.split('.')[-1] for _ in extensionList["audios"]):
				position = 2
			elif any(_ in filename.split('.')[-1] for _ in extensionList["videos"]):
				position = 3
			else:
				continue

			if filename not in os.listdir(destinations[position]): # есть ли уже в папке файл с таким названием
				new = os.path.join(destinations[position], filename)
			else:
				exists = True
				new = processingFile(filename, destinations[position])

			if new != default:
				if not exists:
					print(f"\nMOVING\n{default}\tto\t{new}")
				else:
					print(f"\nFILE EXISTS\n{default}\trenamed to\t{os.path.basename(new)}")
				os.rename(default, new)


def processingFile(filename, destination):
	'''
	формирование файла с новым названием, т.к файл с первоначальным названием уже существует
	'''

	filesList = [_ for _ in os.listdir(destination) if filename in _]

	pickedFileName = '.'.join(filename.split('.')[:-1])
	fileDigit = len(filesList)
	fileExtension = filename.split('.')[-1]

	fileName = f"{pickedFileName}_{fileDigit}.{fileExtension}"

	while fileName in os.listdir(destination):
		fileDigit += 1
		fileName = f"{pickedFileName}_{fileDigit}.{fileExtension}"

	return os.path.join(destination, fileName)


def detectingFolders():
	'''
	проверка наличия папок на диске
	'''

	for folder in folders:
		if not os.path.exists(os.path.join(disk, folder)):
			print(f"{os.path.join(disk, folder)} doesn't exist, creating..")
			os.makedirs(os.path.join(disk, folder))


trackingFolder = "D:\\Downloaded"
disk = "D:\\"
folders = ["_Pictures", "_Documents", "_Audios", "_Videos"] # has to match with extensionList keys order

extensionList = {
	"images": ['jpg', 'bmp', 'png', 'jpeg', 'gif'],
	"documents": ['docx', 'doc', 'pptx', 'pdf', 'xls'],
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
			sleep(10)
	except KeyboardInterrupt:
		observer.stop()

	observer.join()