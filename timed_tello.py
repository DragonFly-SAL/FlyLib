from djitellopy import Tello
from scheduler import Scheduler, Task

class TimedTello(Tello):
    UPDATE_RATE = 100 # Times per second
    FIXED_UPDATE_RATE = 1 # Times per second
    
    __scheduler = Scheduler()
    
    def __init__(self, host=Tello.TELLO_IP, retry_count=Tello.RETRY_COUNT):
        super().__init__(host, retry_count)
        self.__scheduler.schedule_task(Task(self.update, period=1/self.UPDATE_RATE))
        self.__scheduler.schedule_task(Task(self.fixed_update, period=1/self.FIXED_UPDATE_RATE))

    def update(self):
        print("update")
    
    def fixed_update(self):
        print("fixed_update")

if __name__ == "__main__":
    tello = TimedTello()