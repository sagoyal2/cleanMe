import os
import sys

def getFilesInDesktop(home_path):
	"""
	remove files only

	return: tuple (str, list)
			("Desktop", ["filename.txt", ...])
	"""

	desktop_path = os.path.join(home_path, "Desktop")

	list_of_files_and_folders = os.listdir(desktop_path)
	list_of_files = [file for file in list_of_files_and_folders if os.path.isfile(os.path.join(desktop_path, file))]

	return ("Desktop", list_of_files)


def getFilesInDocuments(home_path):
	"""
	remove files only

	return: tuple (str, list)
			("Documents", ["filename.txt", ...])
	"""

	documents_path = os.path.join(home_path, "Documents")

	list_of_files_and_folders = os.listdir(documents_path)
	list_of_files = [file for file in list_of_files_and_folders if os.path.isfile(os.path.join(documents_path, file))]

	return ("Documents", list_of_files)

def getFilesInDownloads(home_path):
	"""
	remove both files and folders

	return: tuple (str, list)
			("Documents", ["foldername", "filename.txt", ...])
	"""

	downloads_path = os.path.join(home_path, "Downloads")

	list_of_files_and_folders = os.listdir(downloads_path)

	return ("Downloads", list_of_files_and_folders)


#https://stackoverflow.com/questions/3041986/apt-command-line-interface-like-yes-no-input
def query_yes_no(question, default="yes"):
	"""Ask a yes/no question via raw_input() and return their answer.

	"question" is a string that is presented to the user.
	"default" is the presumed answer if the user just hits <Enter>.
		It must be "yes" (the default), "no" or None (meaning
		an answer is required of the user).

	The "answer" return value is True for "yes" or False for "no".
	"""
	valid = {"yes": True, "y": True, "ye": True,
			 "no": False, "n": False}
	if default is None:
		prompt = " [y/n] "
	elif default == "yes":
		prompt = " [Y/n] "
	elif default == "no":
		prompt = " [y/N] "
	else:
		raise ValueError("invalid default answer: '%s'" % default)

	while True:
		choice = input(question + prompt).lower()
		if default is not None and choice == '':
			return valid[default]
		elif choice in valid:
			return valid[choice]
		else:
			sys.stdout.write("Please respond with 'yes' or 'no' "
							 "(or 'y' or 'n').\n")

def move_to_trash(home_path, location, filename):
	"""
	places the files into trash
	"""

	trash_path = os.path.join(home_path, '.Trash')

	current_file_path = os.path.join(home_path, location, filename)
	new_file_path = os.path.join(trash_path, filename)

	os.replace(current_file_path, new_file_path)

def main():
	home_path = os.environ['HOME']

	list_tuple_location_files =[getFilesInDesktop(home_path),
								getFilesInDocuments(home_path),
								getFilesInDownloads(home_path)]

	do_not_remove_list = ['.DS_Store', '.localized']


	for (location, _list) in list_tuple_location_files:
		print(f"Folder Location is: {location}")

		for filename in _list:
			if(filename in do_not_remove_list):
				continue

			question = "Trash file: "+ filename
			response = query_yes_no(question , "yes")
			
			if(response):
				#case when the user selects to "Delete" aka move to Trash the file
				move_to_trash(home_path, location, filename)

		print()


if __name__ == '__main__':
	main()













