import webview
import screeninfo
from timed_tello import TimedTello
from typing import Callable, Any
from flask_cors import CORS

class DriverDashboard:
    drone: TimedTello = None
    
    control_window: webview.Window = None
    telemetry_window: webview.Window = None
    
    WINDOW_HEIGHT = 250
    WINDOW_MARGIN_BOTTOM = 10
    WINDOW_PADDING_X = 10
    
    DEV_SERVER_PORT = 5173
    
    def __init__(self, drone: TimedTello, dev_server=False, dev_server_port=DEV_SERVER_PORT):
        self.drone = drone
        monitor = self.__get_primary_monitor()

        self.control_window = webview.create_window(
            title="FlyLib Driver Dashboard Controls",
            url=f"http://localhost:{str(dev_server_port)}/controls" if dev_server else "controls.html",
            resizable=True,
            frameless=True,
            easy_drag=True,
            on_top=True,
            confirm_close=True,
            x=monitor.x - (self.WINDOW_PADDING_X // 2),
            y=monitor.height - self.WINDOW_HEIGHT - self.WINDOW_MARGIN_BOTTOM,
            width=monitor.width + (self.WINDOW_PADDING_X * 2),
            height=self.WINDOW_HEIGHT
        )
        
        self.control_window = webview.create_window(
            title="FlyLib Driver Dashboard Telemetry",
            url=f"http://localhost:{str(dev_server_port)}/telemetry" if dev_server else "telemetry.html",
            resizable=True,
            x=monitor.x - (self.WINDOW_PADDING_X // 2),
            y=0,
            width=monitor.width + (self.WINDOW_PADDING_X * 2),
            height=monitor.height - self.WINDOW_HEIGHT - self.WINDOW_MARGIN_BOTTOM
        )
    
    def start(
        self,
        func: Callable[[Any], Any] = None,
        args: tuple[Any, ...] = None,
        localization={},
        gui=None,
        debug=False,
        http_server=True,
        user_agent=None
    ):
        webview.start(func, args, localization, gui, debug, http_server, user_agent)
    
    def __get_primary_monitor(self):
        monitors = screeninfo.get_monitors()
        for monitor in monitors:
            if monitor.is_primary:
                return monitor
        return monitors[0]

if __name__ == "__main__":
    dashboard = DriverDashboard()
    dashboard.start()