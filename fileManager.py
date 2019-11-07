from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime
from time import sleep
from re import findall
import os
import sys


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

	fileDigit = 1
	fileExtension = filename.split('.')[-1]

	splited = findall(r"_.+", filename)
	splited_file_name = findall(r".+_", filename)

	if len(splited_file_name):
		splited_file_name = splited_file_name[0][:-1]
	else:
		splited_file_name = '.'.join(filename.split('.')[:-1])

	if len(splited):
		splited = splited[0].split('.')

		if len(splited) > 1:
			splited = splited[0].split("_")[-1]

			if splited.isdigit():
				fileDigit = int(splited)

		elif len(splited) == 1:

			for i, letter in enumerate(splited[0]):
				if letter == "_":
					fileDigit = 0

					while splited[0][i+1].isdigit():
						fileDigit += 1
						i += 1
					break
	else:
		filesList = [_ for _ in os.listdir(destination) if ''.join(filename.split(".")[:-1]) in _]
		fileDigit = len(filesList)

	fileName = f"{splited_file_name}_{fileDigit}.{fileExtension}"

	while fileName in os.listdir(destination):
		fileDigit += 1
		fileName = f"{splited_file_name}_{fileDigit}.{fileExtension}"

	return os.path.join(destination, fileName)


def detectingFolders():
	'''
	проверка наличия папок на диске
	'''

	for folder in folders:
		if not os.path.exists(os.path.join(disk, folder)):
			print(f"{os.path.join(disk, folder)} doesn't exist, creating..")
			os.makedirs(os.path.join(disk, folder))

args = sys.argv[1:]

if len(args):
	trackingFolder = args[0]
	disk = args[1]
else:
	trackingFolder = "D:\\Downloaded"
	disk = "D:\\"

folders = ["_Pictures", "_Documents", "_Audios", "_Videos"] # has to match with extensionList keys order

extensionList = {
	"images": ['jpg', 'bmp', 'png', 'jpeg', 'gif'],
	"documents": ['docx', 'doc', 'pptx', 'pdf', 'xls'],
	"audios": ['ogg', 'mp3'],
	"videos": ['mp4']
}

destinations = [os.path.join(disk, folder) for folder in folders]
detectingFolders()

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