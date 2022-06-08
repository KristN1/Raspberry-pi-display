import scrollphathd, threading

class Autoscroll():
    def __init__(self):
        self.status = False

    def enable(self):
        self.status = True
        self.run()

    def disable(self):
        self.status = False
    
    def run(self):
        if self.status is True:
            threading.Timer(0.1, self.run).start()
            scrollphathd.scroll()
            scrollphathd.show()