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
	prefix = ""
	result = subprocess.check_output("ls /Users/amrita/Calendars\ and\ Reminders\ 5.11.15\,\ 8.01\ AM.icbu/Calendars/71DC31D8-F50B-4934-B17C-14370E802B17.caldav/*.calendar/Events", shell=True)
	for item in result.split('\n'):
		if "Event" in item:
			prefix=item.split(':')[0]

		if ".ics" not in item:
			continue

		validDate = True
		# get today's date

		f = open(prefix+"/"+item, 'r')
		for line in f.readlines():
			if "DTSTART" in line:
				if "2014" in line:
					validDate = False

		f.close()

		if validDate is False:
			pdb.set_trace()
			print(item)
			# this won't work - need to escape this string properly
			subprocess.call("rm "+prefix+"/"+item, shell=True)
		


if __name__ == '__main__':
	# export calendar entries
	# delete birthday and notification folders
	# create data structure for all entries
	process_cals()
	print("hello!")