import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os
import shutil
from datetime import datetime

timeArr = []
currtime = datetime.now().strftime('%H:%M:%S')

print('where do you want to watch? specify full path')
wlocation = input('watch here: ')
print('watching ' + wlocation+ '...' + ' at current time: ' + currtime)


def nowTime():
	currtime = datetime.now().strftime('%H:%M:%S')
	filename = 'timewatch' + str(datetime.now().date()) + '.txt'
	file = open( filename, 'w+')
	print('print to ' + filename)
	
	if(len(timeArr) < 2):
		timeArr.append(currtime)
		file.write('start time: ' + currtime)
		print(timeArr)
	else:
		timeArr[1] = currtime
		print(timeArr)
		timetaken = int(timeArr[1][:2]) - int(timeArr[0][:2])
		timeform = 'started at: ' + timeArr[0] + '\n' + 'ended at: ' + timeArr[1] + '\n' + 'watching here ' + wlocation + '\n total time taken: ' + str(timetaken)
		file.write(timeform)

nowTime()	

if __name__ == "__main__":
	patterns = "*"
	ignore_patterns = ""
	ignore_directories = False
	case_sensitive = True
	my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

def on_created(event):
	print(f"{event.src_path} has been created")
	# insert functions here to run at this event
	nowTime()	



def on_deleted(event):
	print(f"Delete {event.src_path}!")
	# insert functions here to run at this event
	nowTime()	



def on_modified(event):
	print(f"{event.src_path} has been modified")
	# insert functions here to run at this event
	nowTime()	

def on_open(even):
	print(f"{event.src_path} is opened")
	# insert functions here to run at this event
	nowTime()	


my_event_handler.on_created = on_created
my_event_handler.on_deleted = on_deleted
my_event_handler.on_modified = on_modified
my_event_handler.on_open = on_open

path = wlocation
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)


my_observer.start()
try:
    while True:
        time.sleep(1)
         
except KeyboardInterrupt:
   		my_observer.stop()
   			
my_observer.join()