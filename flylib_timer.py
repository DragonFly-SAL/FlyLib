import time
import threading

class Timer:
    __start_time = 0
    __last_time = 0
    __end_time = 0
    __running_time = 0
    __current_time = 0
    __update_thread = None
    __running = False

    def __init__(self, start=True):
        self.reset()
    
        if start:
            self.start()
    
    def reset(self):
        self.__start_time = time.time()
        self.__last_time = self.__start_time
    
    def start(self):
        self.__running = True
        self.__update_thread = threading.Thread(target=self.update_loop)
        self.__update_thread.start()
    
    def stop(self):
        self.__end_time = time.time()
        self.__running = False
        self.__update_thread.join()
    
    def update(self):
        current_time = time.time()
        self.__current_time = current_time
        self.__running_time += current_time - self.__last_time
        self.__last_time = current_time
    
    def update_loop(self):
        while self.__running:
            self.update()
    
    def get_time(self):
        return self.__running_time

    def get_delta(self):
        return time.time() - self.__last_time
    
    def get_start_time(self):
        return self.__start_time
    
    def get_end_time(self):
        return self.__end_time
    
    def get_running(self):
        return self.__running

    def __repr__(self) -> str:
        return f"Timer({str(self.get_time())}s, {'paused' if not self.get_running() else 'running'})"

# Test code
if __name__ == "__main__":
    import random
    time_to_wait = random.random() * 10
    print("time_to_wait:", time_to_wait)
    timer = Timer()
    timer.start()
    time.sleep(time_to_wait)
    timer.stop()
    stop_time = timer.get_time()
    print("timer.get_time:", stop_time)
    print("timer.get_end_time:", timer.get_end_time())
    print("timer.get_start_time:", timer.get_start_time())
    print("timer.get_delta:", timer.get_delta())
    print("timer.get_running:", timer.get_running())
    print("timer:", timer)
    print("\nAccuracy: ", stop_time - time_to_wait)