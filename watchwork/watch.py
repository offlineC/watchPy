import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os
import shutil
from datetime import datetime

timeArr = []
startTime = datetime.now().strftime('%H:%M:%S')
startTimeDT = datetime.now()

print('where do you want to watch? specify full path')
wlocation = input('watch here: ')

# for testing 
if(wlocation == 'this'):
	wlocation = os.getcwd();


print('watching ' + wlocation+ '...' + ' at current time: ' + startTime)

filename = 'timewatch' + str(datetime.now().date()) + '.txt'
file = open( filename, 'w+')
print('print to ' + filename)


def nowTime():
	endTime = datetime.now().strftime('%H:%M:%S')
	endTimeDT = datetime.now()
	
	if(len(timeArr) < 2):
		timeArr.append(startTime)
		file.write('start time: ' + startTime)
		print(timeArr)
	else:
		timeArr[1] = endTime
		# timetaken = timeArr[1][:2] - timeArr[0][:2]
		timetaken = endTimeDT - startTimeDT
		timeform = 'started at: ' + timeArr[0] + '\n' + 'ended at: ' + timeArr[1] + '\n' + 'watching here ' + wlocation + '\n total time taken: ' + str(timetaken)
		print(timeArr);
		file.write(timeform)

		print(timeform)

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




my_event_handler.on_created = on_created
my_event_handler.on_deleted = on_deleted
my_event_handler.on_modified = on_modified

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
   		nowTime()
   		file.close()
   			
my_observer.join()