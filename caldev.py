import pdb, subprocess

# TODO: add an argument to set the time period, and make
# process_cals delete everything before that date

# random other stuff

def export_cal():
	print("making calendar archive")

def archive_cleanup():
	print("cleaning up archive")

def process_cals():
	print("processing calendars")
	print("\t deleting all entries older than 7 days")
	for item in subprocess.check_output("ls *.calendar\Events"+, shell=True):
		if ".ics" not in item:
			continue

		f = open(item, 'r')
		


if __name__ == '__main__':
	# export calendar entries
	# delete birthday and notification folders
	# create data structure for all entries
	print("hello!")