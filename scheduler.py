from threading import Thread
from flylib_timer import Timer
from typing import Callable, Any

class Task:
    func: Callable[[Any], Any]
    period: float | None
    delay: float
    args: tuple[any, ...]
    threaded: bool
    thread: Thread | None = None
    
    last_run_time = 0

    def __init__(
        self,
        func: Callable[[Any], Any],
        period: float = None,
        delay: float = 0,
        args: tuple[any, ...] = (),
        threaded: bool = False
    ):
        self.func = func
        self.period = period
        self.delay = delay
        self.args = args
        self.threaded = threaded

class Scheduler(Timer):
    __periodic_tasks: list[Task] = []
    __one_time_tasks: list[Task] = []
    
    def __init__(self, start=True):
        super().__init__(start)
    
    def update(self):
        super().update()
        
        for task in self.__periodic_tasks:
            if self.get_time() - task.last_run_time >= task.period:
                task.last_run_time = self.get_time()
                if task.threaded:
                    thread = Thread(target=task.func, args=task.args)
                    task.thread = thread
                    thread.start()
                else:
                    task.func(*task.args)
        
        for task in self.__one_time_tasks:
            if self.get_time() - task.last_run_time >= task.delay:
                if task.threaded:
                    thread = Thread(target=task.func, args=task.args)
                    task.thread = thread
                    thread.start()
                else:
                    task.func(*task.args)
                self.__one_time_tasks.remove(task)
        
    def schedule_task(self, task: Task):
        if task.period is None:
            self.__one_time_tasks.append(task)
        else:
            self.__periodic_tasks.append(task)