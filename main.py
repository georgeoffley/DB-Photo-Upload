import sys
import time
import logging
import watchdog.observers
import watchdog.events

from db import DbClass
from data_parse import Parse

class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.txt'],
                                                             ignore_directories=True, case_sensitive=False)
        
    # This works for processing events after a file is created
    # TODO: Figure out why two events fire after the file is created
    # TODO: Also figure out how to filter out files not created correctly
    def on_created(self, event)  :
        print("Here is the event: % s" % event.src_path)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt = '%Y-%m-%d %H:%M:%S')
    
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    event_handler = Handler()
    
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path, recursive=True)
    
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()