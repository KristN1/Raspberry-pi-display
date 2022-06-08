import threading

class StoppableThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.stop_event = threading.Event()
        self.daemon = True

    def start(self):
        if not self.is_alive():
            self.stop_event.clear()
            threading.Thread.start(self)

    def stop(self):
        if self.is_alive():
            self.stop_event.set()
            self.join()