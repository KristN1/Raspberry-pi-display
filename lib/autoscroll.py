import scrollphathd, threading

class Autoscroll():
    def __init__(self):
        self.enabled = False
        self.run()

    def enable(self):
        print("enabled autoscroll")
        self.enabled = True

    def disable(self):
        print("disabled autoscroll")
        self.enabled = False
    
    def run(self):
        if self.enabled is True:
            print("scrilling")
            threading.Timer(0.1, self.run).start()
            scrollphathd.scroll()
            scrollphathd.show()