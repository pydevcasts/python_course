import time
from multiprocessing import Process


def show(name, delay):
    print(f"Starting with {name} - {delay}")
    time.sleep(4)
    print(f"Ending with {name} - {delay}")

class ShowProcess(Process):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        show(self.name, self.delay)

process1 = ShowProcess("siyamak", 2)
process2 = ShowProcess("diyana", 3)
process1.start()        
process2.start()         
process1.join()        
process2.join()   