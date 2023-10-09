from driver_dashboard import DriverDashboard
from timed_tello import TimedTello

class Drone(TimedTello):
    def update(self):
        super().update()
        print("override update")

drone = Drone()
dashboard = DriverDashboard(drone, dev_server=True)

dashboard.start()