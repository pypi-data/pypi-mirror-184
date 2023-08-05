from idle_time import IdleMonitor


class Addon():
    name = 'Idle'
    icon = 'mdi:timer-sand'
    unit = 'sec'

    def getInfo(self):
        monitor = IdleMonitor.get_monitor()
        idle_sec = monitor.get_idle_time()
        # idle_min = int(idle_sec / 60)
        return round(idle_sec, 0)
