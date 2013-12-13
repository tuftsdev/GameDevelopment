def convertTimeFormat(seconds):
	''' Assume seconds is not negative '''
	hours = seconds / 3600
	seconds = seconds % 3600
	minutes = seconds / 60
	seconds = seconds % 60
	if seconds <= 9:
		seconds = "0" + str(seconds)
	else:
		seconds = str(seconds)
	if minutes <= 9:
		minutes = "0" + str(minutes)
	else:
		minutes = str(minutes)
	if hours <= 9:
		hours = "0" + str(hours)
	else:
		hours = str(hours)
	return hours + ":" + minutes + ":" + seconds

seconds = 90
while seconds > 0:
	print convertTimeFormat(seconds)
	seconds-=1
