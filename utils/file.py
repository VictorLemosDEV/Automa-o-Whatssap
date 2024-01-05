def clean_file(file):
	file = open(file,"r+")

	file.truncate(0)
	
	file.close()

def read_file(file, array=False):
	f = open(file, "r",encoding="utf-8")
	lines = f.read()

	if array:
		lines = lines.split('\n')

	f.close()

	return lines

def write_file(file, message):
	f = open(file, "a",encoding="utf-8")
	f.write(f"{message}\n")

	f.close()

	return "Success"

def replace_file(file, message):
	f = open(file, "w",encoding="utf-8")
	f.write(f"{message}\n")

	f.close()

	return "Success"